# Stored HTML Injection (CWE-79) via Livechat Visitor Name

- Program: Rocket.Chat
- Weakness / temuan: **Cross-site Scripting (XSS) - DOM**
- Severity: low
- State: resolved
- Bounty: $0.00
- Upvotes: 15
- Submitted: 2026-07-18
- Disclosed: 2026-08-20
- Report: https://hackerone.com/reports/3872858
- CVE: CVE-2026-65644

## Team summary

REST API endpoint POST /api/v1/livechat/visitor accepts an unauthenticated, unsanitized name field for Livechat visitors. This name is stored raw and later rendered via dangerouslySetInnerHTML in the Omnichannel Queue side panel (InquireSidePanelItem.tsx), injecting a real, clickable HTML link - pointing to any attacker-controlled domain, with arbitrary social-engineering text - into the DOM of any agent viewing the queue.
