# Missing ownership validation allows cross‑manager tracker–campaign linking

- Program: Revive Adserver
- Weakness / temuan: **Insecure Direct Object Reference (IDOR)**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 22
- Submitted: 2026-06-03
- Disclosed: 2026-06-25
- Report: https://hackerone.com/reports/3780709
- CVE: CVE-2026-50739, CVE-2026-34913

## Team summary

HackerOne community member hakuopi (and independently sy2no, garuthacktvist, and aszh) has reported a bypass of the fix for CVE‑2026‑34913. Proper ownership validation had not been applied to the reverse operation of linking campaigns and trackers through the `tracker-campaigns.php` script in Revive Adserver 6.0.7 and earlier. As a result, a low‑privileged user could link their trackers to campaigns owned by other managers on the same instance, leading to inconsistent ownership relationships.
