# Cross-agency delivery rule set creation

- Program: Revive Adserver
- Weakness / temuan: **Insecure Direct Object Reference (IDOR)**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 11
- Submitted: 2026-08-10
- Disclosed: 2026-11-11
- Report: https://hackerone.com/reports/3929216
- CVE: CVE-2026-82978
- Asset type: SOURCE_CODE

## Team summary

## Description

HackerOne community members Shmulik Cohen and Dang Hung Vi independently reported an authorization bypass in 'channel-edit.php'. An authenticated manager could change the submitted agencyid parameter to create a delivery rule set belonging to another agency. The server trusted the submitted agency identifier when inserting the new rule set, allowing unauthorized creation of objects in another agency's account.

## Resolution

New delivery rule sets now obtain their agency identifier from the authenticated account rather than submitted form data. The agency identifier has also been removed from the form's hidden fields.

Security advisory: https://www.revive-adserver.com/security/revive-sa-2026-004
