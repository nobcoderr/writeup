# Reflected XSS in stats‑video.php via improperly encoded URL parameters

- Program: Revive Adserver
- Weakness / temuan: **Cross-site Scripting (XSS) - Reflected**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 12
- Submitted: 2026-06-10
- Disclosed: 2026-06-25
- Report: https://hackerone.com/reports/3793243
- CVE: CVE-2026-50745

## Team summary

HackerOne community member Mahmoud Khaled (Kanon4) has reported a missing sanitisation of user input in the stats-video.php script. The way URLs to this script were constructed did not follow best practices, and the output of the Smarty custom helper function url was neither properly encoded nor sanitised, allowing user‑supplied input to be reflected without escaping.
