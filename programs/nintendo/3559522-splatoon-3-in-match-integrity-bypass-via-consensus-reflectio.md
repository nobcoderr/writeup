# Splatoon 3 In-Match Integrity Bypass via Consensus Reflection Attack on Unordered Peer Submission

- Program: Nintendo
- Weakness / temuan: **Client-Side Enforcement of Server-Side Security**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 62
- Submitted: 2026-02-17
- Disclosed: 2026-07-02
- Report: https://hackerone.com/reports/3559522

## Team summary

-

## Researcher summary

In Splatoon 3's anticheat system, the way consoles exchanged integrity hashes during online matches let a cheater copy a legitimate player's hashes instead of computing their own.

* **The Problem:** During online matches, consoles would exchange integrity check data routinely throughout the battle on a timed schedule. The game did not enforce any specific order to this exchange, and all consoles were expected to exchange the same data, meaning a window was available for an attacker to see another console's submission before having to submit their own.

* **The Exploit:** A modified console hooks the anticheat data receiver, and checks if the packet is from the same console type as them. (Switch 1/2). Then, when it's time for us to send our own anticheat data, instead of sending data that would indicate tampered game code, we send the pre-recorded data from our peer. To the other clients, and to replay data, the modified console appears to be legitimate, with no trace of our dirty hashes.

* **The Fix:** Nintendo addressed this in game version 11.2.0 with a commit-reveal scheme. Each console now must first send a cryptographic commitment (using a cryptographically secure algorithm) of the current turn's hashes, bound to player-specific data, and only reveals the actual hash values on the following turn. Because every console has to lock in its answer one turn before anyone reveals theirs, copying another player's revealed values is useless.
