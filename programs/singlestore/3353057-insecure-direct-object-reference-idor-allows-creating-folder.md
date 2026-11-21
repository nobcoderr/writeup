# Insecure Direct Object Reference (IDOR) allows creating folders.

- Program: SingleStore
- Weakness / temuan: **Insecure Direct Object Reference (IDOR)**
- Severity: low
- State: resolved
- Bounty: $0.00
- Upvotes: 39
- Submitted: 2025-09-22
- Disclosed: 2026-07-01
- Report: https://hackerone.com/reports/3353057

## Team summary

An Insecure Direct Object Reference (IDOR) vulnerability was discovered in SingleStore's backend API that allowed authenticated users with low privileges to create unauthorized folders and files in other users' workspaces within the same organization. By manipulating the clusterID parameter in POST requests to the /public/notebooks/api/contents/ endpoint at backend.singlestore.com, an attacker could bypass authorization checks and create resources under another user's cluster without proper permission verification. The vulnerability was assigned a CVSS score of 3.8 (Low severity) due to the high attack complexity requiring knowledge of specific cluster UUIDs, though it posed risks including unauthorized resource creation, potential privilege escalation vectors, data integrity issues, and operational disruption. The issue was reported on September 22, 2025, triaged on October 2, 2025, and resolved by April 21, 2026 when the SingleStore security team implemented a patch to properly validate cluster ownership before allowing resource creation.
