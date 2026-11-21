# Missing Duplicate Check allowing Multiple Retention Rules per System Tag

- Program: Nextcloud
- Weakness / temuan: **Business Logic Errors**
- Severity: low
- State: resolved
- Bounty: $0.00
- Upvotes: 20
- Submitted: 2026-01-23
- Disclosed: 2026-09-05
- Report: https://hackerone.com/reports/3521646

## Team summary

The bug allowed admins to create multiple retention rules for the same tag, potentially causing confusion for other admins as they are not able to directly see the applicable retention time.
