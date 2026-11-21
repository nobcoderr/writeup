# @jitsi/docker-jitsi-meet: `/colibri-relay-ws/` unsafe nginx regex (OCTO relay configuration)

- Program: 8x8
- Weakness / temuan: **Cross-site Scripting (XSS) - Generic**
- Severity: low
- State: resolved
- Bounty: $0.00
- Upvotes: 25
- Submitted: 2026-07-25
- Disclosed: 2026-08-25
- Report: https://hackerone.com/reports/3889473

## Team summary

@a3z4km3 reported an unsafe nginx regex pattern in docker-jitsi-meet's `/colibri-relay-ws/` location. When `ENABLE_OCTO` was enabled, the regex `[a-zA-Z0-9-\._]+` accepted arbitrary domain names and IP addresses for proxy_pass directives,  allowing unauthenticated requests to be proxied to attacker-specified destinations.

The vulnerable nginx location and associated relay WebSocket proxy configuration have been removed.

**Changes:**
* feat(web,jvb): remove deprecated colibri websocket support
  * https://github.com/jitsi/docker-jitsi-meet/pull/2285

We thank @a3z4km3 for submitting this report to us.
