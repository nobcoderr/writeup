# Unauthenticated reflected XSS in update history

- Program: Revive Adserver
- Weakness / temuan: **Cross-site Scripting (XSS) - Reflected**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 2
- Submitted: 2026-10-01
- Disclosed: 2026-11-11
- Report: https://hackerone.com/reports/4075098
- CVE: CVE-2026-108560
- Asset type: SOURCE_CODE

## Team summary

### Description

HackerOne community member Matías López Pereira (HackerOne: @mlopez01) reported a reflected XSS vulnerability in `updates-history.php`. Attacker-controlled values were included in XML command attributes without appropriate encoding, allowing crafted input to inject executable XHTML into the response.

The preliminary session check covered xajax POST requests but omitted GET requests, exposing an unauthenticated attack path. Authenticated administrator requests could also reach the unsafe XML output.

### Resolution

The preliminary session check now applies to both GET and POST xajax requests. XML command attribute values are also encoded in both response serializers, preventing crafted values from injecting markup.

### Security advisory

https://www.revive-adserver.com/security/revive-sa-2026-004
