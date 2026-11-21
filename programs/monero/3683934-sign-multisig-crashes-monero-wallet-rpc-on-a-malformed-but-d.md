# sign_multisig crashes monero-wallet-rpc on a malformed but decryptable multisig txset

- Program: Monero
- Weakness / temuan: **sign_multisig crashes monero-wallet-rpc on a malformed but decryptable multisig txset**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 35
- Submitted: 2026-04-19
- Disclosed: 2026-09-17
- Report: https://hackerone.com/reports/3683934

## Team summary

`monero-wallet-rpc` `sign_multisig` is vulnerable to a process crash from malformed multisig transaction data.

A malicious multisig participant can supply a txset with empty input/source vectors that passes existing consistency checks but later causes an unchecked access during signing, terminating the wallet RPC process instead of returning an error.

Exploitation requires the attacker to be a multisig participant, or otherwise obtain a txset correctly encrypted for the target wallet. The issue does not enable fund theft.

Resolved in https://github.com/monero-project/monero/pull/10426 and v0.18.5.0.
