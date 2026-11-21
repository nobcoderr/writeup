# Permission Model bypass with fs.realpathSync

- Program: Node.js
- Weakness / temuan: **Improper Access Control - Generic**
- Severity: low
- State: resolved
- Bounty: $0.00
- Upvotes: 15
- Submitted: 2026-07-02
- Disclosed: 2026-10-23
- Report: https://hackerone.com/reports/3838675
- CVE: CVE-2026-106073

## Team summary

A flaw in Node.js Permission Model filesystem enforcement leaves `fs.realpathSync()` without the required read permission checks. This is an incomplete fix of CVE-2026-21715, which only covered `fs.realpathSync.native()`.

As a result, code running under `--permission` with restricted `--allow-fs-read` can still use `fs.realpathSync()` to check file existence, resolve symlink targets, and enumerate filesystem paths outside of permitted directories.
