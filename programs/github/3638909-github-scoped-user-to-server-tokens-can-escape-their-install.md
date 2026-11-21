# GitHub scoped user to server tokens can escape their installation

- Program: GitHub
- Weakness / temuan: **Improper Access Control - Generic**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 80
- Submitted: 2026-03-31
- Disclosed: 2026-07-29
- Report: https://hackerone.com/reports/3638909
- CVE: CVE-2026-5845

## Team summary

An improper authorization vulnerability in scoped user-to-server (ghu_) token authorization in GitHub Enterprise Server allows an authenticated attacker to access private repositories outside the intended installation scope, which can include write operations, via an authorization fallback that treated a revoked/deleted installation as a global installation context, which could be chained with token revocation timing and SSH push attribution to obtain and reuse a victim-scoped token. This vulnerability affected all versions of GitHub Enterprise Server prior to 3.21 and was fixed in versions 3.20.1, 3.19.5, 3.18.8, 3.17.14, 3.16.17, 3.15.21, and 3.14.26.

[CVE-2026-5845](https://www.cve.org/CVERecord?id=CVE-2026-5845)
