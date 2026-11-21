# Able to bypass authorization logic and gain more access then intended

- Program: GitHub
- Weakness / temuan: **Able to bypass authorization logic and gain more access then intended**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 105
- Submitted: 2026-05-05
- Disclosed: 2026-07-15
- Report: https://hackerone.com/reports/3713965
- CVE: CVE-2026-9106

## Team summary

A UI misrepresentation vulnerability was identified in GitHub Enterprise Server that allowed an OAuth application to gain unintended access to an organization's runner management. An attacker could exploit this by creating an OAuth application requesting the manage_runners:org scope and directing a victim user to authorize it, as the scope was not displayed on the authorization consent screen. This vulnerability affected all versions of GitHub Enterprise Server prior to 3.22 and was fixed in versions 3.21.2, 3.20.4, 3.19.8, 3.18.11, 3.17.17, 3.16.20. This vulnerability was reported via the GitHub Bug Bounty program.

[CVE-2026-9106](https://nvd.nist.gov/vuln/detail/CVE-2026-9106)
