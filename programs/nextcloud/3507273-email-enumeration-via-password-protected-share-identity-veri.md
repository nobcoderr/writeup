# Email Enumeration via Password-Protected Share Identity Verification

- Program: Nextcloud
- Weakness / temuan: **Information Disclosure**
- Severity: low
- State: resolved
- Bounty: $100.00
- Upvotes: 35
- Submitted: 2026-01-12
- Disclosed: 2026-09-05
- Report: https://hackerone.com/reports/3507273

## Team summary

Requesting a password for an email share gave different response messages depending if the email address is the share recipient or not, allowing to confirm the intended recipient when someone managed to get access to the share token.
