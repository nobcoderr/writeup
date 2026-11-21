# Possible DoS in NumberHelpers

- Program: Ruby on Rails
- Weakness / temuan: **Uncontrolled Resource Consumption**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 18
- Submitted: 2024-10-31
- Disclosed: 2026-10-06
- Report: https://hackerone.com/reports/2814774

## Team summary

Active Support's number helpers accepted strings in scientific notation. `BigDecimal` parses a string such as `"11288E822220222"` into a number with hundreds of trillions of digits, and formatting that number exhausts memory or ties up the CPU. An application that passes user input to `number_to_currency`, `number_to_percentage` or another number helper can be taken down by a single request.

[CVE-2026-33176](https://github.com/rails/rails/security/advisories/GHSA-2j26-frm8-cmj9) fixes this in Active Support 7.2.3.1, 8.0.4.1 and 8.1.2.1. The helpers now treat any string containing `e` or `d` as non-numeric and return it unchanged, as they already did for other non-numeric input.

Thanks to @manun for the report.
