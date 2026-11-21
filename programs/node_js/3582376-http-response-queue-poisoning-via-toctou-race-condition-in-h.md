# HTTP Response Queue Poisoning via TOCTOU Race Condition in `http.Agent`

- Program: Node.js
- Weakness / temuan: **Time-of-check Time-of-use (TOCTOU) Race Condition**
- Severity: low
- State: resolved
- Bounty: $0.00
- Upvotes: 11
- Submitted: 2026-03-03
- Disclosed: 2026-06-25
- Report: https://hackerone.com/reports/3582376
- CVE: CVE-2026-48931

## Team summary

A flaw in Node.js HTTP Agent can cause a client to accept as valid a response that is send before the client has sent the request.

This vulnerability affects all supported release lines: **Node.js 22**, **Node.js 24**, and **Node.js 26**.
