# connect.8x8.com: Automation Builder - Input Validation Issue in Workflow Step Outputs

- Program: 8x8
- Weakness / temuan: **External Control of Critical State Data**
- Severity: high
- State: resolved
- Bounty: $1337.00
- Upvotes: 36
- Submitted: 2026-07-12
- Disclosed: 2026-09-02
- Report: https://hackerone.com/reports/3858504

## Team summary

@kyotozzx reported an input validation issue in the 8x8 Connect Automation Builder's API where workflow step output field names were not validated against reserved context variable names.
The issue was quickly addressed by implementing validation to reject reserved field names at workflow creation.

We thank @kyotozzx for submitting this report to us.
