# IDOR allows user to access report details via reference.json endpoint

- Program: HackerOne
- Weakness / temuan: **Insecure Direct Object Reference (IDOR)**
- Severity: critical
- State: resolved
- Bounty: $15000.00
- Upvotes: 372
- Submitted: 2026-07-14
- Disclosed: 2026-10-01
- Report: https://hackerone.com/reports/3862641

## Team summary

**Summary:**
An information disclosure vulnerability on the `/reports/{id}/reference.json` endpoint allowed VDP accounts created via `hackerone.com/vdp-sign-up` to access certain private report details. While the endpoint returned HTTP 422 "You do not have the appropriate access," the error response contained additional report details in the `context.subject` field.

**Description:**
By sending a POST request to the `/reports/{report_id}/reference.json` endpoint with an empty JSON body `{}`, VDP users could retrieve information about private reports belonging to other programs despite receiving an access-denied error. Although the endpoint correctly rejected unauthorized access with an HTTP 422 status code, it inadvertently included private report data in the error response body.

**Steps To Reproduce:**

1. Create a VDP account at `hackerone.com/vdp-sign-up`
2. Log in with the VDP account
3. Obtain an approved test report ID from https://hackerone.com/security?type=team (these reports contain flags to include in your POC), 
4. Send a POST request to `https://hackerone.com/reports/[TEST_REPORT_ID]/reference.json` with the following structure:

```
POST /reports/[TEST_REPORT_ID]/reference.json HTTP/2
Host: hackerone.com
Cookie: [your session cookie]
Content-Type: application/json
X-Csrf-Token: [your CSRF token]
Content-Length: 2

{}
```

4. Observe that despite receiving HTTP 422 with "You do not have the appropriate access," the response contains report details in the `context.subject` field

**Note:** This vulnerability has been fixed. We have found no evidence of misuse in our investigation to date, and no action is required from users..
