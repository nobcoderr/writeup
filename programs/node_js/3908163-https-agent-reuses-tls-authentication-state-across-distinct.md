# HTTPS Agent reuses TLS authentication state across distinct secureContext policies

- Program: Node.js
- Weakness / temuan: **Improper Certificate Validation**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 25
- Submitted: 2026-08-01
- Disclosed: 2026-11-12
- Report: https://hackerone.com/reports/3908163
- CVE: CVE-2026-123877
- Asset type: SOURCE_CODE

## Team summary

A flaw in Node.js TLS hostname handling can cause HTTPS Agent reuses TLS authentication state across distinct secureContext policies.

This vulnerability affects Node.js **22.x**, **24.x**, and **26.x**.
