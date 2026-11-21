# Missing campaign ownership check in zone bulk linking

- Program: Revive Adserver
- Weakness / temuan: **Insecure Direct Object Reference (IDOR)**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 10
- Submitted: 2026-08-21
- Disclosed: 2026-11-11
- Report: https://hackerone.com/reports/3958112
- CVE: CVE-2026-68486
- Asset type: SOURCE_CODE

## Team summary

### Description

HackerOne community member miauzxw reported a missing campaign ownership check in the bulk-linking operation of `zone-include.php`. The single-link operation and XML-RPC API also lacked the corresponding check. A manager, or a trafficker with zone-linking permissions, could associate another agency's campaign with their own zone.

Although agency filtering prevented foreign banners from being linked, the unauthorized association could expose the foreign campaign's name, type and identifier in the linked-campaign listing.

### Resolution

Campaign ownership is now checked in the bulk-linking and single-link operations and in the XML-RPC campaign-linking method.

### Security advisory

https://www.revive-adserver.com/security/revive-sa-2026-004
