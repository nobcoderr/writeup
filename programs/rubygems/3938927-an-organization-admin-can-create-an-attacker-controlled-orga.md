# An organization admin can create an attacker-controlled organization owner via the gem transfer flow 

- Program: RubyGems
- Weakness / temuan: **Improper Access Control - Generic**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 27
- Submitted: 2026-08-14
- Disclosed: 2026-10-15
- Report: https://hackerone.com/reports/3938927

## Team summary

An Organization admin on RubyGems.org can grant the Owner role, which is reserved for existing owners, by going through the gem transfer flow instead of the normal membership flow. The membership endpoints correctly stop admins from inviting owners: a direct owner invite returns 404, and adding a direct gem owner returns 403.

The transfer flow only checks that the user is an admin of the Organization. It then accepts whatever role is submitted for each invitee, including Owner, and creates the Organization membership without applying the owner-only rule. A previous fix enforced this rule on the direct membership route but did not extend it to gem transfers.
