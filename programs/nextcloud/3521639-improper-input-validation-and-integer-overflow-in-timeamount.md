# Improper Input Validation and Integer Overflow in timeamount parameter of files_retention app

- Program: Nextcloud
- Weakness / temuan: **Integer Overflow**
- Severity: low
- State: resolved
- Bounty: $0.00
- Upvotes: 23
- Submitted: 2026-01-23
- Disclosed: 2026-09-05
- Report: https://hackerone.com/reports/3521639

## Team summary

A missing validation of the provided value on API level, allowed an administrator to store a unintended long time amount as retention period potentially causing files to never get deleted.
