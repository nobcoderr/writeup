# dns.resolveAny() Aborts the Node.js Process When a DNS Response Contains More Than 256 A Records

- Program: Node.js
- Weakness / temuan: **Uncontrolled Resource Consumption**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 12
- Submitted: 2026-06-11
- Disclosed: 2026-08-28
- Report: https://hackerone.com/reports/3795657
- CVE: CVE-2026-58042

## Team summary

A flaw in Node.js can cause dns.resolveAny() Aborts the Node.js Process When a DNS Response Contains More Than 256 A Records.

Repeated triggering of this condition can lead to denial of service.

This vulnerability affects Node.js **26.x**, **24.x**, and **22.x**.
