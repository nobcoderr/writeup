# Launchpad file read leaks production keys

- Program: Basecamp
- Weakness / temuan: **Path Traversal**
- Severity: critical
- State: resolved
- Bounty: $9337.00
- Upvotes: 55
- Submitted: 2026-08-23
- Disclosed: 2026-10-28
- Report: https://hackerone.com/reports/3962925

## Team summary

A file-read vulnerability in Launchpad exposed production storage credentials. We fixed the vulnerable processing path, rotated the exposed credentials and deleted the old key. Thanks to bl0rph for a detailed report and for working with us through remediation.
