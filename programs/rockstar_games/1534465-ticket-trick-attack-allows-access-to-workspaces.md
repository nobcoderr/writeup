# Ticket Trick Attack allows access to ████████' workspaces

- Program: Rockstar Games
- Weakness / temuan: **Improper Access Control - Generic**
- Severity: high
- State: resolved
- Bounty: $0.00
- Upvotes: 66
- Submitted: 2022-04-07
- Disclosed: 2026-09-01
- Report: https://hackerone.com/reports/1534465

## Writeup

████████ does not validate the ownership of an email before allowing access on its support portal . This leads to "ticket trick attack". An attacker can login, signup, and interact as "████████" .
Steps to reproduce :
1. Lets say Rockstar games has an account on website "organisation.com" with email "████████".
2. the website "organisation.com" sends a login link when an email is entered on the login page.
3. The login link is sent from email address "████████"
4. An attacker creates an account on ████████ with email "████████"
5. Attacker logs into ████████ support portal.
6. Attacker goes to "organisation.com" and requests a login link for " ████████" .
7. An email containing login link is sent to "████████" from "████████"
8.This creates a support ticket for "████████".
9. Since the attacker is logged in as "████████" on "████████' support portal he/she can see the contents of the email in "Dashboard" on support portal .
10. The attacker opens the login link and logs in as " ████████" on "organisation.com". 

To demonstrate impact, I have created an account on workspace management site "████████" , the login is done through a link sent on the email but I was able to login as ████████ without owning that email address through exploitation of this vulnerability.

## Impact

An attacker can login/reset passwords for accounts belonging to ████████ on various site leading to unauthorised access and sensitive information disclosure.
