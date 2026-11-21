# Proxy credentials leaked in ERR_PROXY_TUNNEL error message

- Program: Node.js
- Weakness / temuan: **Privacy Violation**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 4
- Submitted: 2026-05-08
- Disclosed: 2026-06-25
- Report: https://hackerone.com/reports/3720313
- CVE: CVE-2026-48615

## Team summary

A flaw in Node.js proxy tunnel error handling could expose proxy credentials in `ERR_PROXY_TUNNEL` error messages.

When proxy credentials are embedded in the proxy URL, they may be exposed through error handling paths and captured by logs, diagnostics, or other error consumers.

This vulnerability affects all supported release lines: **Node.js 22**, **Node.js 24**, and **Node.js 26**.
