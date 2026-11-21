# OAuth redirect uri validation bypass for :proxima_first_party_sync apps

- Program: GitHub
- Weakness / temuan: **Open Redirect**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 79
- Submitted: 2026-03-06
- Disclosed: 2026-07-21
- Report: https://hackerone.com/reports/3588801
- CVE: CVE-2026-4296

## Team summary

An incorrect regular expression vulnerability was identified in GitHub Enterprise Server that allowed an attacker to bypass OAuth redirect URI validation. An attacker with knowledge of a first-party OAuth application's registered callback URL could craft a malicious authorization link that, when clicked by a victim, would redirect the OAuth authorization code to an attacker-controlled domain. This could allow the attacker to gain unauthorized access to the victim's account with the scopes granted to the OAuth application. This vulnerability affected all versions of GitHub Enterprise Server prior to 3.21 and was fixed in versions 3.20.1, 3.19.5, 3.18.8, 3.17.14, 3.16.17, 3.15.21, 3.14.26. This vulnerability was reported via the GitHub Bug Bounty program.

[CVE-2026-4296](https://nvd.nist.gov/vuln/detail/CVE-2026-4296)
