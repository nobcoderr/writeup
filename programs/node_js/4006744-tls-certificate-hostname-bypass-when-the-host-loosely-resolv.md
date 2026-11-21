# TLS certificate hostname bypass when the host loosely resolves to an IP address

- Program: Node.js
- Weakness / temuan: **Improper Certificate Validation**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 24
- Submitted: 2026-09-07
- Disclosed: 2026-10-23
- Report: https://hackerone.com/reports/4006744
- CVE: CVE-2026-106069

## Team summary

A flaw in Node.js TLS hostname verification can cause a server certificate to be validated against a different IP address than the one the client connected to, when the host is a non-canonical IPv4 literal with a leading zero, such as `0127.0.0.1`.

`tls.checkServerIdentity()` normalizes the host following the WHATWG URL rules, which read a leading-zero octet as octal (`0127.0.0.1` becomes `87.0.0.1`), while the connection is made through the operating system resolver, which on some platforms such as macOS reads it as decimal (`127.0.0.1`). A server at the connected address can then be authenticated with a certificate issued for another IP address.

This vulnerability affects Node.js **26.x**, **24.x**, and **22.x**.
