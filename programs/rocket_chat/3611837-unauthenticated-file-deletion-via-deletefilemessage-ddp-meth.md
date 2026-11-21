# Unauthenticated file deletion via deleteFileMessage DDP method allows permanent destruction of any uploaded file

- Program: Rocket.Chat
- Weakness / temuan: **Improper Authentication - Generic**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 34
- Submitted: 2026-03-17
- Disclosed: 2026-06-16
- Report: https://hackerone.com/reports/3611837
- CVE: CVE-2026-48929

## Team summary

The deleteFileMessage Meteor method permanently deletes any uploaded file by ID without requiring authentication. When called via an unauthenticated DDP WebSocket connection, Meteor.userId() returns null, causing the authorization check to be skipped. Execution falls through to FileUpload.getStore('Uploads').deleteById(fileID), which removes the file from storage and database unconditionally. File IDs are discoverable from public channel message payloads and download URLs.
