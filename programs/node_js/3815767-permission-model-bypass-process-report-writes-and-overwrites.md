# Permission Model bypass: process.report writes (and overwrites) files outside --allow-fs-write paths

- Program: Node.js
- Weakness / temuan: **Improper Access Control - Generic**
- Severity: low
- State: resolved
- Bounty: $0.00
- Upvotes: 35
- Submitted: 2026-06-21
- Disclosed: 2026-07-30
- Report: https://hackerone.com/reports/3815767
- CVE: CVE-2026-58039

## Team summary

A flaw in Node.js Permission Model enforcement allows process.report writes (and overwrites) files outside --allow-fs-write paths.

This can lead to confidentiality impact or bypass of the intended security boundary under affected configurations.

This vulnerability affects Node.js **22.x**, **24.x**, and **26.x**.
