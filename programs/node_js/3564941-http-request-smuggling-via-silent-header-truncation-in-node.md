# HTTP Request Smuggling via Silent Header Truncation in Node.js HTTP Parser

- Program: Node.js
- Weakness / temuan: **HTTP Request Smuggling**
- Severity: low
- State: resolved
- Bounty: $0.00
- Upvotes: 16
- Submitted: 2026-02-20
- Disclosed: 2026-08-28
- Report: https://hackerone.com/reports/3564941
- CVE: CVE-2026-58044, CVE-2026-48932

## Team summary

A flaw in Node.js HTTP client can cause a request desynchronization for Node.js-based forwarding proxies that rebuild outbound headers from the visible `IncomingMessage` headers while piping the original body to a reused backend connection.

Node.js can omit headers beyond `maxHeadersCount` / `maxHeaderPairs` from `req.headers`, `req.rawHeaders`, and `req.headersDistinct`, while still using those omitted headers internally for HTTP message framing. In particular, `Content-Length` can be hidden from userland while the request body is still delivered.

This vulnerability affects all supported release lines: **Node.js 22**, **Node.js 24**, and **Node.js 26**.
