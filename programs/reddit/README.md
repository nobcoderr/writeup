# Reddit

Disclosed reports: **72**

| ID | Temuan | Severity | Bounty | Writeup |
| --- | --- | --- | ---: | --- |
| 2967634 | Improper Access Control - Generic | high | $7500 | [Exposed proxy allows to access internal reddit domains](2967634-exposed-proxy-allows-to-access-internal-reddit-domains.md) |
| 1960765 | Server-Side Request Forgery (SSRF) | high | $6000 | [Blind SSRF to internal services in matrix preview_link API](1960765-blind-ssrf-to-internal-services-in-matrix-preview-link-api.md) |
| 1962645 | Cross-site Scripting (XSS) - Generic | high | $5000 | [[accounts.reddit.com] Redirect parameter allows for XSS](1962645-accounts-reddit-com-redirect-parameter-allows-for-xss.md) |
| 1930763 | Cross-site Scripting (XSS) - Stored | high | $5000 | [RichText parser vulnerability in scheduled posts allows XSS](1930763-richtext-parser-vulnerability-in-scheduled-posts-allows-xss.md) |
| 1213237 | Insecure Direct Object Reference (IDOR) | high | $5000 | [Deleting all DMs on RedditGifts.com](1213237-deleting-all-dms-on-redditgifts-com.md) |
| 1551176 | Improper Access Control - Generic | high | $5000 | [Able to bypass email verification and change email to any other user email ](1551176-able-to-bypass-email-verification-and-change-email-to-any-ot.md) |
| 1543159 | Business Logic Errors | high | $5000 | [Able to approve admin approval and change effective status without adding payment details . ](1543159-able-to-approve-admin-approval-and-change-effective-status-w.md) |
| 1549206 | Cross-site Scripting (XSS) - Reflected | high | $5000 | [Reflected xss in https://sh.reddit.com](1549206-reflected-xss-in-https-sh-reddit-com.md) |
| 1658418 | Insecure Direct Object Reference (IDOR) | high | $5000 | [Getting access of mod logs from any public or restricted subreddit with IDOR vulnerability](1658418-getting-access-of-mod-logs-from-any-public-or-restricted-sub.md) |
| 1962951 | Cross-site Scripting (XSS) - Reflected | medium | $500 | [Regression on dest parameter sanitization doesn't check scheme/websafe destinations](1962951-regression-on-dest-parameter-sanitization-doesn-t-check-sche.md) |
| 996041 | Type Confusion | medium | $500 | [Image queue default key of 'None' and GraphQL unhandled type exception](996041-image-queue-default-key-of-none-and-graphql-unhandled-type-e.md) |
| 1213765 | Business Logic Errors | medium | $500 | [IDOR to pay less for coin purchases on oauth.reddit.com via /api/v2/gold/paypal/create_coin_purchase_order in `order_id` parameter ](1213765-idor-to-pay-less-for-coin-purchases-on-oauth-reddit-com-via.md) |
| 1226891 | Improper Access Control - Generic | medium | $500 | [Domain Takeover of Reddit.ru via DNS Hijacking](1226891-domain-takeover-of-reddit-ru-via-dns-hijacking.md) |
| 1606957 | Unrestricted File Upload on reddit.secure.force.com | low | $100 | [Unrestricted File Upload on reddit.secure.force.com](1606957-unrestricted-file-upload-on-reddit-secure-force-com.md) |
| 1543770 | Improper Input Validation | low | $100 | [Moderators can send messages to users from banned subreddits via `oauth.reddit.com/api/mod/conversations`](1543770-moderators-can-send-messages-to-users-from-banned-subreddits.md) |
| 1567186 | Improper Access Control - Generic | critical | $0 | [One-click account hijack for anyone using Apple sign-in with Reddit, due to response-type switch + leaking href to XSS on www.redditmedia.com](1567186-one-click-account-hijack-for-anyone-using-apple-sign-in-with.md) |
| 2353237 | Use of Hard-coded Cryptographic Key | medium | $0 | [Infromation Disclosure To Use of Hard-coded Cryptographic Key](2353237-infromation-disclosure-to-use-of-hard-coded-cryptographic-ke.md) |
| 1504410 | Cross-site Scripting (XSS) - Stored | high | $0 | [XSS via Mod Log Removed Posts](1504410-xss-via-mod-log-removed-posts.md) |
| 1661113 | Insecure Direct Object Reference (IDOR) | high | $0 | [IDOR allows an attacker to modify the links of any user](1661113-idor-allows-an-attacker-to-modify-the-links-of-any-user.md) |
| 1596663 | Improper Access Control - Generic | high | $0 | [Admin can create a hidden admin account  which even the owner can not detect and remove and do administrative actions on the application.](1596663-admin-can-create-a-hidden-admin-account-which-even-the-owner.md) |
| 1051373 | Cross-site Scripting (XSS) - Reflected | high | $0 | [XSS Reflected on reddit.com via url path](1051373-xss-reflected-on-reddit-com-via-url-path.md) |
| 1285598 | Business Logic Errors | high | $0 | [s3 bucket takeover presented in https://github.com/reddit/rpan-studio/blob/e1782332c75ecb2f774343258ff509788feab7ce/CI/full-build-macos.sh](1285598-s3-bucket-takeover-presented-in-https-github-com-reddit-rpan.md) |
| 1656380 | Insecure Direct Object Reference (IDOR) | medium | $0 | [Reddit talk promotion offers don't expire, allowing users to accept them after being demoted](1656380-reddit-talk-promotion-offers-don-t-expire-allowing-users-to.md) |
| 1069039 | Privacy Violation | high | $0 | [GPS metadata preserved when converting HEIF to PNG](1069039-gps-metadata-preserved-when-converting-heif-to-png.md) |
| 1298902 | Improper Access Control - Generic | low | $0 | [Outsider can affect Upvote Percentage of private subreddit post by calling /api/vote API](1298902-outsider-can-affect-upvote-percentage-of-private-subreddit-p.md) |
| 2618486 | Insecure Direct Object Reference (IDOR) | low | $0 | [IDOR lets a malicious user reveal the unpinned achievement badges of any Reddit user](2618486-idor-lets-a-malicious-user-reveal-the-unpinned-achievement-b.md) |
| 1480569 | Cross-Site Request Forgery (CSRF) | medium | $0 | [CSRF (protection bypassed) to force a below 18 user into viewing an nsfw subreddit !](1480569-csrf-protection-bypassed-to-force-a-below-18-user-into-viewi.md) |
| 1341957 | Uncontrolled Resource Consumption | medium | $0 | [Hash-Collision Denial-of-Service Vulnerability in Markdown Parser](1341957-hash-collision-denial-of-service-vulnerability-in-markdown-p.md) |
| 801743 | Time-of-check Time-of-use (TOCTOU) Race Condition | medium | $0 | [Race condition leads to Inflation of coins when bought via Google Play Store at endpoint https://oauth.reddit.com/api/v2/gold/android/verify_purchase ](801743-race-condition-leads-to-inflation-of-coins-when-bought-via-g.md) |
| 1257753 | Open Redirect | medium | $0 | [Open Redirect on www.redditinc.com via `failed` query param](1257753-open-redirect-on-www-redditinc-com-via-failed-query-param.md) |
| 1065186 | Improper Restriction of Authentication Attempts | low | $0 | [Weak rate limit could lead to ATO due to weak password protection mechanisms](1065186-weak-rate-limit-could-lead-to-ato-due-to-weak-password-prote.md) |
| 1237428 | Uncontrolled Resource Consumption | high | $0 | [[dubsmash] Long String in 'shoutout' Parameter Leading Internal server Error on Popular hastags , Community and User Profile](1237428-dubsmash-long-string-in-shoutout-parameter-leading-internal.md) |
| 1122177 | Information Disclosure | medium | $0 | [Third party app could steal access token as well as protected files using inAppBrowser](1122177-third-party-app-could-steal-access-token-as-well-as-protecte.md) |
| 1202408 | Violation of Secure Design Principles | low | $0 | [No Rate Limit on redditgifts gift  when Adding Comment](1202408-no-rate-limit-on-redditgifts-gift-when-adding-comment.md) |
| 1285081 | Open Redirect | medium | $0 | [Open Redirect on www.redditinc.com via `failed` query param bypass after fixed bug #1257753](1285081-open-redirect-on-www-redditinc-com-via-failed-query-param-by.md) |
| 1212374 | Improper Authorization | medium | $0 | [Oauth Misconfiguration Lead To Account Takeover](1212374-oauth-misconfiguration-lead-to-account-takeover.md) |
| 1102365 | Improper Authorization | high | $0 | [[dubmash] Lack of authorization checks - Update Sound Titles](1102365-dubmash-lack-of-authorization-checks-update-sound-titles.md) |
| 1632186 | Insufficient Session Expiration | critical | $0 | [Can use the Reddit android app as usual even though revoking the access of it from reddit.com](1632186-can-use-the-reddit-android-app-as-usual-even-though-revoking.md) |
| 1582778 | Misconfigurated login page able to lock login action for any account without user interaction | critical | $0 | [Misconfigurated login page able to lock login action for any account without user interaction](1582778-misconfigurated-login-page-able-to-lock-login-action-for-any.md) |
| 1165225 | Improper Restriction of Authentication Attempts | low | $0 | [[dubsmash] Username and password bruteforce](1165225-dubsmash-username-and-password-bruteforce.md) |
| 1762927 | Improper Access Control - Generic | medium | $0 | [api keys leaked](1762927-api-keys-leaked.md) |
| 1744264 | Insecure Direct Object Reference (IDOR) | critical | $0 | [ read and message other user's messages](1744264-read-and-message-other-user-s-messages.md) |
| 1170522 | Improper Restriction of Authentication Attempts | medium | $0 | [Missing rate limit in current password change settings leads to Account takeover](1170522-missing-rate-limit-in-current-password-change-settings-leads.md) |
| 1719588 | Remote File Inclusion | critical | $0 | [HTML injection in API response including request url](1719588-html-injection-in-api-response-including-request-url.md) |
| 1815463 | Incorrect Authorization | n/a | $0 | [oauth misconfigration lead to account takeover](1815463-oauth-misconfigration-lead-to-account-takeover.md) |
| 1206004 | Improper Authentication - Generic | medium | $0 | [No rate limit leads to spaming post](1206004-no-rate-limit-leads-to-spaming-post.md) |
| 785833 | Improper Authentication - Generic | low | $0 | [registering with the same email address multiple times leads to account takeover ](785833-registering-with-the-same-email-address-multiple-times-leads.md) |
| 1168804 | Application level DOS at Login Page ( Accepts Long Password ) | high | $0 | [Application level DOS at Login Page ( Accepts Long Password )](1168804-application-level-dos-at-login-page-accepts-long-password.md) |
| 862882 | Cross-site Scripting (XSS) - Stored | medium | $0 | [XSS in redditmedia.com can compromise data of reddit.com](862882-xss-in-redditmedia-com-can-compromise-data-of-reddit-com.md) |
| 1310230 | Open Redirect | medium | $0 | [Open Redirect through POST Request in www.redditinc.com](1310230-open-redirect-through-post-request-in-www-redditinc-com.md) |
| 1187003 | Information Disclosure | high | $0 | [critical file found etc/passwd on www.reddit.com](1187003-critical-file-found-etc-passwd-on-www-reddit-com.md) |
| 1209098 | Cross-site Scripting (XSS) - Generic | none | $0 | [ XSS](1209098-xss.md) |
| 1609004 | Improper Authentication - Generic | low | $0 | [Rate limit is implemented in Reddit , but its not working . ](1609004-rate-limit-is-implemented-in-reddit-but-its-not-working.md) |
| 1195340 | Weak Cryptography for Passwords | critical | $0 | [User Account has been taken out](1195340-user-account-has-been-taken-out.md) |
| 1966262 | Improper Access Control - Generic | medium | $0 | [Huge amount of Subdomains Takeovers at Reddit.com](1966262-huge-amount-of-subdomains-takeovers-at-reddit-com.md) |
| 1165285 | Improper Restriction of Authentication Attempts | low | $0 | [No Rate limit on change password leads to account takeover](1165285-no-rate-limit-on-change-password-leads-to-account-takeover.md) |
| 1241116 | Improper Authentication - Generic | critical | $0 | [hardcoded api secret & api key in com.reddit.frontpage](1241116-hardcoded-api-secret-api-key-in-com-reddit-frontpage.md) |
| 1461207 | Broken links make users from France unable to understand the allowed content policy | none | $0 | [Broken links make users from France unable to understand the allowed content policy](1461207-broken-links-make-users-from-france-unable-to-understand-the.md) |
| 1538157 | Uncontrolled Resource Consumption | medium | $0 | [Regular Expression Denial of Service vulnerability](1538157-regular-expression-denial-of-service-vulnerability.md) |
| 1716249 | Insecure Storage of Sensitive Information | high | $0 | [sensitive data exposure](1716249-sensitive-data-exposure.md) |
| 1167029 | Improper Access Control - Generic | n/a | $0 | [Broken Authendication And Session Management](1167029-broken-authendication-and-session-management.md) |
| 1816181 | Cross-site Scripting (XSS) - Reflected | medium | $0 | [Reflected XSS via File Upload](1816181-reflected-xss-via-file-upload.md) |
| 1276733 | Improper Access Control - Generic | low | $0 | [S3 bucket Upload on studio.redditinc.com (s3-r-w.ap-east-1.amazonaws.com)](1276733-s3-bucket-upload-on-studio-redditinc-com-s3-r-w-ap-east-1-am.md) |
| 1812768 | Cross-site Scripting (XSS) - Reflected | medium | $0 | [CVE-2020-11022](1812768-cve-2020-11022.md) |
| 1350401 | Business Logic Errors | medium | $0 | [Email Verification Bypass And Get access to user's private invitation.](1350401-email-verification-bypass-and-get-access-to-user-s-private-i.md) |
| 1591085 | Several Subdomains Takeover | high | $0 | [Several Subdomains Takeover](1591085-several-subdomains-takeover.md) |
| 1325649 | Phishing | medium | $0 | [com.reddit.frontpage vulernable to Task Hijacking (aka StrandHogg Attack)](1325649-com-reddit-frontpage-vulernable-to-task-hijacking-aka-strand.md) |
| 1182824 | Open Redirect | n/a | $0 | [Vulnerability Name: URL Redirection / Unvalidate Open Redirect](1182824-vulnerability-name-url-redirection-unvalidate-open-redirect.md) |
| 1243009 | Uncontrolled Resource Consumption | none | $0 | [No Password Length Restriction leads to Denial of Service](1243009-no-password-length-restriction-leads-to-denial-of-service.md) |
| 1425884 | No rate limit on password reset leads to email enumeration at  gateway-production.dubsmash.com  | n/a | $0 | [No rate limit on password reset leads to email enumeration at  gateway-production.dubsmash.com ](1425884-no-rate-limit-on-password-reset-leads-to-email-enumeration-a.md) |
| 1166770 | User Interface (UI) Misrepresentation of Critical Information | none | $0 | [Content Spoofing/Text Injection at https://gateway-production.dubsmash.com](1166770-content-spoofing-text-injection-at-https-gateway-production.md) |
| 1165919 | Phishing | low | $0 | [Content Spoofing](1165919-content-spoofing.md) |
