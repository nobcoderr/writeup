# HackerOne disclosed-report corpus

Public disclosed HackerOne reports, indexed by program and weakness.

| Path | Style | Contents |
| --- | --- | --- |
| [`programs/`](programs) | per program | folder per program, one writeup file per disclosed finding |
| [`hackerone-reports/`](hackerone-reports) | reddelexc | `data.csv`, keyword bug-class tops, every public program, every official weakness |
| [`hackerone-bug-bounty-reports/`](hackerone-bug-bounty-reports) | codebygk | `data/reports.json`, indexes by program, weakness, severity, and asset type |

Refresh:

```bash
python3 hackerone-reports/refresh_all.py --by-program
python3 hackerone-reports/build_program_writeups.py
```

Coverage: [hackerone-reports/docs/COVERAGE.md](hackerone-reports/docs/COVERAGE.md)  
Per-program hacktivity audit: [hackerone-reports/docs/HACKTIVITY_AUDIT.md](hackerone-reports/docs/HACKTIVITY_AUDIT.md)
