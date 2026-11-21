#  All stored Slack and Teams credentials can be deleted via Management Console CSRF

- Program: GitHub
- Weakness / temuan: **Cross-Site Request Forgery (CSRF)**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 23
- Submitted: 2026-07-22
- Disclosed: 2026-11-18
- Report: https://hackerone.com/reports/3882740
- CVE: CVE-2026-110288
- Asset type: HARDWARE

## Team summary

A cross-site request forgery vulnerability was identified in GitHub Enterprise Server that allowed an unauthenticated attacker to delete stored Slack and Microsoft Teams ChatOps configuration and provider credentials by inducing an authenticated Management Console operator's browser to send a cross-site GET request to the integration removal endpoint without a CSRF token. Exploitation required configured ChatOps integrations and an operator visiting attacker-controlled content while signed in to the Management Console; deletion could disrupt ChatOps notifications and commands when configuration was applied or services reloaded. 
[CVE-2026-110288](https://www.cve.org/cverecord?id=CVE-2026-110288)
