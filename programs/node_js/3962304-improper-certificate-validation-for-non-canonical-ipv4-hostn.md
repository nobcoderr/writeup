# Improper certificate validation for non-canonical IPv4 hostnames allows DNS SANs to authenticate IP endpoints

- Program: Node.js
- Weakness / temuan: **Improper Certificate Validation**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 13
- Submitted: 2026-08-23
- Disclosed: 2026-10-23
- Report: https://hackerone.com/reports/3962304
- CVE: CVE-2026-106072

## Team summary

A flaw in Node.js TLS hostname verification allows a certificate with only a DNS SAN to authenticate an IP endpoint when the client connects using a non-canonical IPv4 spelling, such as `0177.0.0.1`, `0x7f.0.0.1`, `2130706433` or `127.1`.

`tls.checkServerIdentity()` did not classify these hosts as IP addresses, but normalized them to their canonical form and matched the result against the certificate DNS names. A certificate containing `DNS:127.0.0.1` and no `IP Address:127.0.0.1` SAN was therefore accepted, while the same certificate is correctly rejected for `127.0.0.1`. Exploitation requires a certificate with a numeric DNS SAN issued by a CA trusted by the client, and a platform resolver that accepts these spellings, such as glibc.

This vulnerability affects Node.js **26.x**, **24.x**, and **22.x**.
