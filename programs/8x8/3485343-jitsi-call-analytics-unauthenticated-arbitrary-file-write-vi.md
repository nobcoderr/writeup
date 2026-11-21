# jitsi-call-analytics: Unauthenticated arbitrary file write via path traversal in `/api/v1/uploads/analyze`

- Program: 8x8
- Weakness / temuan: **Path Traversal**
- Severity: low
- State: resolved
- Bounty: $100.00
- Upvotes: 68
- Submitted: 2026-01-03
- Disclosed: 2026-07-02
- Report: https://hackerone.com/reports/3485343

## Team summary

The jitsi-call-analytics backend contained a path traversal vulnerability in the `/api/v1/uploads/analyze` endpoint that allowed unauthenticated users to write files within the configured `RTCSTATS_DOWNLOADS_PATH` directory. The upload handler used user-controlled `file.originalname` directly in `path.join()` without sanitization, enabling attackers to include `../` sequences to escape the intended per-session UUID directory and write or overwrite files anywhere under the configured root path.

Changes:
* fix(security) Prevent path traversal in file upload handler.
  * https://github.com/jitsi/jitsi-call-analytics/pull/56

The fix has been deployed to production instances.

We thank @r1skr1der for submitting this report to us.
