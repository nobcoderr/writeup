# [Splatoon 3] Kick other players with NplnLogin message

- Program: Nintendo
- Weakness / temuan: **Improper Access Control - Generic**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 37
- Submitted: 2026-06-20
- Disclosed: 2026-07-02
- Report: https://hackerone.com/reports/3813932

## Team summary

-

## Researcher summary

In Splatoon 3, a special "NplnLogin" message exists that is designed to prevent one account from going online in Splatoon 3 on multiple consoles at once. Under normal circumstances, this message is only ever sent to your own NPLN user ID, and you would only encounter a communication error from it if you connected online in the game on multiple consoles using the same account. Due to an oversight in server-side message validation, it was possible to send forged "NplnLogin" messages to other users, causing those users to disconnect from NPLN and receive a communication error. It was also possible to send these forged messages to specific Pools, causing anyone who is currently online and has joined the Pool to receive a communication error. These messages could also be repeated rapidly to cause affected users or Pools to receive a communication error while reconnecting or shortly after reconnecting, effectively making it impossible for them to play the game online until the messages stopped being sent. This vulnerability was patched by Nintendo by adding server-side validation to reject "NplnLogin" messages to Pools and to NPLN user IDs that are not your own.
