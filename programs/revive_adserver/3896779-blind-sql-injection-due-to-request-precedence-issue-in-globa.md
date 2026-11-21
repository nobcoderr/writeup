# Blind SQL injection due to request precedence issue in global input registration

- Program: Revive Adserver
- Weakness / temuan: **SQL Injection**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 2
- Submitted: 2026-07-28
- Disclosed: 2026-11-11
- Report: https://hackerone.com/reports/3896779
- CVE: CVE-2026-107662
- Asset type: SOURCE_CODE

## Team summary

### Description

HackerOne community member sh4d0byss has reported blind SQL injection in the banner-zone and campaign-zone administration pages. Permission checks and database queries could use different values for the same request parameter. A restricted manager could exploit this mismatch to extract arbitrary database values, including password hashes and active session identifiers. Reusing an extracted, unexpired administrator session can grant administrative access and the ability to modify configuration or disrupt ad delivery.

### Resolution

The fix combines the request-precedence correction described in the authorization bypass finding with changes to the common input helpers. Global input registration and query-side helpers now both read POST values before GET values, ensuring that permission checks and database queries use the same identifiers. Cookies are excluded from this input path, removing dependence on the PHP request_order configuration. Both changes are required to close the reported input-source mismatch.

### Security advisory

https://www.revive-adserver.com/security/revive-sa-2026-004
