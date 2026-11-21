# ████████ ████████ Server Full Exposure with Database Credentials

- Program: Essity
- Weakness / temuan: **Information Exposure Through Directory Listing**
- Severity: critical
- State: resolved
- Bounty: $0.00
- Upvotes: 12
- Submitted: 2026-03-03
- Disclosed: 2026-06-10
- Report: https://hackerone.com/reports/3584078
- Asset type: URL

## Writeup

I discovered that the ████████ ████████ web server (████████) has directory listing enabled, exposing the entire file structure including database credentials, full website backups, and sensitive internal documents.
https://████████/
████████
████████

## Impact

Database compromise - Working credentials grant full read/write access to ████████'s database containing customer PII
Complete source code theft - 69MB backup file contains entire website code
Customer data exposure - Uploads directory may contain sensitive user information
Admin panel accessible - Attackers can target admin.php for brute force
Business logic/IP theft - Internal documents and source code exposed
Regulatory violations - GDPR/CCPA non-compliance due to exposed PII
