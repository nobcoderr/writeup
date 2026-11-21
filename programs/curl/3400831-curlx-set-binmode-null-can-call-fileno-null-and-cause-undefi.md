# CURLX_SET_BINMODE(NULL) can call fileno(NULL) and cause undefined behavior / crash

- Program: curl
- Weakness / temuan: **CURLX_SET_BINMODE(NULL) can call fileno(NULL) and cause undefined behavior / crash**
- Severity: high
- State: not-applicable
- Bounty: $0.00
- Upvotes: 13
- Submitted: 2025-10-27
- Disclosed: 2025-10-27
- Report: https://hackerone.com/reports/3400831

## Temuan

CURLX_SET_BINMODE(NULL) can call fileno(NULL) and cause undefined behavior / crash

Public writeup body was not in the disclosed JSON; open the report link above.
