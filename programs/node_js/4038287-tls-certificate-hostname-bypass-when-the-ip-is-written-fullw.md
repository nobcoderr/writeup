# TLS certificate hostname bypass when the IP is written fullwidth digits

- Program: Node.js
- Weakness / temuan: **Improper Certificate Validation**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 29
- Submitted: 2026-09-17
- Disclosed: 2026-10-23
- Report: https://hackerone.com/reports/4038287
- CVE: CVE-2026-105483

## Team summary

A flaw in Node.js TLS hostname verification allows a certificate without a matching IP address SAN to authenticate a connection to an IPv4 address when the host is written with non-ASCII characters, such as fullwidth digits (`１２７.0.0.1`).

`tls.checkServerIdentity()` did not recognize such hosts as IP addresses, even though they normalize and resolve to a regular IPv4 address, and matched them against the certificate DNS names and Common Name instead. A certificate containing `DNS:127.0.0.1` or `DNS:*.0.0.1` could therefore be accepted for an IP endpoint it was not issued for. This is a regression introduced after the fix for CVE-2026-48618.

This vulnerability affects Node.js **26.x** and **24.x**.
