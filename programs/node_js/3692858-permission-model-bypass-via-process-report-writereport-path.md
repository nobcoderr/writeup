# Permission Model Bypass via `process.report.writeReport()` Path Misvalidation

- Program: Node.js
- Weakness / temuan: **Improper Access Control - Generic**
- Severity: low
- State: resolved
- Bounty: $0.00
- Upvotes: 29
- Submitted: 2026-04-24
- Disclosed: 2026-06-18
- Report: https://hackerone.com/reports/3692858
- CVE: CVE-2026-48617

## Team summary

A flaw in Node.js Permission Model enforcement allows Bypass via `process.report.writeReport()` Path Misvalidation.

This can lead to confidentiality impact or bypass of the intended security boundary under affected configurations.

This vulnerability affects all supported release lines: **Node.js 22**, **Node.js 24**, and **Node.js 26**.
