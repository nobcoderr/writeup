# Reflected XSS in popup invocation options

- Program: Revive Adserver
- Weakness / temuan: **Cross-site Scripting (XSS) - Reflected**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 9
- Submitted: 2026-08-26
- Disclosed: 2026-11-11
- Report: https://hackerone.com/reports/3971985
- CVE: CVE-2026-108565
- Asset type: SOURCE_CODE

## Team summary

### Description

HackerOne community member miauzxw has reported reflected XSS in the popup invocation options. The top, left, timeout and delay request parameters could be included in HTML attributes without proper encoding. An attacker can send a crafted URL to an authenticated user to execute JavaScript in that user's browser. Exploitation requires an existing popup zone, a configuration that can be created through the administrator API but is not offered by the normal zone-creation interface.

### Resolution

Popup option values are now HTML-encoded when included in invocation-option form fields.

### Security advisory

https://www.revive-adserver.com/security/revive-sa-2026-004
