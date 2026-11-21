# Cross-agency disclosure in website listing

- Program: Revive Adserver
- Weakness / temuan: **Insecure Direct Object Reference (IDOR)**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 12
- Submitted: 2026-07-23
- Disclosed: 2026-11-11
- Report: https://hackerone.com/reports/3883840
- CVE: CVE-2026-68485
- Asset type: SOURCE_CODE

## Team summary

### Description

HackerOne community member Shmulik Cohen has reported an authorization bypass in `website-index.php`. A restricted manager could change the `agencyid` request parameter to view another agency's website listing, including website names, identifiers and timestamps. Detailed website pages continued to enforce ownership checks.

### Resolution

The website listing now obtains the agency identifier from the authenticated account rather than the request.

### Security advisory

https://www.revive-adserver.com/security/revive-sa-2026-004
