# Access control bypass due to request precedence issue in global input registration

- Program: Revive Adserver
- Weakness / temuan: **Insecure Direct Object Reference (IDOR)**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 4
- Submitted: 2026-06-29
- Disclosed: 2026-11-11
- Report: https://hackerone.com/reports/3831102
- CVE: CVE-2026-107247
- Asset type: SOURCE_CODE

## Team summary

### Description

HackerOne community member kushbafti has reported an authorization bypass affecting multiple administration pages in Revive Adserver 6.0.0 through 6.0.8. The regression was introduced in commit 156dee7bc during input-helper simplification. Version 5.5.3 retains the original POST-first behavior and is not affected by this regression. Object identifiers used for permission checks were read with GET precedence, while form submissions could select different objects through POST parameters. A manager could supply identifiers belonging to their own agency in the URL and another agency in the submitted form, allowing unauthorized changes, campaign reassignment and access to other agencies' inventory.

### Resolution

Global input registration now gives POST parameters precedence over GET parameters, so permission checks and submitted form values use the same object identifiers.

### Security advisory

https://www.revive-adserver.com/security/revive-sa-2026-004
