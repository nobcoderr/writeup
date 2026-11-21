# Adding phone number to profile By OTP brute forcing

- Program: CoinMate.io
- Weakness / temuan: **Insecure Storage of Sensitive Information**
- Severity: medium
- State: resolved
- Bounty: $100.00
- Upvotes: 114
- Submitted: 2025-07-23
- Disclosed: 2026-08-08
- Report: https://hackerone.com/reports/3265780

## Writeup

Steps to reproduce the bug :
Step1: In the permanent address enter any phone number, then enter any user phone and verify phone number then it will ask a OTP for phone  number verification.
Step2: So enter any OTP in the OTP filed and intercept the request in the burp-suite, Then send the intercepted request to burp intruder.
Step3: In the burp intruder Brute force the OTP from 100000 to 999999, In this OTP brute force once we send the request with received OTP in the response we will get 961 length So OTP verified .
Step4: Copy that response and paste that first intercepted request response and forward that, Then check phone number added to our account.

## Impact

Using this we can add any user phone number to our account , Then that added phone number will received the OTP's and used to login.

Note : As i received a mail from you to report this bug again i am reporting this bug again so please check and reward me that reward.
