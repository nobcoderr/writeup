# Node.js WebCrypto AES Integer Overflow Leads to Remote Process Abort (DoS)

- Program: Node.js
- Weakness / temuan: **Integer Overflow**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 13
- Submitted: 2026-05-25
- Disclosed: 2026-06-25
- Report: https://hackerone.com/reports/3760016
- CVE: CVE-2026-48933

## Team summary

A flaw in Node.js WebCrypto implementation can crash the process if the input of `subtle.encrypt()` is a multiple of 2GiB.

This vulnerability affects all supported release lines: **Node.js 22**, **Node.js 24**, and **Node.js 26**.
