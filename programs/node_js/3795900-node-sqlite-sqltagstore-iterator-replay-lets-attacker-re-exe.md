# node:sqlite SQLTagStore Iterator Replay Lets Attacker Re-Execute Victim-Bound Writes Indefinitely

- Program: Node.js
- Weakness / temuan: **Time-of-check Time-of-use (TOCTOU) Race Condition**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 11
- Submitted: 2026-06-11
- Disclosed: 2026-08-28
- Report: https://hackerone.com/reports/3795900
- CVE: CVE-2026-58041

## Team summary

A flaw in Node.js node:sqlite allows a stale StatementSyncIterator created through DatabaseSync#createTagStore() to continue executing a cached prepared statement after it has been reset and rebound with new parameters. SQLTagStore resets cached statements using sqlite3_reset() directly, bypassing the iterator invalidation mechanism introduced for StatementSync in recent releases

This vulnerability affects Node.js **22.x**, **24.x**, and **26.x**.
