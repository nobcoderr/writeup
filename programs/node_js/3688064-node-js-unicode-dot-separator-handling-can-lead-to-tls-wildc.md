# Node.js unicode dot separator handling can lead to tls wildcard-depth authentication bypass due to resolver and verifier hostname normalization mismat

- Program: Node.js
- Weakness / temuan: **Improper Handling of Unicode Encoding**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 18
- Submitted: 2026-04-21
- Disclosed: 2026-06-25
- Report: https://hackerone.com/reports/3688064
- CVE: CVE-2026-48618

## Team summary

A flaw in Node.js TLS hostname handling can cause Node.js unicode dot separator handling can lead to tls wildcard-depth authentication bypass due to resolver and verifier hostname normalization mismat.

This can lead to confidentiality impact or bypass of the intended security boundary under affected configurations.

This vulnerability affects all supported release lines: **Node.js 22**, **Node.js 24**, and **Node.js 26**.
