# Unix domain socket server bypasses --permission network restrictions (incomplete CVE-2026-21636 fix)

- Program: Node.js
- Weakness / temuan: **Improper Access Control - Generic**
- Severity: low
- State: resolved
- Bounty: $0.00
- Upvotes: 8
- Submitted: 2026-03-20
- Disclosed: 2026-06-25
- Report: https://hackerone.com/reports/3618831
- CVE: CVE-2026-48936

## Team summary

A flaw in Node.js Permission API can cause a local server to be started (via a Unix domain socket), even without the `--allow-net` permission.

This vulnerability affects one supported release line: **Node.js 26**.
