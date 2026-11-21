# Insufficient checks in the file path parameter allow writing to unauthorized directories

- Program: SingleStore
- Weakness / temuan: **External Control of File Name or Path**
- Severity: low
- State: resolved
- Bounty: $0.00
- Upvotes: 12
- Submitted: 2025-10-15
- Disclosed: 2026-06-24
- Report: https://hackerone.com/reports/3384615

## Team summary

A directory traversal vulnerability was identified in the file upload functionality at backend.singlestore.com. By manipulating the path parameter with `../` sequences (e.g., `../test.csv`) in the `/public?q=UploadGet_ endpoint`, authenticated users could write files to parent directories outside the intended upload location.
The issue was classified as Low severity due to limited impact — file placement manipulation only, with no sensitive data disclosure or critical system file overwrite demonstrated. The vulnerability has been remediated through proper path sanitization.
