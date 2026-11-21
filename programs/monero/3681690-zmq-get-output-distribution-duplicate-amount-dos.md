# ZMQ get_output_distribution duplicate amount DoS

- Program: Monero
- Weakness / temuan: **ZMQ get_output_distribution duplicate amount DoS**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 22
- Submitted: 2026-04-18
- Disclosed: 2026-09-17
- Report: https://hackerone.com/reports/3681690

## Team summary

ZMQ `get_output_distribution` RPC is vulnerable to memory exhaustion DoS.

The method accepts an unbounded `amounts` array and returns a separate distribution for each entry. Repeating amount `0` causes the daemon to duplicate the full RingCT output distribution many times, allowing a small request to expand into a very large response.

The issue is also reachable with `--restricted-zmq-rpc`, because ZMQ lacks the stricter validation applied by restricted HTTP RPC.

Resolved in https://github.com/monero-project/monero/pull/10419 and v0.18.5.0.
