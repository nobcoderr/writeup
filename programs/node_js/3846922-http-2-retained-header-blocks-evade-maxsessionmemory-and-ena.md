# HTTP/2 retained header blocks evade maxSessionMemory and enable remote memory exhaustion

- Program: Node.js
- Weakness / temuan: **Uncontrolled Resource Consumption**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 12
- Submitted: 2026-07-06
- Disclosed: 2026-08-28
- Report: https://hackerone.com/reports/3846922
- CVE: CVE-2026-56846

## Team summary

A flaw in Node.js HTTP/2 handling can cause HTTP/2 retained header blocks evade maxSessionMemory and enable remote memory exhaustion.

This vulnerability affects Node.js **24.x** and **22.x**.
