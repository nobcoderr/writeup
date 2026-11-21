# Stored XSS in maintenance tools via unescaped entity names

- Program: Revive Adserver
- Weakness / temuan: **Cross-site Scripting (XSS) - Stored**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 25
- Submitted: 2026-06-04
- Disclosed: 2026-06-25
- Report: https://hackerone.com/reports/3781311
- CVE: CVE-2026-50742

## Team summary

HackerOne community member Althaf Shajahan (AnGrY) has reported stored XSS vulnerabilities in the `maintenance-acl-check.php` and `maintenance-banners-check.php` tools of Revive Adserver 6.0.7. The issue was caused by entity names being displayed without proper escaping when inconsistencies were detected. Whether the XSS payload is executed when an administrator uses the affected maintenance tools is not entirely under the attacker's control.
