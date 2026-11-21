# Stored XSS via unescaped tracker name in append-code check

- Program: Revive Adserver
- Weakness / temuan: **Cross-site Scripting (XSS) - Stored**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 10
- Submitted: 2026-06-26
- Disclosed: 2026-11-11
- Report: https://hackerone.com/reports/3826207
- CVE: CVE-2026-108562
- Asset type: SOURCE_CODE

## Team summary

### Description

HackerOne community member flasks has reported a stored XSS vulnerability in the 'maintenance-appendcode-check.php' tool. A manager can store a malicious tracker name and cause the tracker to appear in the maintenance results. When an administrator opens the affected page, the name is displayed without proper escaping and the embedded JavaScript executes in the administrator's browser.

### Resolution

Tracker names are now HTML-encoded when displayed by the append-code maintenance tool.

### Security advisory

https://www.revive-adserver.com/security/revive-sa-2026-004
