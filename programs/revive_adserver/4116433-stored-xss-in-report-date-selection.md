# Stored XSS in report date selection

- Program: Revive Adserver
- Weakness / temuan: **Cross-site Scripting (XSS) - Stored**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 2
- Submitted: 2026-10-15
- Disclosed: 2026-11-11
- Report: https://hackerone.com/reports/4116433
- CVE: CVE-2026-108561
- Asset type: SOURCE_CODE

## Team summary

### Description

HackerOne community member Matías López Pereira (HackerOne: @mlopez01) has reported stored XSS in the date-selection controls of standard reports. A crafted period_preset value could be saved in the victim's session and inserted into JavaScript without appropriate encoding. An attacker could supply a report URL retained through normal reauthentication; the payload could then execute on the initial report and subsequent report views using the stored defaults.

### Resolution

Date-selection values are now encoded with JSON encoding appropriate for their JavaScript context. The same encoding has also been applied to the audit date-selection field.

### Security advisory

https://www.revive-adserver.com/security/revive-sa-2026-004
