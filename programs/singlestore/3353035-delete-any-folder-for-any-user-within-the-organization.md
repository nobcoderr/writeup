# Delete any folder for any user within the organization

- Program: SingleStore
- Weakness / temuan: **Insecure Direct Object Reference (IDOR)**
- Severity: low
- State: resolved
- Bounty: $0.00
- Upvotes: 35
- Submitted: 2025-09-22
- Disclosed: 2026-07-01
- Report: https://hackerone.com/reports/3353035

## Team summary

An IDOR vulnerability in the SingleStore backend API allowed low-privileged users to delete folders belonging to other users within the same organization by manipulating the folder_id parameter in DELETE requests to /public/notebooks/api/contents/<id>/_internal-s2-stage/folder_id/folder_name/ on backend.singlestore.com, bypassing authorization checks that should have verified folder ownership. The vulnerability (CWE-639) was rated CVSS 3.0 Low (3.8) due to high attack complexity requiring knowledge of two UUIDs, reported September 22, 2025, triaged October 2, 2025, and successfully patched by SingleStore on April 21, 2026.
