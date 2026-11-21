# A disabled account's API key still works on BMO's Mojolicious /rest/ routes, including for security-group bugs filed after the disable

- Program: Mozilla
- Weakness / temuan: **Improper Authentication - Generic**
- Severity: high
- State: resolved
- Bounty: $4000.00
- Upvotes: 32
- Submitted: 2026-09-05
- Disclosed: 2026-10-26
- Report: https://hackerone.com/reports/4000084

## Team summary

Mozilla's Bugzilla instance had two authentication implementations with inconsistent account status validation. The legacy REST API (rest.cgi) and web interface correctly refused disabled accounts, but the newer REST routes (/rest/search/*, /rest/component/*) authenticated API keys without checking if the account was still enabled.

The issue was fixed by adding proper account status validation to the REST API authentication flow.

## Researcher summary

BMO had two authentication paths, and only one of them checked whether an account was still enabled. The legacy stack (`rest.cgi` and the web UI) refused a disabled account. The Mojolicious `bugzilla.login` helper serving the native /rest/ V1 routes never called `is_enabled`.

Disabling an account deleted its login cookies but left its API keys and group memberships in place. So a key minted before the disable kept working on the native routes. Its owner could go on reading security-restricted bugs, including ones filed after the disable, and could still write through `PUT /rest/component`. Setting a component's triage owner or CC list that way handed restricted bugs to a second account that had never been in the security group. An account flagged to change its password, without being disabled, behaved the same way.

The people in that position are anyone whose account was shut off while they still held a key: offboarded staff, a banned user, or someone who closed their own account.

Mozilla fixed it in [mozilla-bteam/bmo#2757](https://github.com/mozilla-bteam/bmo/pull/2757), merged 2026-09-23 and shipped in `release-20260923.1`. The native login path now refuses disabled and password-reset accounts the way the legacy stack does. The affected code is BMO-specific. Upstream `bugzilla/bugzilla` has no Mojolicious login helper and isn't affected.
