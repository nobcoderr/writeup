# Unbounded memory growth in `node:http2` clients via attacker-controlled ORIGIN frames

- Program: Node.js
- Weakness / temuan: **Uncontrolled Resource Consumption**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 4
- Submitted: 2026-04-16
- Disclosed: 2026-06-25
- Report: https://hackerone.com/reports/3676863
- CVE: CVE-2026-48619

## Team summary

A flaw in Node.js HTTP/2 client allows a server to send an unlimited number of ORIGIN frames, which could lead to an Out of Memory error on the client.

This vulnerability affects all supported release lines: **Node.js 22**, **Node.js 24**, and **Node.js 26**.
