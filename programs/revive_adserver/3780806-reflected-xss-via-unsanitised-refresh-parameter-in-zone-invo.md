# Reflected XSS via unsanitised refresh parameter in zone invocation tag

- Program: Revive Adserver
- Weakness / temuan: **Cross-site Scripting (XSS) - Reflected**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 29
- Submitted: 2026-06-03
- Disclosed: 2026-06-25
- Report: https://hackerone.com/reports/3780806
- CVE: CVE-2026-50740

## Team summary

HackerOne community member Mahmoud Khaled (Kanon4) has reported a missing sanitisation of user input in the zone-include.php script of Revive Adserver 6.0.7 and earlier. A low‑privileged user could exploit the refresh parameter of the iFrame invocation tag to perform reflected XSS attacks.
