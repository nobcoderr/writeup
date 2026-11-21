# Formula injection in conversion tracking report export

- Program: Revive Adserver
- Weakness / temuan: **Code Injection**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 9
- Submitted: 2026-07-12
- Disclosed: 2026-11-11
- Report: https://hackerone.com/reports/3859000
- CVE: CVE-2026-108563
- Asset type: SOURCE_CODE

## Team summary

### Description

HackerOne community member BapToutatis has reported spreadsheet formula injection in conversion-tracking report exports. An unauthenticated attacker can submit conversion values that are subsequently written as formulas rather than text in an XLS report. Opening the exported workbook in a spreadsheet application can evaluate attacker-supplied formulas. The confirmed impact is formula execution within the workbook; disclosure of information to the attacker has not been established.

### Resolution

Conversion values are sanitised before being written to the affected XLS report sections, preventing them from being interpreted as formulas.

### Security advisory

https://www.revive-adserver.com/security/revive-sa-2026-004
