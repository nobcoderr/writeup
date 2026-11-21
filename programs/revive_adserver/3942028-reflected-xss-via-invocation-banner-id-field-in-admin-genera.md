# Reflected XSS via invocation banner ID field in admin-generate.php

- Program: Revive Adserver
- Weakness / temuan: **Cross-site Scripting (XSS) - Reflected**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 12
- Submitted: 2026-08-15
- Disclosed: 2026-11-11
- Report: https://hackerone.com/reports/3942028
- CVE: CVE-2026-108564
- Asset type: SOURCE_CODE

## Team summary

### Description

HackerOne community member Umesh Paytode has reported reflected XSS through the banner identifier in the invocation-tag generation interface. When Direct Selection is enabled, attacker-supplied input could be included in HTML form fields without proper encoding. Successful exploitation requires an attacker to persuade an authenticated user to visit a crafted URL. Direct Selection is disabled by default.

### Resolution

Banner identifier values are now HTML-encoded when included in invocation-option form fields.

### Security advisory

https://www.revive-adserver.com/security/revive-sa-2026-004
