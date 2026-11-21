# Permission Model Bypass: `trace_events.createTracing().enable()` Writes Trace Logs Outside `--allow-fs-write`

- Program: Node.js
- Weakness / temuan: **Improper Access Control - Generic**
- Severity: low
- State: resolved
- Bounty: $0.00
- Upvotes: 21
- Submitted: 2026-07-02
- Disclosed: 2026-07-29
- Report: https://hackerone.com/reports/3838601
- CVE: CVE-2026-56847

## Team summary

A flaw in Node.js Permission Model enforcement allows `trace_events.createTracing().enable()` Writes Trace Logs Outside `--allow-fs-write`.

This can lead to confidentiality impact or bypass of the intended security boundary under affected configurations.

This vulnerability affects Node.js **22.x**, **24.x**, and **26.x**.
