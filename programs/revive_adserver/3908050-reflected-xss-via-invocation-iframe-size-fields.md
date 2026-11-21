# Reflected XSS via invocation iFrame size fields

- Program: Revive Adserver
- Weakness / temuan: **Cross-site Scripting (XSS) - Reflected**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 2
- Submitted: 2026-08-01
- Disclosed: 2026-11-11
- Report: https://hackerone.com/reports/3908050
- CVE: CVE-2026-108559
- Asset type: SOURCE_CODE

## Team summary

### Description

HackerOne community member Adam Rayyan Aryasatya (kannrisha) has reported reflected XSS in the iframe invocation options. The frame_width and frame_height request parameters could be included in HTML attributes without appropriate encoding when generating invocation tags for an any-size zone. An attacker can send a crafted URL to an authenticated user to execute JavaScript in that user's browser.

### Resolution

Width and height values are now HTML-encoded when included in invocation-option form fields.

### Security advisory

https://www.revive-adserver.com/security/revive-sa-2026-004
