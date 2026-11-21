# Null Dereference in X509ToObject

- Program: Node.js
- Weakness / temuan: **NULL Pointer Dereference**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 22
- Submitted: 2026-06-25
- Disclosed: 2026-10-23
- Report: https://hackerone.com/reports/3824331

## Team summary

A null pointer dereference in Node.js X.509 certificate handling could cause the process to crash when converting a specially crafted certificate to a JavaScript object through `X509ToObject`.

An attacker able to supply or influence certificate data consumed by an affected application could trigger a denial of service by causing the Node.js process to terminate.

This vulnerability affects Node.js **24.x** and **26.x**.
