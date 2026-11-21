# XML‑RPC login leak exposes valid session ID enabling unauthorized API access

- Program: Revive Adserver
- Weakness / temuan: **Improper Access Control - Generic**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 28
- Submitted: 2026-06-05
- Disclosed: 2026-06-25
- Report: https://hackerone.com/reports/3783738
- CVE: CVE-2026-50744

## Team summary

HackerOne community member Kenji Subagja (garuthacktivist) has reported a way to bypass the admin‑only restriction of the XML‑RPC API in Revive Adserver 6.0.7. The API response for the `ox.login` method returned a session ID cookie in the HTTP headers, and although the method correctly returned an error, the associated session was not invalidated. As a result, the leaked session ID could be used to perform subsequent API calls without restrictions.
