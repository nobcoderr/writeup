# TLS host identity verification bypass via session reuse with different servername leads to unauthorized connections

- Program: Node.js
- Weakness / temuan: **Exploiting Incorrectly Configured SSL/TLS**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 5
- Submitted: 2026-04-04
- Disclosed: 2026-06-25
- Report: https://hackerone.com/reports/3649802
- CVE: CVE-2026-48934

## Team summary

A flaw in Node.js TLS host verification can cause an attacker to bypass certification validation.

This vulnerability affects all supported release lines: **Node.js 22**, **Node.js 24**, and **Node.js 26**.
