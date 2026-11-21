# TaskProcessing callback authorization bypass allows ex-members to post as Assistant Talk Bot

- Program: Nextcloud
- Weakness / temuan: **Insecure Direct Object Reference (IDOR)**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 73
- Submitted: 2026-06-12
- Disclosed: 2026-08-14
- Report: https://hackerone.com/reports/3799010

## Team summary

An authenticated user could inject messages into Talk conversations they no longer had access to by scheduling a text processing task with a callback targeting the Assistant Talk Bot. The bot did not verify that the user still had access to the target conversation before posting messages under its trusted identity. Fixed in Assistant Talk Bot version 3.3.0 by limiting bot replies to active conversation participants only.
