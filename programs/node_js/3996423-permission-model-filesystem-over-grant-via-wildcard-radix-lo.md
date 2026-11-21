# Permission Model filesystem over-grant via wildcard radix lookup

- Program: Node.js
- Weakness / temuan: **Improper Access Control - Generic**
- Severity: low
- State: resolved
- Bounty: $0.00
- Upvotes: 6
- Submitted: 2026-09-04
- Disclosed: 2026-10-27
- Report: https://hackerone.com/reports/3996423
- CVE: CVE-2026-106071

## Team summary

A flaw in Node.js Permission Model filesystem enforcement can grant access to paths that do not match a wildcard `--allow-fs-read` or `--allow-fs-write` rule.

When the requested path is shorter than the prefix of a wildcard grant, the radix tree lookup stops comparing early and treats the path as a match. For example, `--allow-fs-read=/etc/passwd.*` also allows reading `/etc/passwd`. This requires the wildcard grant to sit directly under the root of the permission tree, for example when it is the only grant for that scope. This is a different root cause from CVE-2026-58043.

This vulnerability affects Node.js **26.x**.
