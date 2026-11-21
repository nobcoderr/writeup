# A third-party Basecamp OAuth token mints a full launchpad web session through GET /my/login_option

- Program: Basecamp
- Weakness / temuan: **Improper Access Control - Generic**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 33
- Submitted: 2026-09-05
- Disclosed: 2026-10-30
- Report: https://hackerone.com/reports/3999856

## Team summary

A Basecamp API endpoint that hands a signed-in person off to their 37signals ID web session accepted any third-party OAuth token, including one an integration had been granted only for Basecamp data. An integration the victim had authorized could obtain a full 37signals ID web session, change their account settings, and keep that session after its access was revoked. The handoff now only honors the session bridge our own apps use, so third-party OAuth tokens can no longer mint a 37signals ID session through it. Thanks to @deivizzzz for a precise report.
