# Reflected XSS via wrong permission check in conversion statistics

- Program: Revive Adserver
- Weakness / temuan: **Cross-site Scripting (XSS) - Reflected**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 9
- Submitted: 2026-07-21
- Disclosed: 2026-11-11
- Report: https://hackerone.com/reports/3878649
- CVE: CVE-2026-108558
- Asset type: SOURCE_CODE

## Team summary

### Description

HackerOne community member Patrick Lang (7YR) has reported a reflected XSS vulnerability in the conversion-statistics pages. An incorrect ownership check used the advertiser identifier in place of the website identifier, allowing crafted website input to reach the page output. An attacker can send a crafted URL to an authenticated user and execute JavaScript in that user's browser. A related hour-parameter output issue is addressed by the same fix.

### Resolution

Website ownership checks now validate the correct identifier, and the hour parameter is normalised to an integer before formatting.

### Security advisory

https://www.revive-adserver.com/security/revive-sa-2026-004
