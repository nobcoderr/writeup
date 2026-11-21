# Authentication Bypass via XML Signature Wrapping in SAML SSO

- Program: Rocket.Chat
- Weakness / temuan: **Improper Authentication - Generic**
- Severity: critical
- State: resolved
- Bounty: $0.00
- Upvotes: 39
- Submitted: 2026-06-26
- Disclosed: 2026-07-27
- Report: https://hackerone.com/reports/3827674
- CVE: CVE-2026-58066

## Team summary

Rocket.Chat's SAML SSO verified XML signatures but did not bind the validated signature to `samlp:Response` / `saml:Assertion`. An attacker could submit a wrapped document carrying forged identity attributes alongside any valid signature made by the trusted IdP certificate, and log in as an arbitrary user.
