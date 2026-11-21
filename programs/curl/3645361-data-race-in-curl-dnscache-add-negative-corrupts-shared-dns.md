# Data race in Curl_dnscache_add_negative() corrupts shared DNS cache — heap corruption and double-free when using CURLOPT_SHARE with CURL_LOCK_DATA_DNS

- Program: curl
- Weakness / temuan: **Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')**
- Severity: medium
- State: informative
- Bounty: $0.00
- Upvotes: 23
- Submitted: 2026-04-02
- Disclosed: 2026-04-04
- Report: https://hackerone.com/reports/3645361

## Temuan

Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')

Public writeup body was not in the disclosed JSON; open the report link above.
