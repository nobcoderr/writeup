# DDP methods getThreadsList / getThreadMessages leaks private thread content to any authenticated low privilege user (unpatched sibling of #1446767)

- Program: Rocket.Chat
- Weakness / temuan: **NoSQL Injection**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 16
- Submitted: 2026-07-09
- Disclosed: 2026-08-20
- Report: https://hackerone.com/reports/3852135
- CVE: CVE-2026-65645

## Team summary

The Meteor DDP methods getThreadsList and getThreadMessages accept rid / tmid as raw, untyped parameters with no schema validation. A MongoDB operator object (e.g. {"$gt": "4"}) can be substituted for a string room-id or message-id. The authorization check resolves to a room the attacker already has access to, while the downstream data query fans out across all rooms - disclosing private thread parents and their full reply content to any low-privilege authenticated user.
The REST route chat.getThreadsList was patched in v5.0 (HackerOne report #1446767) by adding rid: {type:'string'} AJV validation. The equivalent DDP method was never given the same fix and remains exploitable
