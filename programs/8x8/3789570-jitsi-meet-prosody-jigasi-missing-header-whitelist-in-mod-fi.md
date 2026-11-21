# jitsi-meet: Prosody/Jigasi missing header whitelist in mod_filter_iq_rayo allows arbitrary SIP header injection and Caller ID spoofing

- Program: 8x8
- Weakness / temuan: **Improper Input Validation**
- Severity: low
- State: resolved
- Bounty: $100.00
- Upvotes: 72
- Submitted: 2026-06-08
- Disclosed: 2026-07-02
- Report: https://hackerone.com/reports/3789570

## Team summary

Jitsi Meet's Prosody and Jigasi components contained a SIP header injection vulnerability in the interaction between `mod_filter_iq_rayo.lua` and the call handling backend. The Prosody filter implemented an incomplete blocklist that stripped only three specific internal header names (`X-outbound-call-initiator-user`, `X-outbound-call-initiator-group`, and `JvbRoomName` on visitor nodes) from client-supplied Rayo `<dial>` IQ stanzas, but forwarded all other arbitrary headers unfiltered to Jigasi. Jigasi's `CallControl.java` consumed these headers without validation and stored them in an `extraHeaders` map. `SipGatewaySession.java` then injected every entry directly into outbound SIP `INVITE` requests as raw protocol-level headers. This allowed authenticated users with outbound-call privileges to inject arbitrary SIP headers such as `P-Asserted-Identity` and `Remote-Party-ID`, enabling Caller ID spoofing on outgoing SIP calls in environments where Jigasi operates as a trusted SIP peer.

Changes:
* fix(security): Implement whitelist for Rayo dial headers
  * https://github.com/jitsi/jitsi-meet/pull/17480

We thank @pmgjoe for submitting this report to us.
