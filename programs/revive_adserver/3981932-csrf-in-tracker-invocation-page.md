# CSRF in tracker invocation page

- Program: Revive Adserver
- Weakness / temuan: **Cross-Site Request Forgery (CSRF)**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 14
- Submitted: 2026-08-31
- Disclosed: 2026-11-11
- Report: https://hackerone.com/reports/3981932
- CVE: CVE-2026-77168
- Asset type: SOURCE_CODE

## Team summary

### Description

HackerOne community member Abhishek Nandkumar Bhaskar (Abhi_Hackz) has reported a leftover state-changing handler in 'tracker-invocation.php' that did not verify a CSRF token. The handler could modify a tracker name, description or advertiser assignment using the victim's permissions. It was not used by the normal invocation-tag interface. Exploitation requires an authenticated victim and a request path that carries the victim's session credentials.

### Resolution

The unused tracker-modification handler has been removed from the invocation-tag page.

### Security advisory

https://www.revive-adserver.com/security/revive-sa-2026-004
