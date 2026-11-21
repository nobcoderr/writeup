# Keep-alive socket process a response that was written before the request was sent

- Program: Node.js
- Weakness / temuan: **Time-of-check Time-of-use (TOCTOU) Race Condition**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 15
- Submitted: 2026-09-17
- Disclosed: 2026-10-23
- Report: https://hackerone.com/reports/4038361
- CVE: CVE-2026-105481

## Team summary

A flaw in Node.js HTTP Agent connection reuse can cause a client to accept as valid a response that was sent before the client has sent the request. This is an incomplete fix of CVE-2026-48931.

The guard that destroys idle keep-alive sockets when unexpected data arrives only runs when the event loop polls for I/O. If an unsolicited response has already reached the socket but has not been read yet when the socket is handed to a new request, for example because the event loop was busy with synchronous work, the guard is removed without seeing it and the data is parsed as the response to the new request.

This vulnerability affects Node.js **26.x**, **24.x**, and **22.x**.
