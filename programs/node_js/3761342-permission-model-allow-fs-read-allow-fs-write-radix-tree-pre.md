# Permission Model: --allow-fs-read/--allow-fs-write radix-tree prefix-boundary over-grant

- Program: Node.js
- Weakness / temuan: **Improper Access Control - Generic**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 33
- Submitted: 2026-05-25
- Disclosed: 2026-07-29
- Report: https://hackerone.com/reports/3761342
- CVE: CVE-2026-58043

## Team summary

A flaw in Node.js Permission Model enforcement can over-grant filesystem access across radix-tree prefix boundaries.

Under `--permission`, an attacker who is granted access to one path can abuse boundary handling to read from or write to paths outside the intended filesystem allowlist.

This vulnerability affects Node.js **main**, **22.x**, **24.x**, and **26.x**.
