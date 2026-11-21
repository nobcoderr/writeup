# Embedded-nul hostnames can lead to silent authority rebinding due to c-string truncation in resolver bindings

- Program: Node.js
- Weakness / temuan: **Improper Access Control - Generic**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 4
- Submitted: 2026-04-07
- Disclosed: 2026-06-25
- Report: https://hackerone.com/reports/3656716
- CVE: CVE-2026-48930

## Team summary

A flaw in Node.js TLS hostname handling can cause Embedded-nul hostnames can lead to silent authority rebinding due to c-string truncation in resolver bindings.

This vulnerability affects all supported release lines: **Node.js 22**, **Node.js 24**, and **Node.js 26**.
