# Unauthenticated reading of every file via livechat auth and predicting MongoDB ObjectId()

- Program: Rocket.Chat
- Weakness / temuan: **Improper Access Control - Generic**
- Severity: critical
- State: resolved
- Bounty: $0.00
- Upvotes: 49
- Submitted: 2026-04-21
- Disclosed: 2026-06-15
- Report: https://hackerone.com/reports/3687142
- CVE: CVE-2026-48616

## Team summary

Protected file downloads at `/file-upload/:fileId/:name` authorize livechat access using `rc_room_type=l` with `rc_rid+rc_token`, but the authorization path does not verify that `rc_rid` matches the requested file's `rid`. Furthermore, `:fileId` is predictable via sequential MongoDB IDs, and `:name` can be anything, allowing unauthenticated discovery of all uploaded files.
