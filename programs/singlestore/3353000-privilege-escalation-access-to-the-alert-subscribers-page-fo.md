# Privilege Escalation – Access to the Alert Subscribers page for users with low privileges

- Program: SingleStore
- Weakness / temuan: **Privilege Escalation**
- Severity: low
- State: resolved
- Bounty: $0.00
- Upvotes: 26
- Submitted: 2025-09-22
- Disclosed: 2026-07-01
- Report: https://hackerone.com/reports/3353000

## Team summary

A privilege escalation vulnerability in the SingleStore Helios alert management system allowed users with low privileges to access the Alert Subscribers API endpoint and retrieve email addresses and alert severity level preferences of notification subscribers, despite lacking authorization to view this information. This information disclosure posed a privacy risk and could potentially be leveraged for targeted phishing or social engineering attacks. The vulnerability was patched by restricting access to alert subscriber functionality to only authorized users with appropriate privileges.
