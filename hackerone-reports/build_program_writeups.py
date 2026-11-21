#!/usr/bin/env python3
"""Build programs/<program>/ folders with one writeup file per disclosed report."""

from __future__ import annotations

import argparse
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
REPO = ROOT.parent
PROGRAMS = REPO / "programs"
CACHE = ROOT / "cache"
FULL_JSON = CACHE / "reports_full.json"
TEAM_CACHE = CACHE / "teams.json"
WRITEUP_CACHE = CACHE / "writeups"
PUBLIC_TEAM_STATES = {"public_mode", "soft_launched"}
REPORT_JSON = "https://hackerone.com/reports/{rid}.json"
JSON_WORKERS = 8
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)
BODY_LIMIT = 200_000


def log(msg: str) -> None:
    print(msg, flush=True)


def session() -> requests.Session:
    s = requests.Session()
    s.headers.update({
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
    })
    return s


def folder_slug(name: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9\s\-()]+", " ", name or "unknown")
    text = re.sub(r"[^a-zA-Z0-9]", " ", text).lower()
    text = re.sub(r"\s+", " ", text).strip().replace(" ", "_")
    return text or "unknown"


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


def title_slug(title: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", (title or "").lower()).strip("-")
    return (text[:60] or "report").strip("-")


def day(value: str) -> str:
    if not value:
        return ""
    return value[:10]


def select_directory_teams(teams: list[dict]) -> list[dict]:
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
            payload = r.json()
            summaries = []
            for item in payload.get("summaries") or []:
                summaries.append({
                    "category": item.get("category") or "",
                    "content": item.get("content") or "",
                })
            return {
                "id": str(rid),
                "vulnerability_information": payload.get("vulnerability_information") or "",
                "summaries": summaries,
            }
        except (requests.RequestException, ValueError):
            time.sleep(delay)
            delay = min(delay * 2, 20)
    return None


def fill_writeups(report_ids: list[str]) -> None:
    WRITEUP_CACHE.mkdir(parents=True, exist_ok=True)
    missing = [rid for rid in report_ids if not (WRITEUP_CACHE / f"{rid}.json").exists()]
    if not missing:
        log("Writeup cache already complete")
        return
    log(f"Fetching public writeup JSON for {len(missing)} reports")
    s = session()

    def work(rid: str):
        return rid, fetch_report_json(s, rid)

    done = 0
    with ThreadPoolExecutor(max_workers=JSON_WORKERS) as pool:
        futures = [pool.submit(work, rid) for rid in missing]
        for fut in as_completed(futures):
            rid, payload = fut.result()
            done += 1
            if payload:
                (WRITEUP_CACHE / f"{rid}.json").write_text(
                    json.dumps(payload, ensure_ascii=False),
                    encoding="utf-8",
                )
            if done % 50 == 0 or done == len(missing):
                log(f"  writeup JSON {done}/{len(missing)}")


def load_writeup(rid: str) -> dict:
    path = WRITEUP_CACHE / f"{rid}.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def clip(text: str) -> str:
    text = (text or "").strip()
    if len(text) > BODY_LIMIT:
        return text[:BODY_LIMIT] + "\n\n… truncated …\n"
    return text


def report_markdown(report: dict, writeup: dict) -> str:
    title = report.get("title") or "(untitled)"
    weakness = (report.get("vuln_type") or "").strip() or title
    lines = [
        f"# {title}",
        "",
        f"- Program: {report.get('program') or 'Unknown'}",
        f"- Weakness / temuan: **{weakness}**",
        f"- Severity: {report.get('severity') or 'n/a'}",
        f"- State: {report.get('state') or 'n/a'}",
        f"- Bounty: ${float(report.get('bounty') or 0):.2f}",
        f"- Upvotes: {int(report.get('upvotes') or 0)}",
        f"- Submitted: {day(report.get('submitted_at') or '') or 'n/a'}",
        f"- Disclosed: {day(report.get('disclosed_at') or '') or 'n/a'}",
        f"- Report: {report.get('url') or ('https://hackerone.com/reports/' + str(report.get('id') or ''))}",
    ]
    cves = report.get("cve_ids") or []
    if cves:
        lines.append(f"- CVE: {', '.join(cves)}")
    if report.get("asset_type"):
        lines.append(f"- Asset type: {report.get('asset_type')}")
    lines.append("")

    summaries = writeup.get("summaries") or []
    for item in summaries:
        content = clip(item.get("content") or "")
        if not content:
            continue
        category = item.get("category") or "summary"
        heading = "Team summary" if category == "team" else "Researcher summary" if category == "researcher" else category.title()
        lines.extend([f"## {heading}", "", content, ""])

    body = clip(writeup.get("vulnerability_information") or "")
    if body:
        lines.extend(["## Writeup", "", body, ""])

    if not any(line.startswith("## ") for line in lines):
        lines.extend([
            "## Temuan",
            "",
            weakness,
            "",
            "Public writeup body was not in the disclosed JSON; open the report link above.",
            "",
        ])
    return "\n".join(lines).rstrip() + "\n"


def program_readme(name: str, reports: list[dict]) -> str:
    lines = [
        f"# {name}",
        "",
        f"Disclosed reports: **{len(reports)}**",
        "",
    ]
    if not reports:
        lines.extend([
            "No public disclosed writeups for this program.",
            "",
        ])
        return "\n".join(lines)
    lines.extend([
        "| ID | Temuan | Severity | Bounty | Writeup |",
        "| --- | --- | --- | ---: | --- |",
    ])
    ranked = sorted(
        reports,
        key=lambda r: (float(r.get("bounty") or 0), int(r.get("upvotes") or 0)),
        reverse=True,
    )
    slugs_used: dict[str, str] = {}
    for report in ranked:
        rid = str(report.get("id") or "")
        fname = unique_slug(f"{rid}-{title_slug(report.get('title') or '')}", slugs_used, rid) + ".md"
        weakness = (report.get("vuln_type") or "").strip() or (report.get("title") or "(untitled)")
        title = (report.get("title") or "(untitled)").replace("|", "\\|")
        lines.append(
            f"| {rid} | {weakness} | {report.get('severity') or 'n/a'} | "
            f"${float(report.get('bounty') or 0):.0f} | [{title}]({fname}) |"
        )
    lines.append("")
    return "\n".join(lines)


def generate(reports: list[dict], teams: list[dict]) -> None:
    reports_by_program: dict[str, list[dict]] = defaultdict(list)
    for report in reports:
        name = (report.get("program") or "").strip()
        if name:
            reports_by_program[name].append(report)

    program_names = []
    seen = set()
    for team in select_directory_teams(teams):
        name = (team.get("name") or "").strip()
        if name and name not in seen:
            seen.add(name)
            program_names.append(name)
    for name in sorted(reports_by_program, key=str.lower):
        if name not in seen:
            program_names.append(name)
            seen.add(name)
    program_names.sort(key=lambda n: (0 if reports_by_program.get(n) else 1, n.lower()))

    if PROGRAMS.exists():
        for stale in PROGRAMS.glob("*"):
            if stale.is_dir() or stale.name == "README.md":
                continue
        # Recreate cleanly but keep directory.
        for child in PROGRAMS.iterdir():
            if child.is_file():
                child.unlink()
            elif child.is_dir():
                for nested in child.rglob("*"):
                    if nested.is_file():
                        nested.unlink()
                for nested in sorted(child.rglob("*"), reverse=True):
                    if nested.is_dir():
                        nested.rmdir()
                child.rmdir()
    PROGRAMS.mkdir(parents=True, exist_ok=True)

    slugs: dict[str, str] = {}
    index_lines = [
        "# Programs",
        "",
        "One folder per HackerOne program. Each disclosed report is a writeup file "
        "with the weakness/temuan, metadata, and public summary/writeup text.",
        "",
        f"Updated (UTC): `{datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}`",
        "",
        "| Program | Reports | Folder |",
        "| --- | ---: | --- |",
    ]
    for name in program_names:
        slug = unique_slug(folder_slug(name), slugs, name)
        folder = PROGRAMS / slug
        folder.mkdir(parents=True, exist_ok=True)
        program_reports = reports_by_program.get(name, [])
        (folder / "README.md").write_text(program_readme(name, program_reports), encoding="utf-8")
        file_slugs: dict[str, str] = {}
        for report in program_reports:
            rid = str(report.get("id") or "")
            if not rid:
                continue
            fname = unique_slug(f"{rid}-{title_slug(report.get('title') or '')}", file_slugs, rid) + ".md"
            writeup = load_writeup(rid)
            (folder / fname).write_text(report_markdown(report, writeup), encoding="utf-8")
        index_lines.append(f"| {name} | {len(program_reports)} | [{slug}]({slug}/) |")
        log(f"  {name}: {len(program_reports)} writeups -> programs/{slug}/")

    (PROGRAMS / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    log(f"Wrote {len(program_names)} program folders under {PROGRAMS}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build per-program writeup folders")
    parser.add_argument("--skip-fetch", action="store_true", help="Use cached writeup JSON only")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not FULL_JSON.exists():
        log(f"Missing {FULL_JSON}; run refresh_all.py first")
        return 1
    reports = json.loads(FULL_JSON.read_text(encoding="utf-8"))
    teams = json.loads(TEAM_CACHE.read_text(encoding="utf-8")) if TEAM_CACHE.exists() else []
    ids = [str(r.get("id")) for r in reports if r.get("id")]
    if not args.skip_fetch:
        fill_writeups(ids)
    generate(reports, teams)
    return 0


if __name__ == "__main__":
    sys.exit(main())
