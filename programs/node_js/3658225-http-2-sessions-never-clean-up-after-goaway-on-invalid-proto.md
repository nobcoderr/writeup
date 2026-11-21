# HTTP/2 sessions never clean up after GOAWAY on invalid protocol errors

- Program: Node.js
- Weakness / temuan: **Uncontrolled Resource Consumption**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 33
- Submitted: 2026-04-08
- Disclosed: 2026-06-18
- Report: https://hackerone.com/reports/3658225
- CVE: CVE-2026-48937

## Team summary

A flaw in Node.js HTTP/2 server API can cause servers to keep accepting data even after sending a `GOAWAY` frame.

This vulnerability affects two supported release lines: **Node.js 22** and **Node.js 24**.
