# PHP code injection in delivery-limitation `logical` validation bypass

- Program: Revive Adserver
- Weakness / temuan: **Code Injection**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 35
- Submitted: 2026-06-03
- Disclosed: 2026-06-25
- Report: https://hackerone.com/reports/3780854
- CVE: CVE-2026-50741

## Team summary

HackerOne community member Rio Darmawan (riodrwn) and Mikhail Ilin (doomtech) have independently reported new vectors to bypass the fix for CVE-2026-34916. Variants of such vectors have been also reported by phucrio and offsetmd. The fix can be bypassed either by sending a disallowed but otherwise valid plugin identifier as `type`, or using the `ox.setChannelTargeting` XML-RPC API method.
