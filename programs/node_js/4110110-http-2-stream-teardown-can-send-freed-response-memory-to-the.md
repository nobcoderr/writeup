# HTTP/2 stream teardown can send freed response memory to the peer

- Program: Node.js
- Weakness / temuan: **Use After Free**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 28
- Submitted: 2026-10-13
- Disclosed: 2026-11-12
- Report: https://hackerone.com/reports/4110110
- CVE: CVE-2026-123866
- Asset type: SOURCE_CODE

## Team summary

A flaw in Node.js HTTP/2 handling can cause HTTP/2 stream teardown can send freed response memory to the peer.

This vulnerability affects Node.js **22.x**, **24.x**, and **26.x**.
