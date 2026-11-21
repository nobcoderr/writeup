# HTTPS Agent PFX object-array key collision allows mTLS client identity reuse across different per-request certificates

- Program: Node.js
- Weakness / temuan: **Improper Authentication - Generic**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 24
- Submitted: 2026-06-22
- Disclosed: 2026-07-29
- Report: https://hackerone.com/reports/3816840
- CVE: CVE-2026-56850

## Team summary

A flaw in Node.js HTTPS Agent connection reuse can cause PFX object-array key collisions, allowing mutual TLS (mTLS) client identities to be reused across requests configured with different client certificates.

This vulnerability affects Node.js **26.x**, **24.x**, and **22.x**.
