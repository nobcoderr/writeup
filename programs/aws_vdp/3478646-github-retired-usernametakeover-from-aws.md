# GitHub Retired UsernameTakeover From  [aws/████████]

- Program: AWS VDP
- Weakness / temuan: **Inclusion of Functionality from Untrusted Control Sphere**
- Severity: low
- State: resolved
- Bounty: $0.00
- Upvotes: 48
- Submitted: 2025-12-25
- Disclosed: 2026-08-03
- Report: https://hackerone.com/reports/3478646

## Writeup

#Summary
In one of Github Repository, there is a link to a GitHub repository under the username `████████`, which was unclaimed. I registered the retired username and created a repository with the name PoC. As a result, the original link now points to my controlled Account, enabling a persistent repository hijack.

#Description
I have found a link which was `████████` and it was throwing 404 Not Found , i went on to register the unclaimed (**retired**) username and host PoC Repo with my own content 



#Steps To Reproduce


1. Navigate to: ████████
2. Search For ` ████████`
3. Navigate to this Account  & Open the PoC Reporistory
3. Notice that the repo is taken over and saying `Taken Over By ████████`


#PoC
████████

#Recommendations
All Links assosicated with this retired username should be removed from the repository 

#Reference
* https://hackerone.com/reports/1434967
* https://hackerone.com/reports/1212853

Regards
████████

## Impact

Users accessing the link from Your Official GitHub are serving content from an attacker-controlled repository, breaking the trust model. This allows an attacker to easily convince users to take actions that could be malicious.
