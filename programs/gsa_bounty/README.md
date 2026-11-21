# GSA Bounty

Disclosed reports: **49**

| ID | Temuan | Severity | Bounty | Writeup |
| --- | --- | --- | ---: | --- |
| 311289 | Improper Access Control - Generic | critical | $2000 | [CI for [example.gov] can be logged in and accessible](311289-ci-for-example-gov-can-be-logged-in-and-accessible.md) |
| 726773 | HTTP Request Smuggling | high | $750 | [HTTP Request Smuggling on https://labs.data.gov](726773-http-request-smuggling-on-https-labs-data-gov.md) |
| 303730 | Cross-site Scripting (XSS) - Stored | high | $750 | [Defacement of catalog.data.gov via web cache poisoning to stored DOMXSS](303730-defacement-of-catalog-data-gov-via-web-cache-poisoning-to-st.md) |
| 665651 | Open Redirect | high | $750 | [Stealing Users OAuth Tokens through redirect_uri parameter](665651-stealing-users-oauth-tokens-through-redirect-uri-parameter.md) |
| 895696 | Use of Inherently Dangerous Function | medium | $300 | [Blind SSRF on https://labs.data.gov/dashboard/Campaign/json_status/ Endpoint](895696-blind-ssrf-on-https-labs-data-gov-dashboard-campaign-json-st.md) |
| 895972 | Remote File Inclusion | medium | $300 | [Limited LFI](895972-limited-lfi.md) |
| 272095 | Server-Side Request Forgery (SSRF) | medium | $300 | [SSRF/XSPA in labs.data.gov/dashboard/validate](272095-ssrf-xspa-in-labs-data-gov-dashboard-validate.md) |
| 615840 | Cross-site Scripting (XSS) - Stored | medium | $300 | [Blind Stored XSS In  "Report a Problem" on www.data.gov/issue/](615840-blind-stored-xss-in-report-a-problem-on-www-data-gov-issue.md) |
| 299835 | Open Redirect | low | $150 | [Link poisoning on https://secure.login.gov/ login page](299835-link-poisoning-on-https-secure-login-gov-login-page.md) |
| 514224 | Server-Side Request Forgery (SSRF) | low | $150 | [SSRF in Search.gov via ?url= parameter](514224-ssrf-in-search-gov-via-url-parameter.md) |
| 387007 | Open Redirect | low | $150 | [[idp.fr.cloud.gov] Open Redirect](387007-idp-fr-cloud-gov-open-redirect.md) |
| 798742 | Open Redirect | low | $150 | [open redirect in eb9f.pivcac.prod.login.gov](798742-open-redirect-in-eb9f-pivcac-prod-login-gov.md) |
| 297478 | SQL Injection | critical | $0 | [SQL injection in https://labs.data.gov/dashboard/datagov/csv_to_json via User-agent ](297478-sql-injection-in-https-labs-data-gov-dashboard-datagov-csv-t.md) |
| 268382 | Information Disclosure | high | $0 | [Nginx misconfiguration leading to direct PHP source code download](268382-nginx-misconfiguration-leading-to-direct-php-source-code-dow.md) |
| 263226 | Cross-site Scripting (XSS) - Reflected | medium | $0 | [HTML injection (with XSS possible) on the https://www.data.gov/issue/ using media_url attribute](263226-html-injection-with-xss-possible-on-the-https-www-data-gov-i.md) |
| 263873 | Insufficient Session Expiration | medium | $0 | [Improper Session management can cause account takeover[https://micropurchase.18f.gov]](263873-improper-session-management-can-cause-account-takeover-https.md) |
| 263662 | Cross-Site Request Forgery (CSRF) | medium | $0 | [Cross-Site Request Forgery on the Federalist API (all endpoints), using Flash file on the attacker's host](263662-cross-site-request-forgery-on-the-federalist-api-all-endpoin.md) |
| 265528 | Cross-site Scripting (XSS) - Reflected | medium | $0 | [Reflected XSS on the data.gov (WAF bypass+ Chrome XSS Auditor bypass+ works in all browsers)](265528-reflected-xss-on-the-data-gov-waf-bypass-chrome-xss-auditor.md) |
| 728664 | Violation of Secure Design Principles | high | $0 | [Cache poisoning DoS to various TTS assets](728664-cache-poisoning-dos-to-various-tts-assets.md) |
| 263902 | Violation of Secure Design Principles | high | $0 | [{REDACTED}.data.gov subdomain takeover.](263902-redacted-data-gov-subdomain-takeover.md) |
| 262649 | Information Disclosure | low | $0 | [Information disclosure (system username) in the x-amz-meta-s3cmd-attrs response header on federation.data.gov](262649-information-disclosure-system-username-in-the-x-amz-meta-s3c.md) |
| 245872 | Insecure Direct Object Reference (IDOR) | medium | $0 | [[IDOR] The authenticated user can restart website build or view build logs on any another Federalist account](245872-idor-the-authenticated-user-can-restart-website-build-or-vie.md) |
| 374907 | Information Disclosure | low | $0 | [Root user disclosure in data.gov domain though x-amz-meta-s3cmd-attrs header](374907-root-user-disclosure-in-data-gov-domain-though-x-amz-meta-s3.md) |
| 263542 | Privilege Escalation | high | $0 | [Subdomain take-over of {REDACTED}.18f.gov](263542-subdomain-take-over-of-redacted-18f-gov.md) |
| 515574 | Phishing | low | $0 | [Unclaimed Github Repository Takeover on https://www.data.gov/labs](515574-unclaimed-github-repository-takeover-on-https-www-data-gov-l.md) |
| 317005 | Off-by-one Error | low | $0 | [Subdomain Takeover due to unclaimed domain pointing to AWS](317005-subdomain-takeover-due-to-unclaimed-domain-pointing-to-aws.md) |
| 249319 | Violation of Secure Design Principles | low | $0 | [Race condition on the Federalist API endpoints can lead to the Denial of Service attack](249319-race-condition-on-the-federalist-api-endpoints-can-lead-to-t.md) |
| 245833 | Improper Authentication - Generic | medium | $0 | [The user, who was deleted from Github Organization, still can access all functions of federalist, in case he didn't do logout](245833-the-user-who-was-deleted-from-github-organization-still-can.md) |
| 250688 | Insufficient Session Expiration | low | $0 | [The Federalsit session cookie (federalist.sid) is not properly invalidated - backdoor access to the account is possible](250688-the-federalsit-session-cookie-federalist-sid-is-not-properly.md) |
| 360171 | Multiple Bugs in api.data.gov/signup endpoint leads to send custom messages to Anyone | medium | $0 | [Multiple Bugs in api.data.gov/signup endpoint leads to send custom messages to Anyone](360171-multiple-bugs-in-api-data-gov-signup-endpoint-leads-to-send.md) |
| 245172 | Cross-site Scripting (XSS) - Stored | medium | $0 | [Double Stored Cross-Site scripting in the admin panel](245172-double-stored-cross-site-scripting-in-the-admin-panel.md) |
| 942481 | Information Disclosure | medium | $0 | [Wordpress Users Disclosure (/wp-json/wp/v2/users/) on data.gov](942481-wordpress-users-disclosure-wp-json-wp-v2-users-on-data-gov.md) |
| 384289 | Improper Authentication - Generic | critical | $0 | [Redirect on authorization allows account compromise](384289-redirect-on-authorization-allows-account-compromise.md) |
| 318068 | Use of a Broken or Risky Cryptographic Algorithm | medium | $0 | [SSH server compatible with several vulnerable cryptographic algorithms](318068-ssh-server-compatible-with-several-vulnerable-cryptographic.md) |
| 942629 | Denial of service via cache poisoning on https://www.data.gov/ | high | $0 | [Denial of service via cache poisoning on https://www.data.gov/](942629-denial-of-service-via-cache-poisoning-on-https-www-data-gov.md) |
| 264090 | Improper Access Control - Generic | medium | $0 | [2FA bypass - confirmation tokens don't expire](264090-2fa-bypass-confirmation-tokens-don-t-expire.md) |
| 673384 | Improper Access Control - Generic | medium | $0 | [xmlrpc.php file enabled - data.gov](673384-xmlrpc-php-file-enabled-data-gov.md) |
| 263913 | Code Injection | n/a | $0 | [Content injection via URL parameter.](263913-content-injection-via-url-parameter.md) |
| 263498 | Cross-Site Request Forgery (CSRF) | medium | $0 | [CSRF to change Account Security Keys on secure.login.gov](263498-csrf-to-change-account-security-keys-on-secure-login-gov.md) |
| 263736 | Violation of Secure Design Principles | none | $0 | [Email Spoofing - SPF record set to Neutral](263736-email-spoofing-spf-record-set-to-neutral.md) |
| 289051 | Privilege Escalation | high | $0 | [Subdomain Takeover](289051-subdomain-takeover.md) |
| 268679 | Violation of Secure Design Principles | none | $0 | [Homo graphs attack ](268679-homo-graphs-attack.md) |
| 266449 | Improper Authentication - Generic | none | $0 | [[api.data.gov] Leak Valid API With out Verification -](266449-api-data-gov-leak-valid-api-with-out-verification.md) |
| 263508 | Improper Authentication - Generic | none | $0 | [Server Side Misconfiguration (EMAIL SPOOFING) ](263508-server-side-misconfiguration-email-spoofing.md) |
| 667032 | Information Disclosure | low | $0 | [Information disclosure (system username, server info) in the x-amz-meta-s3cmd-attrs response header on data.gov](667032-information-disclosure-system-username-server-info-in-the-x.md) |
| 263512 | Cross-Site Request Forgery (CSRF) | medium | $0 | [CSRF in generating a new Personal Key](263512-csrf-in-generating-a-new-personal-key.md) |
| 263553 | Man-in-the-Middle | medium | $0 | [federalist.18f.gov vulnerable to Sweet32 attack](263553-federalist-18f-gov-vulnerable-to-sweet32-attack.md) |
| 263733 | Violation of Secure Design Principles | none | $0 | [Email Spoofing - SPF record set to Neutral](263733-email-spoofing-spf-record-set-to-neutral.md) |
| 263866 | Error Page Content Spoofing or Text Injection | n/a | $0 | [Error Page Content Spoofing or Text Injection](263866-error-page-content-spoofing-or-text-injection.md) |
