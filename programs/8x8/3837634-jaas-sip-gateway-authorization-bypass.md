# JaaS SIP Gateway Authorization Bypass

- Program: 8x8
- Weakness / temuan: **Missing Authorization**
- Severity: medium
- State: resolved
- Bounty: $500.00
- Upvotes: 64
- Submitted: 2026-07-02
- Disclosed: 2026-08-12
- Report: https://hackerone.com/reports/3837634

## Team summary

The JaaS SIP gateway endpoint (`/sip-jibri-gateway/jibris/invite`) validated the `sip-outbound-call` feature flag from client-supplied JWTs without verifying the tenant's actual provisioned entitlements. This allowed tenants to place outbound SIP calls regardless of their subscription level. Our team promptly validated and addressed the report by implementing server-side entitlement checks to ensure proper authorization enforcement.

We thank @offseq for submitting this report to us.
