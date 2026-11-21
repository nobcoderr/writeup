# CSRF in zone‑include.php allows unauthorized banner and campaign linking

- Program: Revive Adserver
- Weakness / temuan: **Cross-Site Request Forgery (CSRF)**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 20
- Submitted: 2026-06-04
- Disclosed: 2026-06-25
- Report: https://hackerone.com/reports/3781691
- CVE: CVE-2026-50743

## Team summary

HackerOne community member Althaf Shajahan (AnGrY) has reported that the `zone-include.php` script in Revive Adserver 6.0.7 was vulnerable to a CSRF attack. Linking and unlinking banners or campaigns to zones could be triggered via crafted GET or POST requests without any verification of the CSRF token, allowing an attacker to perform these actions on behalf of an authenticated administrator.
