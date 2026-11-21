# Permission Model bypass via FileHandle.utimes() in the promises API

- Program: Node.js
- Weakness / temuan: **Incorrect Default Permissions**
- Severity: low
- State: resolved
- Bounty: $0.00
- Upvotes: 4
- Submitted: 2026-03-24
- Disclosed: 2026-06-25
- Report: https://hackerone.com/reports/3625987
- CVE: CVE-2026-48935

## Team summary

A flaw in Node.js Permission API can cause a file metadata to be modified even on a path that was set as read-only with e.g. `--allow-fs-read`.

This vulnerability affects all supported release lines: **Node.js 22**, **Node.js 24**, and **Node.js 26**.
