# Client-Side Denial of Service (DoS) via Memory Exhaustion on Password Reset Endpoint

- Program: Khan Academy
- Weakness / temuan: **Uncontrolled Resource Consumption**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 32
- Submitted: 2026-09-01
- Disclosed: 2026-10-05
- Report: https://hackerone.com/reports/3987499

## Writeup

Visiting ```/pwreset?action=reset ```endpoint while logged in causes the browser to automatically send thousands of requests (observable via Burp Suite or DevTools), leading to memory exhaustion and browser crash within few minutes.

##Steps to Reproduce
1. Log in to Khan Academy

2.  Open Burp Suite (or browser DevTools → Network tab) to monitor requests

3.Visit: 
```https://www.khanacademy.org/pwreset?action=reset```

4.  Observe Burp Suite shows thousands of requests being automatically generated without any user interaction

5.Monitor browser memory usage — it continuously increases

6. Within few minutes, the browser becomes unresponsive and eventually crashes or is suspended by the system

## Impact

1.Denial of Service for any logged‑in user who visits the link

2.Browser memory exhaustion leading to crash or system suspend

3.No user interaction required beyond visiting the link

4.Can be used in phishing campaigns to disrupt users
