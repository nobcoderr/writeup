# Image upload reaches TIFF/JPEG heap overwrite (potential RCE)

- Program: Basecamp
- Weakness / temuan: **Heap Overflow**
- Severity: critical
- State: resolved
- Bounty: $0.00
- Upvotes: 42
- Submitted: 2026-08-14
- Disclosed: 2026-11-17
- Report: https://hackerone.com/reports/3938691
- Asset type: URL

## Team summary

The report describes a critical heap buffer overflow vulnerability in the libvips image processing library used by Basecamp. The analysis found that a mismatch between the TIFF container component count (1 byte/pixel) and the embedded JPEG output (2 bytes/pixel) leads to a deterministic heap buffer overwrite. The researcher provided clear reproduction steps, multiple proof-of-concept files, and demonstrated the potential for remote code execution through control-flow hijacking.
