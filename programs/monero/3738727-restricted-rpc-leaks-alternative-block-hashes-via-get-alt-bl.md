# Restricted RPC leaks alternative block hashes via /get_alt_blocks_hashes

- Program: Monero
- Weakness / temuan: **Improper Access Control - Generic**
- Severity: low
- State: resolved
- Bounty: $0.00
- Upvotes: 52
- Submitted: 2026-05-15
- Disclosed: 2026-07-20
- Report: https://hackerone.com/reports/3738727

## Team summary

The `/get_alt_blocks_hashes` RPC endpoint was restricted to prevent unintended access to alternative block hashes. The endpoint had previously been unrestricted. The issue was assessed as low severity due to the limited impact and the availability of similar information through other mechanisms.

## Researcher summary

Monero's restricted RPC mode is designed to limit the information exposed to untrusted clients. The `get_info` endpoint correctly hides alternative block metadata by returning `alt_blocks_count` as `0`.

However, the separate `get_alt_blocks_hashes` endpoint was not restricted in the same way and continued to return the list of alternative block hashes.

This inconsistency allowed clients connected to the restricted RPC port to learn whether alternative blocks existed and retrieve their exact hashes.
