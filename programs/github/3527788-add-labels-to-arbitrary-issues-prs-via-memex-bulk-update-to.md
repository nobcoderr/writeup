# Add labels to arbitrary issues/prs via Memex Bulk Update to compromise github actions label gating 

- Program: GitHub
- Weakness / temuan: **Insecure Direct Object Reference (IDOR)**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 46
- Submitted: 2026-01-27
- Disclosed: 2026-08-25
- Report: https://hackerone.com/reports/3527788
- CVE: CVE-2026-3306

## Team summary

An improper authorization vulnerability was identified in GitHub Enterprise Server that allowed a user with read access to a repository and write access to a project to modify issue and pull request metadata through the project. When adding an item to a project that already existed, column value updates were applied without verifying the actor's repository write permissions.

[CVE-2026-3306](https://nvd.nist.gov/vuln/detail/CVE-2026-3306)
