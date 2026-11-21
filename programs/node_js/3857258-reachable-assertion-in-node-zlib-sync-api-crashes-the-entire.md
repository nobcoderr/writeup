# Reachable assertion in node:zlib sync API crashes the entire process via spoofed TypedArray byteLength (all 11 *Sync functions affected)

- Program: Node.js
- Weakness / temuan: **Uncontrolled Resource Consumption**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 12
- Submitted: 2026-07-11
- Disclosed: 2026-08-28
- Report: https://hackerone.com/reports/3857258
- CVE: CVE-2026-58045

## Team summary

A flaw in Node.js allows a spoofed `TypedArray` `byteLength` to trigger a reachable assertion in the synchronous `node:zlib` APIs, causing the entire process to crash. All 11 synchronous zlib functions are affected.

Repeated exploitation of this condition can result in a denial of service.

This vulnerability affects Node.js **22.x**, **24.x**, and **26.x**.
