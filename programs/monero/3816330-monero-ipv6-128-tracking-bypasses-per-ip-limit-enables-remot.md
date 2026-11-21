# Monero IPv6 /128 tracking bypasses per-IP limit, enables remote OOM

- Program: Monero
- Weakness / temuan: **Uncontrolled Resource Consumption**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 23
- Submitted: 2026-06-21
- Disclosed: 2026-10-28
- Report: https://hackerone.com/reports/3816330

## Team summary

Monero's IPv6 connection tracking uses individual `/128` addresses, allowing the per-IP RPC connection limit to be bypassed by using multiple IPv6 addresses. This undermines the intended connection restrictions for IPv6 clients. 

Resolved in v0.18.5.3: https://github.com/monero-project/monero/pull/10812
