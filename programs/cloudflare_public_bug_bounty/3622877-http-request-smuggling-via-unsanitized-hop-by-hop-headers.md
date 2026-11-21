# HTTP Request Smuggling via Unsanitized Hop-by-Hop Headers

- Program: Cloudflare Public Bug Bounty
- Weakness / temuan: **Improper Access Control - Generic**
- Severity: high
- State: resolved
- Bounty: $1500.00
- Upvotes: 54
- Submitted: 2026-03-23
- Disclosed: 2026-09-14
- Report: https://hackerone.com/reports/3622877

## Team summary

Note: the content of the report diverged during the triage process. A more fitting title would be Request Inspection Bypass via Unintended h2c Upgrade Tunneling; there was no request smuggling desync enabled.

Pingora could forward h2c upgrade requests in HTTP/1 to upstream servers, allowing subsequent h2c requests over the upgraded connection to bypass request-level filters applied by the proxy. Pingora 0.9.0 restricts HTTP/1 upgrades to WebSocket by default, addressing this issue. Users with h2c-compatible upstreams should upgrade to that version or later. We thank the researcher for responsibly reporting the issue and verifying the fix.
