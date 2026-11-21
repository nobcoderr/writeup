# Uppercase sni context matching can lead to mtls authorization bypass due to case-sensitive hostname matching

- Program: Node.js
- Weakness / temuan: **Improper Access Control - Generic**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 7
- Submitted: 2026-04-07
- Disclosed: 2026-06-25
- Report: https://hackerone.com/reports/3656869
- CVE: CVE-2026-48928

## Team summary

A inconsistency in Node.js hostname matching can cause a trust-policy bypass in multi-context mTLS setups.

This vulnerability affects all supported release lines: **Node.js 22**, **Node.js 24**, and **Node.js 26**.
