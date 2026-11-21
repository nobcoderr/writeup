# Unauthenticated Path Traversal (LFI) via /custom-sounds/ when CustomSounds uses FileSystem storage

- Program: Rocket.Chat
- Weakness / temuan: **Path Traversal**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 47
- Submitted: 2026-01-17
- Disclosed: 2026-08-03
- Report: https://hackerone.com/reports/3514640
- CVE: CVE-2026-56845

## Team summary

An unauthenticated path traversal (LFI) vulnerability exists under /custom-sounds/ when CustomSounds storage is configured to FileSystem. By including ../ sequences in the request path, an attacker can read arbitrary files outside the base directory.
