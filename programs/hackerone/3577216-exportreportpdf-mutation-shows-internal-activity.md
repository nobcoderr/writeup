# `exportReportPdf` mutation shows internal Activity

- Program: HackerOne
- Weakness / temuan: **`exportReportPdf` mutation shows internal Activity**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 92
- Submitted: 2026-02-27
- Disclosed: 2026-07-29
- Report: https://hackerone.com/reports/3577216

## Team summary

A issue was identified in the PDF export path for disclosed reports. When a report was exported to PDF, the export pipeline did not apply the same visibility and authorization scoping that governs the normal report view. As a result, the generated PDF could potentially include timeline content beyond what the requester was authorized to see, such as internal team activity, triage guidance, and internal fields, and reports at a limited disclosure level could potentially be rendered as if fully disclosed.

The root cause was that PDF generation assembled report content from the underlying timeline without re-checking each activity against the requester's permission level, effectively bypassing authorization for that code path rather than the report as a whole.

The issue was validated by our team and fixed promptly by enforcing the same per-activity visibility checks and disclosure-level scoping along the export path, as already applied elsewhere. We have found no evidence of misuse in our investigation to date, and no action is required from users.
