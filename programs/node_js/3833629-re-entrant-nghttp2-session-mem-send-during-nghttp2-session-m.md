# Re-entrant `nghttp2_session_mem_send()` during `nghttp2_session_mem_recv()` causes heap-use-after-free in Node.js HTTP/2

- Program: Node.js
- Weakness / temuan: **Use After Free**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 17
- Submitted: 2026-06-30
- Disclosed: 2026-08-28
- Report: https://hackerone.com/reports/3833629
- CVE: CVE-2026-56848

## Team summary

A flaw in Node.js HTTP/2 handling allows `nghttp2_session_mem_send()` to be called re-entrantly while `nghttp2_session_mem_recv()` is executing, resulting in a heap-use-after-free.

This vulnerability affects Node.js **26.x**, **24.x**, and **22.x**.
