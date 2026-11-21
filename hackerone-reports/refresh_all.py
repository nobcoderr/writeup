#!/usr/bin/env python3
"""Refresh the local HackerOne disclosed-report corpora.

Pulls public disclosed reports, the official weakness catalog, and the
program directory from HackerOne GraphQL. Merges with data.csv, fills
new-report metadata from the public report JSON, then rebuilds:

  - this reddelexc-style repo: every program and every weakness
  - ../hackerone-bug-bounty-reports: codebygk-style indexes

Unauthenticated public data only. Does not use the researcher session.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent
CODEBYGK = ROOT.parent / "hackerone-bug-bounty-reports"
CACHE = ROOT / "cache"
CSV_PATH = ROOT / "data.csv"
FULL_JSON = CACHE / "reports_full.json"
WEAKNESS_CACHE = CACHE / "weaknesses.json"
TEAM_CACHE = CACHE / "teams.json"

GRAPHQL = "https://hackerone.com/graphql"
REPORT_JSON = "https://hackerone.com/reports/{rid}.json"
PAGE_SIZE = 100
GRAPHQL_SLEEP = 0.12
JSON_WORKERS = 6
WINDOW_SPLIT_AT = 14000
PUBLIC_TEAM_STATES = {"public_mode", "soft_launched"}
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)

KEYWORD_BUG_TYPES = [
    ("XSS", "XSS", ["css", "xss", "domxss", "cross site scripting"]),
    ("XXE", "XXE", ["xxe", "xml external entity", "xml entity"]),
    ("CSRF", "CSRF", ["csrf", "xsrf", "cross site request forgery"]),
    ("IDOR", "IDOR", ["idor", "insecure direct object reference"]),
    ("RCE", "RCE", ["rce", "remote code execution"]),
    ("SQLI", "SQLI", ["sqli", "sql inj", "sql command injection"]),
    ("SSRF", "SSRF", ["ssrf", "server side request forgery"]),
    ("RACECONDITION", "Race Condition", ["race condition"]),
    ("SUBDOMAINTAKEOVER", "Subdomain Takeover", ["domain takeover", "domain take over"]),
    ("OPENREDIRECT", "Open Redirect", ["open redirect"]),
    ("CLICKJACKING", "Clickjacking", ["clickjacking", "click jacking", "clicjacking"]),
    ("DOS", "DoS", ["dos", "denial of service", "service denial"]),
    ("OAUTH", "OAuth", ["oauth"]),
    ("ACCOUNTTAKEOVER", "Account Takeover", ["account takeover", "ato"]),
    ("BUSINESSLOGIC", "Business Logic", [
        "functional", "logic", "function", "functionality",
        "manipulating response", "response manipulation", "manipulation",
    ]),
    ("API", "REST API", ["api", "rest api", "restapi"]),
    ("GRAPHQL", "GraphQL", ["graphql", "graphql api", "api graphql"]),
    ("INFODISCLOSURE", "Information Disclosure", [
        "information disclosure", "infos disclosure", "user information", "pii",
    ]),
    ("WEBCACHE", "Web Cache", ["web cache poisoning", "web cache", "web cache deception"]),
    ("SSTI", "SSTI", ["ssti", "server side template injection"]),
    ("UPLOAD", "Upload", ["upload", "unrestricted file upload", "file upload"]),
    ("REQUESTSMUGGLING", "Request Smuggling", ["request smuggling", "http request smuggling"]),
    ("OPENID", "OpenID", ["openid", "saml", "sso"]),
    ("MOBILE", "Mobile", ["mobile", "android", "ios", "apk"]),
    ("FILEREADING", "File Reading", ["lfi", "rfi", "file reading", "path", "traversal", "file inclusion"]),
    ("AUTHORIZATION", "Authorization Bypass", [
        "authorization bypass", "authorization", "able to access", "access control",
        "ability", "privilege", "escalation", "admin", "unauthorized", "permission",
    ]),
    ("AUTH", "Authentication", ["authentication bypass", "authentication", "auth"]),
    ("MFA", "MFA", ["mfa", "2fa", "two factor", "two_factor", "multi factor", "multi_factor"]),
]

REPORTS_QUERY = """
query($first:Int, $after:String, $where:FiltersReportFilterInput) {
  reports(first:$first, after:$after, where:$where) {
    pageInfo { hasNextPage endCursor }
    edges {
      node {
        _id
        title
        url
        substate
        disclosed_at
        created_at
        cve_ids
        severity { rating }
        weakness { name external_id }
        team { handle name }
        structured_scope { asset_type }
        bounties { edges { node { amount bonus_amount } } }
      }
    }
  }
}
"""

WEAKNESSES_QUERY = """
query($first:Int, $after:String) {
  weaknesses(first:$first, after:$after) {
    pageInfo { hasNextPage endCursor }
    edges { node { _id name external_id } }
  }
}
"""

TEAMS_QUERY = """
query($first:Int, $after:String) {
  teams(first:$first, after:$after) {
    pageInfo { hasNextPage endCursor }
    edges { node { handle name state offers_bounties } }
  }
}
"""


def log(msg: str) -> None:
    print(msg, flush=True)


def session() -> requests.Session:
    s = requests.Session()
    s.headers.update({
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://hackerone.com",
        "Referer": "https://hackerone.com/hacktivity/overview",
    })
    return s


def graphql(s: requests.Session, query: str, variables: dict, retries: int = 6) -> dict:
    last = None
    delay = 1.0
    for attempt in range(retries):
        try:
            r = s.post(GRAPHQL, json={"query": query, "variables": variables}, timeout=60)
            if r.status_code in (429, 500, 502, 503, 504):
                last = RuntimeError(f"HTTP {r.status_code}")
                time.sleep(delay)
                delay = min(delay * 2, 30)
                continue
            r.raise_for_status()
            data = r.json()
            if data.get("errors"):
                message = data["errors"][0].get("message", "graphql error")
                if "rate" in message.lower() or "timeout" in message.lower():
                    last = RuntimeError(message)
                    time.sleep(delay)
                    delay = min(delay * 2, 30)
                    continue
                raise RuntimeError(message)
            return data["data"]
        except (requests.RequestException, ValueError, RuntimeError) as err:
            last = err
            time.sleep(delay)
            delay = min(delay * 2, 30)
    raise RuntimeError(f"GraphQL failed after retries: {last}")


def paginate(
    s: requests.Session,
    query: str,
    root: str,
    variables: dict | None = None,
    quiet: bool = False,
) -> list[dict]:
    after = None
    items: list[dict] = []
    while True:
        vars_ = {"first": PAGE_SIZE, "after": after}
        if variables:
            vars_.update(variables)
        conn = graphql(s, query, vars_)[root]
        edges = conn.get("edges") or []
        items.extend(edge["node"] for edge in edges)
        page_info = conn["pageInfo"]
        if not quiet:
            log(f"  {root}: {len(items)} (+{len(edges)}) hasNext={page_info.get('hasNextPage')}")
        if not page_info.get("hasNextPage"):
            break
        after = page_info.get("endCursor")
        if not after:
            break
        if len(items) >= WINDOW_SPLIT_AT and root == "reports":
            break
        time.sleep(GRAPHQL_SLEEP)
    return items


def bounty_sum(node: dict) -> float:
    total = 0.0
    bounties = node.get("bounties") or {}
    for edge in bounties.get("edges") or []:
        amount = (edge.get("node") or {}).get("amount") or 0
        bonus = (edge.get("node") or {}).get("bonus_amount") or 0
        try:
            total += float(amount) + float(bonus)
        except (TypeError, ValueError):
            continue
    return total


def node_to_report(node: dict) -> dict:
    rid = str(node.get("_id") or "").strip()
    team = node.get("team") or {}
    weakness = node.get("weakness") or {}
    severity = node.get("severity") or {}
    scope = node.get("structured_scope") or {}
    url = node.get("url") or f"https://hackerone.com/reports/{rid}"
    link = url.replace("https://", "").replace("http://", "").rstrip("/")
    return {
        "id": rid,
        "program": (team.get("name") or "").strip(),
        "handle": (team.get("handle") or "").strip(),
        "title": node.get("title") or "",
        "link": link,
        "url": url if url.startswith("http") else f"https://{link}",
        "upvotes": 0,
        "bounty": bounty_sum(node),
        "vuln_type": (weakness.get("name") or "").strip(),
        "external_id": (weakness.get("external_id") or "").strip(),
        "severity": (severity.get("rating") or "").strip(),
        "state": (node.get("substate") or "").strip(),
        "asset_type": (scope.get("asset_type") or "").strip(),
        "submitted_at": node.get("created_at") or "",
        "disclosed_at": node.get("disclosed_at") or "",
        "cve_ids": node.get("cve_ids") or [],
    }


def month_windows(start_iso: str, end_iso: str) -> list[tuple[str, str, str]]:
    start = datetime.fromisoformat(start_iso.replace("Z", "+00:00"))
    end = datetime.fromisoformat(end_iso.replace("Z", "+00:00"))
    windows = []
    year, month = start.year, start.month
    while datetime(year, month, 1, tzinfo=timezone.utc) < end:
        cur = datetime(year, month, 1, tzinfo=timezone.utc)
        if month == 12:
            nxt = datetime(year + 1, 1, 1, tzinfo=timezone.utc)
        else:
            nxt = datetime(year, month + 1, 1, tzinfo=timezone.utc)
        if nxt > end:
            nxt = end
        windows.append((
            cur.strftime("%Y-%m-%dT00:00:00.000Z"),
            nxt.strftime("%Y-%m-%dT00:00:00.000Z"),
            f"{year}-{month:02d}",
        ))
        year, month = (year + 1, 1) if month == 12 else (year, month + 1)
    return windows


def fetch_reports_window(s: requests.Session, start: str, end: str, label: str) -> list[dict]:
    log(f"Fetching disclosed reports {label} ({start} .. {end})")
    where = {"disclosed_at": {"_gte": start, "_lt": end}}
    nodes = paginate(s, REPORTS_QUERY, "reports", {"where": where})
    if len(nodes) >= WINDOW_SPLIT_AT:
        log(f"  {label} hit {len(nodes)}; splitting into months")
        merged: dict[str, dict] = {}
        for m_start, m_end, m_label in month_windows(start, end):
            for node in fetch_reports_window(s, m_start, m_end, m_label):
                merged[node["id"]] = node
        return list(merged.values())
    reports = [node_to_report(node) for node in nodes if node.get("_id")]
    log(f"  {label}: {len(reports)} reports")
    return reports


def fetch_all_reports(s: requests.Session, resume: bool = False) -> list[dict]:
    now = datetime.now(timezone.utc)
    start_year = 2013
    merged: dict[str, dict] = {}
    year_dir = CACHE / "years"
    year_dir.mkdir(parents=True, exist_ok=True)
    for year in range(start_year, now.year + 1):
        year_path = year_dir / f"{year}.json"
        if resume and year_path.exists() and year < now.year:
            year_reports = json.loads(year_path.read_text(encoding="utf-8"))
            log(f"Resume {year}: {len(year_reports)} cached reports")
        else:
            start = f"{year}-01-01T00:00:00.000Z"
            end = f"{year + 1}-01-01T00:00:00.000Z"
            year_reports = fetch_reports_window(s, start, end, str(year))
            year_path.write_text(json.dumps(year_reports, ensure_ascii=False), encoding="utf-8")
        for report in year_reports:
            merged[report["id"]] = report
        (CACHE / "reports_graphql.json").write_text(
            json.dumps(list(merged.values()), ensure_ascii=False),
            encoding="utf-8",
        )
    log(f"GraphQL disclosed reports: {len(merged)}")
    return list(merged.values())


def fetch_catalog(s: requests.Session, query: str, root: str, cache_path: Path) -> list[dict]:
    log(f"Fetching {root} catalog")
    items = paginate(s, query, root)
    CACHE.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
    log(f"{root}: {len(items)}")
    return items


def load_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def report_id_from_link(link: str) -> str:
    match = re.search(r"/reports/(\d+)", link or "")
    return match.group(1) if match else ""


def parse_bounty(value) -> float:
    try:
        return float(str(value).replace('"', "").replace("$", "").replace(",", "").strip() or 0)
    except ValueError:
        return 0.0


def parse_upvotes(value) -> int:
    try:
        return int(str(value).strip() or 0)
    except ValueError:
        return 0


def merge_reports(existing_rows: list[dict], fetched: list[dict]) -> tuple[list[dict], list[str]]:
    existing: dict[str, dict] = {}
    for row in existing_rows:
        rid = report_id_from_link(row.get("link", ""))
        if not rid:
            continue
        existing[rid] = {
            "id": rid,
            "program": row.get("program") or "",
            "handle": "",
            "title": row.get("title") or "",
            "link": row.get("link") or f"hackerone.com/reports/{rid}",
            "url": "https://" + (row.get("link") or f"hackerone.com/reports/{rid}"),
            "upvotes": parse_upvotes(row.get("upvotes")),
            "bounty": parse_bounty(row.get("bounty")),
            "vuln_type": row.get("vuln_type") or "",
            "external_id": "",
            "severity": "",
            "state": "",
            "asset_type": "",
            "submitted_at": "",
            "disclosed_at": "",
            "cve_ids": [],
        }

    new_ids = []
    for report in fetched:
        rid = report["id"]
        old = existing.get(rid)
        if old is None:
            existing[rid] = report
            new_ids.append(rid)
            continue
        old["program"] = report["program"] or old["program"]
        old["handle"] = report["handle"] or old["handle"]
        old["title"] = report["title"] or old["title"]
        old["link"] = report["link"] or old["link"]
        old["url"] = report["url"] or old["url"]
        if report["bounty"] > 0:
            old["bounty"] = report["bounty"]
        old["vuln_type"] = report["vuln_type"] or old["vuln_type"]
        old["external_id"] = report["external_id"] or old["external_id"]
        old["severity"] = report["severity"] or old["severity"]
        old["state"] = report["state"] or old["state"]
        old["asset_type"] = report["asset_type"] or old["asset_type"]
        old["submitted_at"] = report["submitted_at"] or old["submitted_at"]
        old["disclosed_at"] = report["disclosed_at"] or old["disclosed_at"]
        old["cve_ids"] = report["cve_ids"] or old["cve_ids"]
        existing[rid] = old
    return list(existing.values()), new_ids


def fetch_report_json(s: requests.Session, rid: str) -> dict | None:
    delay = 1.0
    for _ in range(5):
        try:
            r = s.get(REPORT_JSON.format(rid=rid), timeout=30)
            if r.status_code == 429:
                time.sleep(delay)
                delay = min(delay * 2, 20)
                continue
            if r.status_code == 404:
                return None
            r.raise_for_status()
            return r.json()
        except requests.RequestException:
            time.sleep(delay)
            delay = min(delay * 2, 20)
    return None


def apply_json(report: dict, payload: dict) -> None:
    team = payload.get("team") or {}
    profile = team.get("profile") or {}
    weakness = payload.get("weakness") or {}
    scope = payload.get("structured_scope") or {}
    report["title"] = payload.get("title") or report["title"]
    report["program"] = profile.get("name") or report["program"]
    if payload.get("vote_count") is not None:
        report["upvotes"] = int(payload.get("vote_count") or 0)
    if payload.get("has_bounty?"):
        report["bounty"] = parse_bounty(payload.get("bounty_amount") or 0)
    report["vuln_type"] = (weakness.get("name") or report["vuln_type"] or "").strip()
    report["severity"] = payload.get("severity_rating") or report["severity"]
    report["state"] = payload.get("state") or report["state"]
    report["asset_type"] = scope.get("asset_type") or report["asset_type"]
    report["submitted_at"] = payload.get("submitted_at") or report["submitted_at"]
    report["disclosed_at"] = payload.get("disclosed_at") or report["disclosed_at"]


def fill_new_reports(reports: list[dict], new_ids: list[str]) -> None:
    if not new_ids:
        log("No new reports to fill from JSON")
        return
    by_id = {report["id"]: report for report in reports}
    log(f"Filling {len(new_ids)} new reports from public JSON")
    s = session()

    def work(rid: str):
        payload = fetch_report_json(s, rid)
        return rid, payload

    done = 0
    with ThreadPoolExecutor(max_workers=JSON_WORKERS) as pool:
        futures = [pool.submit(work, rid) for rid in new_ids]
        for fut in as_completed(futures):
            rid, payload = fut.result()
            done += 1
            if payload:
                apply_json(by_id[rid], payload)
            if done % 25 == 0 or done == len(new_ids):
                log(f"  JSON fill {done}/{len(new_ids)}")


def sort_reports(reports: list[dict]) -> list[dict]:
    def key(report: dict):
        disclosed = report.get("disclosed_at") or ""
        rid = int(report["id"]) if str(report.get("id", "")).isdigit() else 0
        return (disclosed, rid)

    return sorted(reports, key=key, reverse=True)


def write_csv(reports: list[dict], path: Path) -> None:
    fieldnames = ["program", "title", "link", "upvotes", "bounty", "vuln_type"]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for report in reports:
            writer.writerow({
                "program": report.get("program") or "",
                "title": report.get("title") or "",
                "link": report.get("link") or f"hackerone.com/reports/{report['id']}",
                "upvotes": int(report.get("upvotes") or 0),
                "bounty": float(report.get("bounty") or 0),
                "vuln_type": report.get("vuln_type") or "",
            })


def clean_title(title: str) -> str:
    return " ".join((title or "").split()).lower().replace("-", " ").replace("—", " ") \
        .replace(",", "").replace(".", "").replace(":", "").replace(";", "")


def check_title(title: str, keywords: list[str]) -> bool:
    for keyword in keywords:
        if len(keyword.split()) == 1:
            if keyword in title.split():
                return True
        elif keyword in title:
            return True
    return False


def md_escape(title: str) -> str:
    return (title or "").replace("<", r"\<").replace(">", r"\>")


def program_slug(name: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "", (name or "unknown").upper())
    return slug or "UNKNOWN"


def weakness_slug(name: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "", (name or "unknown").upper())
    return slug or "UNKNOWN"


def codebygk_slug(name: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9\s\-()]+", " ", name or "unknown")
    text = re.sub(r"[^a-zA-Z0-9]", " ", text).lower()
    text = re.sub(r"\s+", " ", text).strip().replace(" ", "_")
    return text or "unknown"


def select_directory_teams(teams: list[dict]) -> list[dict]:
    """Keep live public/soft-launched programs; drop unpublished directory junk."""
    selected = []
    seen = set()
    for team in teams:
        if team.get("state") not in PUBLIC_TEAM_STATES:
            continue
        name = (team.get("name") or "").strip()
        if not name or name in seen:
            continue
        seen.add(name)
        selected.append(team)
    return selected


def unique_slug(base: str, used: dict[str, str], key: str) -> str:
    if key in used:
        return used[key]
    slug = base
    n = 2
    reverse = {v: k for k, v in used.items()}
    while slug in reverse and reverse[slug] != key:
        slug = f"{base}{n}"
        n += 1
    used[key] = slug
    return slug


def write_report_list(path: Path, heading: str, reports: list[dict], empty_note: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [heading, ""]
    if not reports:
        lines.append(empty_note)
        lines.append("")
    else:
        for i, report in enumerate(reports, 1):
            title = md_escape(report.get("title") or "(untitled)")
            link = report.get("link") or f"hackerone.com/reports/{report.get('id')}"
            program = report.get("program") or "Unknown"
            upvotes = int(report.get("upvotes") or 0)
            bounty = int(float(report.get("bounty") or 0))
            lines.append(
                f"{i}. [{title}](https://{link}) to {program} - {upvotes} upvotes, ${bounty}"
            )
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_table(path: Path, heading: str, reports: list[dict], columns: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [heading, "", columns, "| ---- | ----- | ------ |"]
    if "Upvotes" in columns:
        lines[3] = "| ---- | ----- | ------ | ------- |"
    if not reports:
        lines.append("|  | No disclosed public reports in this corpus. |  |")
        if "Upvotes" in columns:
            lines[-1] = "|  | No disclosed public reports in this corpus. |  |  |"
    else:
        for i, report in enumerate(reports, 1):
            title = (report.get("title") or "(untitled)").replace("|", "&#124;")
            url = report.get("url") or f"https://{report.get('link')}"
            bounty = report.get("bounty") or 0
            if "Upvotes" in columns:
                lines.append(f"| {i} | [{title}]({url}) | ${bounty} | {int(report.get('upvotes') or 0)} |")
            else:
                lines.append(f"| {i} | [{title}]({url}) | ${bounty} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def ranked(reports: list[dict]) -> list[dict]:
    return list(reversed(sorted(reports, key=lambda r: (int(r.get("upvotes") or 0), float(r.get("bounty") or 0)))))


def bounty_ranked(reports: list[dict]) -> list[dict]:
    return list(reversed(sorted(reports, key=lambda r: (float(r.get("bounty") or 0), int(r.get("upvotes") or 0)))))


def build_reddelexc_indexes(reports: list[dict], weaknesses: list[dict], teams: list[dict]) -> dict:
    teams = select_directory_teams(teams)
    docs = ROOT / "docs"
    (docs / "tops_100").mkdir(parents=True, exist_ok=True)
    (docs / "tops_by_bug_type").mkdir(parents=True, exist_ok=True)
    (docs / "tops_by_weakness").mkdir(parents=True, exist_ok=True)
    (docs / "tops_by_program").mkdir(parents=True, exist_ok=True)

    categories = {"tops_100": [], "tops_by_bug_type": [], "tops_by_weakness": [], "tops_by_program": []}

    write_report_list(
        docs / "tops_100" / "TOP100UPVOTED.md",
        "Top 100 upvoted reports from HackerOne:",
        ranked(reports)[:100],
        "Not enough reports.",
    )
    categories["tops_100"].append({"name": "Top 100 Upvoted", "file": "tops_100/TOP100UPVOTED.md"})
    write_report_list(
        docs / "tops_100" / "TOP100PAID.md",
        "Top 100 paid reports from HackerOne:",
        bounty_ranked(reports)[:100],
        "Not enough reports.",
    )
    categories["tops_100"].append({"name": "Top 100 Paid", "file": "tops_100/TOP100PAID.md"})

    wanted_bug = set()
    for slug, name, keywords in KEYWORD_BUG_TYPES:
        filtered = [r for r in reports if check_title(clean_title(r.get("title") or ""), keywords)]
        rel = f"tops_by_bug_type/TOP{slug}.md"
        write_report_list(docs / rel, f"Top {name} reports from HackerOne:", ranked(filtered), "No matching reports.")
        categories["tops_by_bug_type"].append({"name": name, "file": rel})
        wanted_bug.add(f"TOP{slug}.md")
    for stale in (docs / "tops_by_bug_type").glob("*.md"):
        if stale.name not in wanted_bug:
            stale.unlink()

    reports_by_weakness: dict[str, list[dict]] = defaultdict(list)
    for report in reports:
        name = (report.get("vuln_type") or "").strip()
        if name:
            reports_by_weakness[name].append(report)

    catalog_names = []
    seen_names = set()
    for item in weaknesses:
        name = (item.get("name") or "").strip()
        if name and name not in seen_names:
            seen_names.add(name)
            catalog_names.append(name)
    for name in sorted(reports_by_weakness, key=str.lower):
        if name not in seen_names:
            catalog_names.append(name)
            seen_names.add(name)

    weakness_slugs: dict[str, str] = {}
    wanted_weak = set()
    for name in catalog_names:
        slug = unique_slug(weakness_slug(name), weakness_slugs, name)
        rel = f"tops_by_weakness/TOP{slug}.md"
        write_report_list(
            docs / rel,
            f"Top {name} reports from HackerOne:",
            ranked(reports_by_weakness.get(name, [])),
            "No disclosed public reports for this weakness in the corpus.",
        )
        categories["tops_by_weakness"].append({"name": name, "file": rel, "count": len(reports_by_weakness.get(name, []))})
        wanted_weak.add(f"TOP{slug}.md")
    for stale in (docs / "tops_by_weakness").glob("*.md"):
        if stale.name not in wanted_weak:
            stale.unlink()

    reports_by_program: dict[str, list[dict]] = defaultdict(list)
    for report in reports:
        name = (report.get("program") or "").strip()
        if name:
            reports_by_program[name].append(report)

    program_names = []
    seen_programs = set()
    for team in teams:
        name = (team.get("name") or "").strip()
        if name and name not in seen_programs:
            seen_programs.add(name)
            program_names.append(name)
    extra_programs = sorted(set(reports_by_program) - seen_programs, key=str.lower)
    program_names.extend(extra_programs)

    # Keep programs with reports first, then catalog-only programs, alpha within groups.
    program_names.sort(key=lambda n: (0 if reports_by_program.get(n) else 1, n.lower()))

    program_slugs: dict[str, str] = {}
    wanted_prog = set()
    for name in program_names:
        slug = unique_slug(program_slug(name), program_slugs, name)
        rel = f"tops_by_program/TOP{slug}.md"
        write_report_list(
            docs / rel,
            f"Top reports from {name} program at HackerOne:",
            ranked(reports_by_program.get(name, [])),
            "No disclosed public reports for this program in the corpus.",
        )
        categories["tops_by_program"].append({"name": name, "file": rel, "count": len(reports_by_program.get(name, []))})
        wanted_prog.add(f"TOP{slug}.md")
    for stale in (docs / "tops_by_program").glob("*.md"):
        if stale.name not in wanted_prog:
            stale.unlink()

    (docs / "categories.json").write_text(
        json.dumps(categories, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return categories


def write_coverage(reports: list[dict], weaknesses: list[dict], teams: list[dict], new_ids: list[str]) -> None:
    teams = select_directory_teams(teams)
    programs_with = {r.get("program") for r in reports if r.get("program")}
    vulns_with = {r.get("vuln_type") for r in reports if r.get("vuln_type")}
    catalog_weak = sorted({w.get("name") for w in weaknesses if w.get("name")}, key=str.lower)
    catalog_prog = sorted({t.get("name") for t in teams if t.get("name")}, key=str.lower)
    missing_weak = [n for n in catalog_weak if n not in vulns_with]
    missing_prog = [n for n in catalog_prog if n not in programs_with]
    extra_weak = sorted(vulns_with - set(catalog_weak), key=str.lower)
    extra_prog = sorted(programs_with - set(catalog_prog), key=str.lower)
    payload = {
        "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "disclosed_reports": len(reports),
        "new_reports_this_run": len(new_ids),
        "programs_with_reports": len(programs_with),
        "directory_programs": len(catalog_prog),
        "weaknesses_with_reports": len(vulns_with),
        "catalog_weaknesses": len(catalog_weak),
        "programs_without_disclosed_reports": missing_prog,
        "weaknesses_without_disclosed_reports": missing_weak,
        "programs_not_in_directory": extra_prog,
        "weaknesses_not_in_catalog": extra_weak,
    }
    CACHE.mkdir(parents=True, exist_ok=True)
    (CACHE / "coverage.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "# Corpus coverage",
        "",
        f"- Updated (UTC): `{payload['updated_at']}`",
        f"- Disclosed reports: **{payload['disclosed_reports']}**",
        f"- New reports this run: **{payload['new_reports_this_run']}**",
        f"- Programs with reports: **{payload['programs_with_reports']}** / {payload['directory_programs']} directory programs",
        f"- Weaknesses with reports: **{payload['weaknesses_with_reports']}** / {payload['catalog_weaknesses']} catalog weaknesses",
        "",
        "Every directory program and every catalog weakness has an index page.",
        "Pages with zero public disclosures say so explicitly.",
        "",
        f"## Directory programs with no disclosed reports ({len(missing_prog)})",
        "",
    ]
    lines.extend(f"- {name}" for name in missing_prog[:500])
    if len(missing_prog) > 500:
        lines.append(f"- … {len(missing_prog) - 500} more")
    lines.extend(["", f"## Catalog weaknesses with no disclosed reports ({len(missing_weak)})", ""])
    lines.extend(f"- {name}" for name in missing_weak)
    (ROOT / "docs" / "COVERAGE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_readme(reports: list[dict], categories: dict) -> None:
    lines = [
        "**Live site:** [reddelexc.github.io/hackerone-reports](https://reddelexc.github.io/hackerone-reports)",
        "",
        "Tops of HackerOne reports. All reports' raw info stored in `data.csv`.",
        "Refresh with `python3 refresh_all.py` (GraphQL + public report JSON).",
        "Legacy scripts remain: `fetcher.py` → `uniquer.py` → `filler.py` → `rater.py`.",
        "",
        f"Corpus size: **{len(reports)}** disclosed reports, "
        f"**{len(categories['tops_by_program'])}** programs, "
        f"**{len(categories['tops_by_weakness'])}** weakness types.",
        "",
        "Tops 100.",
        "",
    ]
    for item in categories["tops_100"]:
        lines.append(f"- [{item['name']}](docs/{item['file']})")
    lines.extend(["", "Tops by common bug class (title keywords).", ""])
    for item in categories["tops_by_bug_type"]:
        lines.append(f"- [Top {item['name']} reports](docs/{item['file']})")
    lines.extend(["", "Tops by HackerOne weakness (every catalog type).", ""])
    for item in categories["tops_by_weakness"]:
        count = item.get("count", 0)
        lines.append(f"- [{item['name']}](docs/{item['file']}) ({count})")
    lines.extend(["", "Tops by program (every directory program).", ""])
    for item in categories["tops_by_program"]:
        count = item.get("count", 0)
        lines.append(f"- [{item['name']}](docs/{item['file']}) ({count})")
    lines.extend(["", "Coverage: [docs/COVERAGE.md](docs/COVERAGE.md)", ""])
    (ROOT / "README.md").write_text("\n".join(lines), encoding="utf-8")


def build_codebygk(reports: list[dict], weaknesses: list[dict], teams: list[dict]) -> None:
    teams = select_directory_teams(teams)
    CODEBYGK.mkdir(parents=True, exist_ok=True)
    results = CODEBYGK / "results"
    data_dir = CODEBYGK / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    payload = []
    for report in reports:
        payload.append({
            "title": report.get("title") or "",
            "url": report.get("url") or f"https://{report.get('link')}",
            "program": report.get("program") or "",
            "asset_type": report.get("asset_type") or "",
            "bounty": float(report.get("bounty") or 0),
            "vulnerability_type": report.get("vuln_type") or "",
            "severity": report.get("severity") or "",
            "state": report.get("state") or "",
            "upvotes": int(report.get("upvotes") or 0),
            "submitted_at": report.get("submitted_at") or "",
            "disclosed_at": report.get("disclosed_at") or "",
        })
    (data_dir / "reports.json").write_text(
        json.dumps({"reports": payload}, ensure_ascii=False),
        encoding="utf-8",
    )

    def parse_dt(value: str):
        if not value:
            return None
        for fmt in ("%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%SZ"):
            try:
                return datetime.strptime(value, fmt)
            except ValueError:
                continue
        return None

    now = datetime.now(timezone.utc).replace(tzinfo=None)
    recent = []
    for report in reports:
        disclosed = parse_dt(report.get("disclosed_at") or "")
        if disclosed and (now - disclosed).days < 90:
            recent.append(report)
    recent.sort(key=lambda r: r.get("disclosed_at") or "", reverse=True)
    write_table(
        results / "recent" / "recently_disclosed.md",
        "## Reports disclosed in the last 90 days:",
        recent,
        "| S.No | Title | Bounty |",
    )

    write_table(
        results / "top" / "top_upvotes.md",
        "## Top 100 reports with highest upvotes:",
        ranked(reports)[:100],
        "| S.No | Title | Bounty | Upvotes |",
    )
    write_table(
        results / "top" / "top_bounties.md",
        "## Top 100 reports with highest bounty:",
        bounty_ranked(reports)[:100],
        "| S.No | Title | Bounty |",
    )

    by_vuln = defaultdict(list)
    for report in reports:
        if report.get("vuln_type"):
            by_vuln[report["vuln_type"]].append(report)
    vuln_names = []
    seen = set()
    for item in weaknesses:
        name = (item.get("name") or "").strip()
        if name and name not in seen:
            seen.add(name)
            vuln_names.append(name)
    for name in sorted(by_vuln, key=str.lower):
        if name not in seen:
            vuln_names.append(name)
            seen.add(name)
    vuln_slugs: dict[str, str] = {}
    wanted = set()
    readme = [
        "",
        "## Recent reports:",
        "| S.No | Title |",
        "| ---- | ----- |",
        "| 1 | [Recently disclosed](results/recent/recently_disclosed.md) |",
        "",
        "## Top reports:",
        "| S.No | Title |",
        "| ---- | ----- |",
        "| 1 | [Top upvotes](results/top/top_upvotes.md) |",
        "| 2 | [Top bounties](results/top/top_bounties.md) |",
        "",
        "## Reports based on vulnerability:",
        "| S.No | Title |",
        "| ---- | ----- |",
    ]
    out_dir = results / "based_on_vulnerability_type"
    out_dir.mkdir(parents=True, exist_ok=True)
    for i, name in enumerate(vuln_names, 1):
        slug = unique_slug(codebygk_slug(name), vuln_slugs, name)
        rel = Path("results") / "based_on_vulnerability_type" / f"{slug}.md"
        write_table(
            CODEBYGK / rel,
            f"## Reports in {name} category:",
            bounty_ranked(by_vuln.get(name, [])),
            "| S.No | Title | Bounty |",
        )
        readme.append(f"| {i} | [{name}]({rel.as_posix()}) |")
        wanted.add(f"{slug}.md")
    for stale in out_dir.glob("*.md"):
        if stale.name not in wanted:
            stale.unlink()

    by_sev = defaultdict(list)
    for report in reports:
        if report.get("severity"):
            by_sev[report["severity"]].append(report)
    readme.extend(["", "## Reports based on severity:", "| S.No | Title |", "| ---- | ----- |"])
    sev_dir = results / "based_on_severity"
    sev_dir.mkdir(parents=True, exist_ok=True)
    wanted = set()
    for i, name in enumerate(sorted(by_sev, key=str.lower), 1):
        slug = codebygk_slug(name)
        rel = Path("results") / "based_on_severity" / f"{slug}.md"
        write_table(CODEBYGK / rel, f"## Reports in {name} severity:", bounty_ranked(by_sev[name]), "| S.No | Title | Bounty |")
        readme.append(f"| {i} | [{name}]({rel.as_posix()}) |")
        wanted.add(f"{slug}.md")
    for stale in sev_dir.glob("*.md"):
        if stale.name not in wanted:
            stale.unlink()

    by_asset = defaultdict(list)
    for report in reports:
        if report.get("asset_type"):
            by_asset[report["asset_type"]].append(report)
    readme.extend(["", "## Reports based on asset type:", "| S.No | Title |", "| ---- | ----- |"])
    asset_dir = results / "based_on_asset_type"
    asset_dir.mkdir(parents=True, exist_ok=True)
    wanted = set()
    for i, name in enumerate(sorted(by_asset, key=str.lower), 1):
        slug = codebygk_slug(name)
        rel = Path("results") / "based_on_asset_type" / f"{slug}.md"
        write_table(CODEBYGK / rel, f"## Reports in {name} asset type:", bounty_ranked(by_asset[name]), "| S.No | Title | Bounty |")
        readme.append(f"| {i} | [{name}]({rel.as_posix()}) |")
        wanted.add(f"{slug}.md")
    for stale in asset_dir.glob("*.md"):
        if stale.name not in wanted:
            stale.unlink()

    by_prog = defaultdict(list)
    for report in reports:
        if report.get("program"):
            by_prog[report["program"]].append(report)
    program_names = []
    seen = set()
    for team in teams:
        name = (team.get("name") or "").strip()
        if name and name not in seen:
            seen.add(name)
            program_names.append(name)
    for name in sorted(by_prog, key=str.lower):
        if name not in seen:
            program_names.append(name)
            seen.add(name)
    program_names.sort(key=lambda n: (0 if by_prog.get(n) else 1, n.lower()))
    readme.extend(["", "## Reports based on program:", "| S.No | Title |", "| ---- | ----- |"])
    prog_dir = results / "based_on_program"
    prog_dir.mkdir(parents=True, exist_ok=True)
    prog_slugs: dict[str, str] = {}
    wanted = set()
    for i, name in enumerate(program_names, 1):
        slug = unique_slug(codebygk_slug(name), prog_slugs, name)
        rel = Path("results") / "based_on_program" / f"{slug}.md"
        write_table(
            CODEBYGK / rel,
            f"## Reports in {name} program:",
            bounty_ranked(by_prog.get(name, [])),
            "| S.No | Title | Bounty |",
        )
        readme.append(f"| {i} | [{name}]({rel.as_posix()}) |")
        wanted.add(f"{slug}.md")
    for stale in prog_dir.glob("*.md"):
        if stale.name not in wanted:
            stale.unlink()
    (CODEBYGK / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")
    log(f"Wrote codebygk corpus to {CODEBYGK}")


def update_script_js() -> None:
    path = ROOT / "docs" / "script.js"
    text = path.read_text(encoding="utf-8")
    old = """    const sections = [
      { key: 'tops_100', title: 'Top 100' },
      { key: 'tops_by_bug_type', title: 'By Bug Type' },
      { key: 'tops_by_program', title: 'By Program' },
    ];"""
    new = """    const sections = [
      { key: 'tops_100', title: 'Top 100' },
      { key: 'tops_by_bug_type', title: 'By Bug Type' },
      { key: 'tops_by_weakness', title: 'By Weakness' },
      { key: 'tops_by_program', title: 'By Program' },
    ];"""
    if old in text:
        path.write_text(text.replace(old, new), encoding="utf-8")


def index_only(reports: list[dict], weaknesses: list[dict], teams: list[dict], new_ids: list[str]) -> None:
    categories = build_reddelexc_indexes(reports, weaknesses, teams)
    write_coverage(reports, weaknesses, teams, new_ids)
    write_readme(reports, categories)
    update_script_js()
    build_codebygk(reports, weaknesses, teams)
    log(
        f"Indexed {len(reports)} reports, "
        f"{len(categories['tops_by_program'])} programs, "
        f"{len(categories['tops_by_weakness'])} weaknesses"
    )


def collect_program_handles(teams: list[dict], reports: list[dict]) -> list[dict]:
    """Public directory handles plus any handle already seen in the corpus."""
    selected: dict[str, dict] = {}
    for team in teams:
        handle = (team.get("handle") or "").strip()
        name = (team.get("name") or "").strip()
        if not handle:
            continue
        if team.get("state") in PUBLIC_TEAM_STATES:
            selected[handle] = {"handle": handle, "name": name, "state": team.get("state") or ""}
    by_name = {(t.get("name") or "").strip().lower(): t for t in teams if t.get("handle")}
    for report in reports:
        handle = (report.get("handle") or "").strip()
        name = (report.get("program") or "").strip()
        if handle and handle not in selected:
            selected[handle] = {"handle": handle, "name": name, "state": "corpus"}
        if name and name.lower() in by_name:
            team = by_name[name.lower()]
            handle = (team.get("handle") or "").strip()
            if handle and handle not in selected:
                selected[handle] = {
                    "handle": handle,
                    "name": team.get("name") or name,
                    "state": team.get("state") or "matched",
                }
    return sorted(selected.values(), key=lambda item: item["handle"])


def fetch_reports_for_handle(s: requests.Session, handle: str) -> list[dict]:
    where = {"disclosed_at": {"_is_null": False}, "team": {"handle": {"_eq": handle}}}
    nodes = paginate(s, REPORTS_QUERY, "reports", {"where": where}, quiet=True)
    if len(nodes) >= WINDOW_SPLIT_AT:
        log(f"  {handle} hit {len(nodes)}; splitting by year")
        merged: dict[str, dict] = {}
        now = datetime.now(timezone.utc)
        for year in range(2013, now.year + 1):
            year_where = {
                "disclosed_at": {
                    "_gte": f"{year}-01-01T00:00:00.000Z",
                    "_lt": f"{year + 1}-01-01T00:00:00.000Z",
                },
                "team": {"handle": {"_eq": handle}},
            }
            year_nodes = paginate(s, REPORTS_QUERY, "reports", {"where": year_where}, quiet=True)
            for node in year_nodes:
                report = node_to_report(node)
                if report["id"]:
                    merged[report["id"]] = report
        return list(merged.values())
    return [node_to_report(node) for node in nodes if node.get("_id")]


def fetch_all_by_program(
    s: requests.Session,
    teams: list[dict],
    reports: list[dict],
    resume: bool = False,
) -> tuple[list[dict], list[dict]]:
    handles = collect_program_handles(teams, reports)
    log(f"Fetching disclosed hacktivity for {len(handles)} program handles")
    prog_dir = CACHE / "programs"
    prog_dir.mkdir(parents=True, exist_ok=True)
    merged: dict[str, dict] = {}
    audit = []
    for i, item in enumerate(handles, 1):
        handle = item["handle"]
        cache_path = prog_dir / f"{handle}.json"
        if resume and cache_path.exists():
            fetched = json.loads(cache_path.read_text(encoding="utf-8"))
            log(f"[{i}/{len(handles)}] resume {handle}: {len(fetched)}")
        else:
            fetched = fetch_reports_for_handle(s, handle)
            cache_path.write_text(json.dumps(fetched, ensure_ascii=False), encoding="utf-8")
            log(f"[{i}/{len(handles)}] {handle}: {len(fetched)} disclosed")
            time.sleep(GRAPHQL_SLEEP)
        for report in fetched:
            merged[report["id"]] = report
        corpus_for_handle = sum(1 for report in reports if report.get("handle") == handle)
        if not corpus_for_handle:
            corpus_for_handle = sum(
                1 for report in reports
                if (report.get("program") or "").strip() == (item.get("name") or "").strip()
            )
        audit.append({
            "handle": handle,
            "name": item.get("name") or "",
            "state": item.get("state") or "",
            "live_disclosed": len(fetched),
            "corpus_before": corpus_for_handle,
            "delta": len(fetched) - corpus_for_handle,
        })
    log(f"Per-program disclosed reports: {len(merged)}")
    return list(merged.values()), audit


def write_hacktivity_audit(audit: list[dict], new_ids: list[str]) -> None:
    missing = [row for row in audit if row["delta"] > 0]
    extra = [row for row in audit if row["delta"] < 0]
    zero = [row for row in audit if row["live_disclosed"] == 0]
    lines = [
        "# Per-program disclosed hacktivity audit",
        "",
        "Live source: HackerOne GraphQL `reports` filtered by `team.handle` and `disclosed_at`.",
        "Private/undisclosed reports are not public and are not in this corpus.",
        "",
        f"- Programs checked: **{len(audit)}**",
        f"- Programs with live disclosed reports: **{sum(1 for row in audit if row['live_disclosed'] > 0)}**",
        f"- Programs whose live hacktivity added reports: **{len(missing)}**",
        f"- New report IDs this pass: **{len(new_ids)}**",
        f"- Programs with zero public disclosed reports: **{len(zero)}**",
        f"- Programs where corpus still has historical rows live no longer returns: **{len(extra)}**",
        "",
        "## Programs where live hacktivity had more reports than the corpus",
        "",
        "| Handle | Program | Live | Corpus before | Delta |",
        "| --- | --- | ---: | ---: | ---: |",
    ]
    for row in sorted(missing, key=lambda item: item["delta"], reverse=True):
        lines.append(
            f"| {row['handle']} | {row['name']} | {row['live_disclosed']} | {row['corpus_before']} | {row['delta']} |"
        )
    if not missing:
        lines.append("|  | none |  |  |  |")
    lines.extend([
        "",
        "## All checked programs",
        "",
        "| Handle | Program | Live disclosed | Corpus before | Delta |",
        "| --- | --- | ---: | ---: | ---: |",
    ])
    for row in audit:
        lines.append(
            f"| {row['handle']} | {row['name']} | {row['live_disclosed']} | {row['corpus_before']} | {row['delta']} |"
        )
    (ROOT / "docs" / "HACKTIVITY_AUDIT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (CACHE / "hacktivity_audit.json").write_text(
        json.dumps(audit, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Refresh HackerOne disclosed-report corpora")
    parser.add_argument("--index-only", action="store_true", help="Rebuild indexes from existing CSV/cache")
    parser.add_argument("--skip-json", action="store_true", help="Do not fetch per-report JSON for upvotes")
    parser.add_argument("--resume", action="store_true", help="Reuse cached completed year windows")
    parser.add_argument(
        "--by-program",
        action="store_true",
        help="Fetch disclosed reports from each program handle (hacktivity-equivalent)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    CACHE.mkdir(parents=True, exist_ok=True)
    existing_rows = load_csv(CSV_PATH)

    if args.index_only:
        if FULL_JSON.exists():
            reports = json.loads(FULL_JSON.read_text(encoding="utf-8"))
            new_ids = []
        else:
            graphql_reports = []
            if (CACHE / "reports_graphql.json").exists():
                graphql_reports = json.loads((CACHE / "reports_graphql.json").read_text(encoding="utf-8"))
            reports, new_ids = merge_reports(existing_rows, graphql_reports)
        reports = sort_reports(reports)
        weaknesses = json.loads(WEAKNESS_CACHE.read_text(encoding="utf-8")) if WEAKNESS_CACHE.exists() else []
        teams = json.loads(TEAM_CACHE.read_text(encoding="utf-8")) if TEAM_CACHE.exists() else []
        index_only(reports, weaknesses, teams, new_ids)
        return 0

    s = session()
    if WEAKNESS_CACHE.exists() and TEAM_CACHE.exists() and args.by_program:
        weaknesses = json.loads(WEAKNESS_CACHE.read_text(encoding="utf-8"))
        teams = json.loads(TEAM_CACHE.read_text(encoding="utf-8"))
        log(f"Using cached catalogs: {len(weaknesses)} weaknesses, {len(teams)} teams")
    else:
        weaknesses = fetch_catalog(s, WEAKNESSES_QUERY, "weaknesses", WEAKNESS_CACHE)
        teams = fetch_catalog(s, TEAMS_QUERY, "teams", TEAM_CACHE)
    if FULL_JSON.exists():
        current_reports = json.loads(FULL_JSON.read_text(encoding="utf-8"))
    else:
        current_reports, _ = merge_reports(existing_rows, [])
    if args.by_program:
        fetched, audit = fetch_all_by_program(s, teams, current_reports, resume=args.resume)
    else:
        fetched = fetch_all_reports(s, resume=args.resume)
        audit = []
    existing_for_merge = [
        {
            "program": r.get("program") or "",
            "title": r.get("title") or "",
            "link": r.get("link") or f"hackerone.com/reports/{r.get('id')}",
            "upvotes": r.get("upvotes") or 0,
            "bounty": r.get("bounty") or 0,
            "vuln_type": r.get("vuln_type") or "",
        }
        for r in current_reports
    ]
    reports, new_ids = merge_reports(existing_for_merge, fetched)
    extra = {r["id"]: r for r in current_reports if r.get("id")}
    for report in reports:
        old = extra.get(report["id"])
        if not old:
            continue
        for key in ("handle", "url", "external_id", "severity", "state", "asset_type", "submitted_at", "disclosed_at", "cve_ids"):
            if not report.get(key):
                report[key] = old.get(key) or report.get(key)
        if not report.get("upvotes"):
            report["upvotes"] = old.get("upvotes") or 0
    log(f"Merged corpus {len(reports)} (new {len(new_ids)})")
    if not args.skip_json:
        fill_new_reports(reports, new_ids)
    reports = sort_reports(reports)
    write_csv(reports, CSV_PATH)
    FULL_JSON.write_text(json.dumps(reports, ensure_ascii=False), encoding="utf-8")
    if audit:
        write_hacktivity_audit(audit, new_ids)
    index_only(reports, weaknesses, teams, new_ids)
    return 0


if __name__ == "__main__":
    sys.exit(main())
