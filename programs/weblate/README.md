# Weblate

Disclosed reports: **164**

| ID | Temuan | Severity | Bounty | Writeup |
| --- | --- | --- | ---: | --- |
| 3869124 | Insecure Direct Object Reference (IDOR) | high | $0 | [**Unauthenticated IDOR allows modification of payment customer billing information**](3869124-unauthenticated-idor-allows-modification-of-payment-customer.md) |
| 3179850 | Privacy Violation | n/a | $0 | [exposure of personal IP address via email.](3179850-exposure-of-personal-ip-address-via-email.md) |
| 4081135 | Privilege Escalation | critical | $0 | [Privilege escalation via unfiltered role restoration in project backup import](4081135-privilege-escalation-via-unfiltered-role-restoration-in-proj.md) |
| 3887969 | Server-Side Request Forgery (SSRF) | high | $0 | [SSRF via URL Parser Differential in `normalize_request_url` (wlc)](3887969-ssrf-via-url-parser-differential-in-normalize-request-url-wl.md) |
| 1004536 | Reliance on Cookies without Validation and Integrity Checking in a Security Decision | medium | $0 | [Reset password cookie leads to account takeover](1004536-reset-password-cookie-leads-to-account-takeover.md) |
| 3874004 | OS Command Injection | high | $0 | [ Incomplete fix for CVE-2022-23915: Mercurial argument injection in HgRepository.get_file() leads to command execution](3874004-incomplete-fix-for-cve-2022-23915-mercurial-argument-injecti.md) |
| 3518571 | Argument Injection in /manage/ssh/ via host parameter leads to sensitive file disclosure on Weblate | n/a | $0 | [Argument Injection in /manage/ssh/ via host parameter leads to sensitive file disclosure on Weblate](3518571-argument-injection-in-manage-ssh-via-host-parameter-leads-to.md) |
| 4059744 | Uncontrolled Resource Consumption | medium | $0 | [Anonymous API Rate Limit Bypass via X-Forwarded-For](4059744-anonymous-api-rate-limit-bypass-via-x-forwarded-for.md) |
| 3898281 | Uncontrolled Resource Consumption | high | $0 | [Unauthenticated ?q= search query causes exponential pyparsing backtracking under a process-global lock in Weblate](3898281-unauthenticated-q-search-query-causes-exponential-pyparsing.md) |
| 4094236 | XML Entity Expansion | medium | $0 | [ Billion laughs entity expansion in Qt .ts discovery: a crafted ~950 KB file forces ~55 MB of XML expansion per parse, cost scales with crafted file c](4094236-billion-laughs-entity-expansion-in-qt-ts-discovery-a-crafted.md) |
| 1971589 | Cross-Site Request Forgery (CSRF) | n/a | $0 | [CSRF with logout action](1971589-csrf-with-logout-action.md) |
| 236398 | Violation of Secure Design Principles | n/a | $0 | [no captcha for register user and weak question attacker can spam email](236398-no-captcha-for-register-user-and-weak-question-attacker-can.md) |
| 3825141 | Information Disclosure | medium | $0 | [API token sent to URL dictated by an untrusted project .weblate file](3825141-api-token-sent-to-url-dictated-by-an-untrusted-project-webla.md) |
| 4117330 | Information Disclosure | low | $0 | [Anonymous Translation Suggestion IP Address Exposure Through Change API](4117330-anonymous-translation-suggestion-ip-address-exposure-through.md) |
| 4028616 | Uncontrolled Resource Consumption | medium | $0 | [Memory exhaustion (DoS) via unbounded file read in `EncodingDiscovery.detect_encoding()`](4028616-memory-exhaustion-dos-via-unbounded-file-read-in-encodingdis.md) |
| 942146 | Cleartext Storage of Sensitive Information | none | $0 | [Open Github Repo Leaking WEBLATE SECRET KEY](942146-open-github-repo-leaking-weblate-secret-key.md) |
| 4037976 | Path Traversal | medium | $0 | [Incomplete VCS metadata exclusion: `.svn` / `.bzr` bypass CVE-2026-61792 due to missing `VCS_METADATA_DIRS` entries.](4037976-incomplete-vcs-metadata-exclusion-svn-bzr-bypass-cve-2026-61.md) |
| 1087188 | Business Logic Errors | low | $0 | [Race Condition allows to get more free trials and get more than 100 languages and strings for free](1087188-race-condition-allows-to-get-more-free-trials-and-get-more-t.md) |
| 634312 | Information Disclosure | medium | $0 | [HTML injection and information disclosure in support panel](634312-html-injection-and-information-disclosure-in-support-panel.md) |
| 400826 | Broken Authentication – Session Token bug | none | $0 | [Broken Authentication – Session Token bug](400826-broken-authentication-session-token-bug.md) |
| 232614 | XML External Entities (XXE) | high | $0 | [Uploaded XLF files result in External Entity Execution](232614-uploaded-xlf-files-result-in-external-entity-execution.md) |
| 224460 | Improper Authentication - Generic | medium | $0 | [Rate Limit Bypass on login Page](224460-rate-limit-bypass-on-login-page.md) |
| 4105212 | Uncontrolled Resource Consumption | medium | $0 | [CPU Exhaustion via Crafted TOML Files in translation-finder](4105212-cpu-exhaustion-via-crafted-toml-files-in-translation-finder.md) |
| 4022462 | Uncontrolled Resource Consumption | low | $0 | [Uncaught RecursionError crash in translation-finder (deep directory tree DoS)](4022462-uncaught-recursionerror-crash-in-translation-finder-deep-dir.md) |
| 229532 | Violation of Secure Design Principles | low | $0 | [Insecure Account Removal #2](229532-insecure-account-removal-2.md) |
| 4040149 | Information Exposure Through an Error Message | low | $0 | [wlc: Project-wide download fails part-way and leaves stale archives on disk; filesystem errors surface as raw Python tracebacks.](4040149-wlc-project-wide-download-fails-part-way-and-leaves-stale-ar.md) |
| 4088592 | Uncontrolled Resource Consumption | medium | $0 | [CPU-based Denial of Service in translation-finder via O(N²) per-result wildcard mask matching](4088592-cpu-based-denial-of-service-in-translation-finder-via-o-n-pe.md) |
| 1723445 | Business Logic Errors | none | $0 | [No rate limiting for Remove Account lead to huge Mass mailings](1723445-no-rate-limiting-for-remove-account-lead-to-huge-mass-mailin.md) |
| 253926 | Improper Authentication - Generic | none | $0 | [DKIM records not present, Email Hijacking is possible.....](253926-dkim-records-not-present-email-hijacking-is-possible.md) |
| 229920 | Violation of Secure Design Principles | low | $0 | [Password Restriction](229920-password-restriction.md) |
| 4044441 | Use of Externally-Controlled Format String | low | $0 | [Translation discovery crashes on crafted filenames (regex substitution injection)](4044441-translation-discovery-crashes-on-crafted-filenames-regex-sub.md) |
| 610219 | Cross-site Scripting (XSS) - Stored | medium | $0 | [Stored XSS via Create Project (Add new translation project)](610219-stored-xss-via-create-project-add-new-translation-project.md) |
| 481654 | Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition') | low | $0 | [No Rate On Add Suggest](481654-no-rate-on-add-suggest.md) |
| 404035 | Violation of Secure Design Principles | low | $0 | [flood of comment no rate  limit on commnets >>  by using different user agent ](404035-flood-of-comment-no-rate-limit-on-commnets-by-using-differen.md) |
| 282772 | Business Logic Errors | low | $0 | [no notification send to victim if attacker hacks/accesses his victims WebLate account.](282772-no-notification-send-to-victim-if-attacker-hacks-accesses-hi.md) |
| 229528 | Cross-Site Request Forgery (CSRF) | medium | $0 | [Login CSRF : Login Authentication Flaw](229528-login-csrf-login-authentication-flaw.md) |
| 225653 | Cross-Site Request Forgery (CSRF) | high | $0 | [Account Takeover using Third party Auth CSRF](225653-account-takeover-using-third-party-auth-csrf.md) |
| 1971610 | Logging in without knowing credentials after logged out action | n/a | $0 | [Logging in without knowing credentials after logged out action](1971610-logging-in-without-knowing-credentials-after-logged-out-acti.md) |
| 224572 | Weak password policy | low | $0 | [Weak password policy](224572-weak-password-policy.md) |
| 229825 | Improper Restriction of Authentication Attempts | low | $0 | [Rate Limit Issue on hosted.weblate.org](229825-rate-limit-issue-on-hosted-weblate-org.md) |
| 223461 | Violation of Secure Design Principles | low | $0 | [Weak e-mail change functionality could lead to account takeover](223461-weak-e-mail-change-functionality-could-lead-to-account-takeo.md) |
| 223430 | Violation of Secure Design Principles | low | $0 | [Content Spoofing](223430-content-spoofing.md) |
| 1238749 | Improper Restriction of Authentication Attempts | n/a | $0 | [No rate Limit on Add new Translation Project ](1238749-no-rate-limit-on-add-new-translation-project.md) |
| 225901 | Violation of Secure Design Principles | none | $0 | [Missing filteration of meta characters in full name field on registration page https://demo.weblate.org/accounts/register](225901-missing-filteration-of-meta-characters-in-full-name-field-on.md) |
| 223339 | Cross-Site Request Forgery (CSRF) | medium | $0 | [Activation tokens are not expiring](223339-activation-tokens-are-not-expiring.md) |
| 223355 | Violation of Secure Design Principles | low | $0 | [Insecure Account Removal](223355-insecure-account-removal.md) |
| 1927499 | Use of Hard-coded Credentials | low | $0 | [Testing flow includes a DeepSource secret](1927499-testing-flow-includes-a-deepsource-secret.md) |
| 245304 | Business Logic Errors | n/a | $0 | [Running 2 accounts with a single email #3](245304-running-2-accounts-with-a-single-email-3.md) |
| 245450 | Business Logic Errors | n/a | $0 | [Reset password more than once with a reset link #2](245450-reset-password-more-than-once-with-a-reset-link-2.md) |
| 257376 | Memory Corruption - Generic | none | $0 | [Missing Restriction On String Size](257376-missing-restriction-on-string-size.md) |
| 243594 | Business Logic Errors | n/a | $0 | [Reset password more than once with a reset link](243594-reset-password-more-than-once-with-a-reset-link.md) |
| 224362 | Invalidate session after password reset - hosted website | low | $0 | [Invalidate session after password reset - hosted website](224362-invalidate-session-after-password-reset-hosted-website.md) |
| 229511 | Memory Corruption - Generic | low | $0 | [No Rate Limiting at /contact](229511-no-rate-limiting-at-contact.md) |
| 223337 | Improper Restriction of Authentication Attempts | medium | $0 | [No BruteForce Protection](223337-no-bruteforce-protection.md) |
| 223324 | Violation of Secure Design Principles | medium | $0 | [Registration captcha bypass](223324-registration-captcha-bypass.md) |
| 223854 | Uncontrolled Resource Consumption | low | $0 | [No Password Length Restriction leads to Denial of Service](223854-no-password-length-restriction-leads-to-denial-of-service.md) |
| 223434 | Improper Access Control - Generic | high | $0 | [Improper access control when an added email address is deleted from authentication](223434-improper-access-control-when-an-added-email-address-is-delet.md) |
| 472391 | Cross-site Scripting (XSS) - Stored | medium | $0 | [Stored XSS @ /engage/<project_slug>](472391-stored-xss-engage-project-slug.md) |
| 400781 | Information Disclosure | n/a | $0 | [Browser Self XSS Protection not implemented](400781-browser-self-xss-protection-not-implemented.md) |
| 241608 | Business Logic Errors | n/a | $0 | [Running 2 accounts with a single email [Part 2]](241608-running-2-accounts-with-a-single-email-part-2.md) |
| 244287 | Password token validation in Weblate Bypass #2 | n/a | $0 | [Password token validation in Weblate Bypass #2](244287-password-token-validation-in-weblate-bypass-2.md) |
| 230648 | Weblate |Security Misconfiguration| Method Enumeration Possible on domain  | none | $0 | [Weblate \|Security Misconfiguration\| Method Enumeration Possible on domain ](230648-weblate-security-misconfiguration-method-enumeration-possibl.md) |
| 230076 | Improper Authentication - Generic | low | $0 | [Takeover of an account via reset password options after removing the account](230076-takeover-of-an-account-via-reset-password-options-after-remo.md) |
| 229541 | Violation of Secure Design Principles | n/a | $0 | [Captcha Bypass at Email Reset can lead to Spamming users.](229541-captcha-bypass-at-email-reset-can-lead-to-spamming-users.md) |
| 229620 | Information Disclosure | low | $0 | [Information Disclosure on demo.weblate.org](229620-information-disclosure-on-demo-weblate-org.md) |
| 229417 | Improper Access Control - Generic | n/a | $0 | [Design Flaw in session management of password reset ](229417-design-flaw-in-session-management-of-password-reset.md) |
| 224072 | Business Logic Errors | none | $0 | [Running 2 accounts with a single email](224072-running-2-accounts-with-a-single-email.md) |
| 223454 | Memory Corruption - Generic | low | $0 | [Missing restriction on string size of Full Name at https://demo.weblate.org/accounts/register/](223454-missing-restriction-on-string-size-of-full-name-at-https-dem.md) |
| 223333 | Cross-Site Request Forgery (CSRF) | low | $0 | [CSRF : Reset API ](223333-csrf-reset-api.md) |
| 223344 | OS Command Injection | low | $0 | [CSV Injection with the CSV export feature](223344-csv-injection-with-the-csv-export-feature.md) |
| 223329 | Cross-Site Request Forgery (CSRF) | low | $0 | [Logout CSRF](223329-logout-csrf.md) |
| 225100 | Cross-Site Request Forgery (CSRF) | medium | $0 | [CSRF to Connect third party Account](225100-csrf-to-connect-third-party-account.md) |
| 926093 | Information Disclosure | none | $0 | [Secret_key in GitHub](926093-secret-key-in-github.md) |
| 404713 | Violation of Secure Design Principles | low | $0 | [2nd issue>>> flood of email  no rate limit on delete account confirmation email >> ](404713-2nd-issue-flood-of-email-no-rate-limit-on-delete-account-con.md) |
| 264934 |  Application allowing old password to be set as new password | hosted.weblate.org | n/a | $0 | [ Application allowing old password to be set as new password \| hosted.weblate.org](264934-application-allowing-old-password-to-be-set-as-new-password.md) |
| 241598 | Full Name Overwrite on Third party login | n/a | $0 | [Full Name Overwrite on Third party login](241598-full-name-overwrite-on-third-party-login.md) |
| 241623 | Business Logic Errors | n/a | $0 | [Persistence of Third Party Association.](241623-persistence-of-third-party-association.md) |
| 243635 | Improper validation of unicode characters #3 | n/a | $0 | [Improper validation of unicode characters #3](243635-improper-validation-of-unicode-characters-3.md) |
| 229577 | Old password can be new password | low | $0 | [Old password can be new password](229577-old-password-can-be-new-password.md) |
| 223435 | Cryptographic Issues - Generic | n/a | $0 | [Open SMTP port can let anyone send email from mail.chihar.com](223435-open-smtp-port-can-let-anyone-send-email-from-mail-chihar-co.md) |
| 223374 | You can simply just use passwords that simply are as 123456 | low | $0 | [You can simply just use passwords that simply are as 123456](223374-you-can-simply-just-use-passwords-that-simply-are-as-123456.md) |
| 223999 | Command Injection - Generic | medium | $0 | [CSV export filter bypass leads to formula injection.](223999-csv-export-filter-bypass-leads-to-formula-injection.md) |
| 223427 | Improper Authentication - Generic | low | $0 | [Login using disconnected google account i.e login using old email id](223427-login-using-disconnected-google-account-i-e-login-using-old.md) |
| 223637 | [hosted.weblate.org]Account Takeover | low | $0 | [[hosted.weblate.org]Account Takeover](223637-hosted-weblate-org-account-takeover.md) |
| 223694 | No Rate Limitting at Change Password | medium | $0 | [No Rate Limitting at Change Password](223694-no-rate-limitting-at-change-password.md) |
| 1003468 | Cross-Site Request Forgery (CSRF) | low | $0 | [Send Empty CSRF leads to log out user on [https://hosted.weblate.org/accounts/profile]](1003468-send-empty-csrf-leads-to-log-out-user-on-https-hosted-weblat.md) |
| 479021 | Business Logic Errors | low | $0 | [No Rate Limit  On Add new word](479021-no-rate-limit-on-add-new-word.md) |
| 223421 | Information Disclosure | low | $0 | [Open port leads to information disclosure](223421-open-port-leads-to-information-disclosure.md) |
| 403891 | Tab nabbing via window.opener | n/a | $0 | [Tab nabbing via window.opener](403891-tab-nabbing-via-window-opener.md) |
| 265987 | Improper Access Control - Generic | n/a | $0 | [Add another email address without verification](265987-add-another-email-address-without-verification.md) |
| 232306 | Improper Cookie expiration | Cookies Expiration Set to Future  | low | $0 | [Improper Cookie expiration \| Cookies Expiration Set to Future ](232306-improper-cookie-expiration-cookies-expiration-set-to-future.md) |
| 243619 | No Rate Limitation on Regenerate Api Key | n/a | $0 | [No Rate Limitation on Regenerate Api Key](243619-no-rate-limitation-on-regenerate-api-key.md) |
| 243842 | Improper Authentication - Generic | none | $0 | [Password token validation in Weblate Bypass](243842-password-token-validation-in-weblate-bypass.md) |
| 243611 | Improper validation of unicode characters still not fixed #2 | n/a | $0 | [Improper validation of unicode characters still not fixed #2](243611-improper-validation-of-unicode-characters-still-not-fixed-2.md) |
| 241596 | Improper validation of unicode characters still not fixed | n/a | $0 | [Improper validation of unicode characters still not fixed](241596-improper-validation-of-unicode-characters-still-not-fixed.md) |
| 242171 | Violation of Secure Design Principles | n/a | $0 | [Improper validation of unicode characters](242171-improper-validation-of-unicode-characters.md) |
| 229405 | Cross-Site Request Forgery (CSRF) | low | $0 | [Csrf in watch-unwatch projects](229405-csrf-in-watch-unwatch-projects.md) |
| 243609 | Business Logic Errors | none | $0 | [The username of an account can be ..](243609-the-username-of-an-account-can-be.md) |
| 238117 | Open Redirect | n/a | $0 | [Open redirect while disconnecting Email](238117-open-redirect-while-disconnecting-email.md) |
| 224317 | Open Redirect | medium | $0 | [Open redirect while disconnecting authenticated account](224317-open-redirect-while-disconnecting-authenticated-account.md) |
| 223391 | Clickjacking docs.weblate.org | low | $0 | [Clickjacking docs.weblate.org](223391-clickjacking-docs-weblate-org.md) |
| 229796 | Missing restriction on string size | low | $0 | [Missing restriction on string size](229796-missing-restriction-on-string-size.md) |
| 229735 | Cross-site Scripting (XSS) - Generic | none | $0 | [Self-XSS can be achieved in the editor link using filter bypass](229735-self-xss-can-be-achieved-in-the-editor-link-using-filter-byp.md) |
| 230194 | Violation of Secure Design Principles | none | $0 | [Option method enabled](230194-option-method-enabled.md) |
| 223846 | Improper Access Control - Generic | none | $0 | [Access to completion page without performing any action](223846-access-to-completion-page-without-performing-any-action.md) |
| 223345 | Cross-Site Request Forgery (CSRF) | medium | $0 | [CSRF : Lock and Unlock Translation](223345-csrf-lock-and-unlock-translation.md) |
| 224379 | session id missing secure flag - Hosted Website | low | $0 | [session id missing secure flag - Hosted Website](224379-session-id-missing-secure-flag-hosted-website.md) |
| 223525 | Violation of Secure Design Principles | low | $0 | [Spamming any user from Reset Password Function](223525-spamming-any-user-from-reset-password-function.md) |
| 223326 | Open Redirect | medium | $0 | [Open Redirect via "next" parameter in third-party authentication](223326-open-redirect-via-next-parameter-in-third-party-authenticati.md) |
| 223350 | Cryptographic Issues - Generic | low | $0 | [Web server is vulnerable to Beast Attack](223350-web-server-is-vulnerable-to-beast-attack.md) |
| 296632 | Improper Neutralization of HTTP Headers for Scripting Syntax | none | $0 | [Audit log validation](296632-audit-log-validation.md) |
| 275303 |  Account Restore / Reactivating an old email via old reset link | n/a | $0 | [ Account Restore / Reactivating an old email via old reset link](275303-account-restore-reactivating-an-old-email-via-old-reset-link.md) |
| 278718 | Improper validation of unicode characters  | none | $0 | [Improper validation of unicode characters ](278718-improper-validation-of-unicode-characters.md) |
| 245518 | Violation of Secure Design Principles | low | $0 | [[debian.weblate.org]-Missing SPF Record](245518-debian-weblate-org-missing-spf-record.md) |
| 243616 | Previous password could set as new password | n/a | $0 | [Previous password could set as new password](243616-previous-password-could-set-as-new-password.md) |
| 243664 | Business Logic Errors | none | $0 | [Error Message When Changing Username](243664-error-message-when-changing-username.md) |
| 242945 | Violation of Secure Design Principles | none | $0 | [No filteration of null characters in name field](242945-no-filteration-of-null-characters-in-name-field.md) |
| 224342 | Uncontrolled Resource Consumption | medium | $0 | [Bypassing captcha in registration on Hosted site](224342-bypassing-captcha-in-registration-on-hosted-site.md) |
| 229483 | Improper validation of unicode characters | n/a | $0 | [Improper validation of unicode characters](229483-improper-validation-of-unicode-characters.md) |
| 223475 | Improper Authentication - Generic | low | $0 | [Existing sessions valid after removing third party auth](223475-existing-sessions-valid-after-removing-third-party-auth.md) |
| 230633 | Weblate- Banner Grabbing-Ngnix Server version | n/a | $0 | [Weblate- Banner Grabbing-Ngnix Server version](230633-weblate-banner-grabbing-ngnix-server-version.md) |
| 230863 | Cross-Site Request Forgery (CSRF) | medium | $0 | [CSRF bypass ( Delate Source Translation From dictionaries ) in demo.weblate.org](230863-csrf-bypass-delate-source-translation-from-dictionaries-in-d.md) |
| 232994 | Improper Access Control - Generic | low | $0 | [API Does Not Apply Access Controls to Translations](232994-api-does-not-apply-access-controls-to-translations.md) |
| 229909 | No notificatoin sent on email after account deletion. | n/a | $0 | [No notificatoin sent on email after account deletion.](229909-no-notificatoin-sent-on-email-after-account-deletion.md) |
| 223531 | User Enumeration when adding email to account | low | $0 | [User Enumeration when adding email to account](223531-user-enumeration-when-adding-email-to-account.md) |
| 223456 | Violation of Secure Design Principles | low | $0 | [Content Spoofing in error message](223456-content-spoofing-in-error-message.md) |
| 223327 | Insufficient Session Expiration | low | $0 | [No expiration of session ID after Password change](223327-no-expiration-of-session-id-after-password-change.md) |
| 223545 | Missing DMARC on weblate.org | low | $0 | [Missing DMARC on weblate.org](223545-missing-dmarc-on-weblate-org.md) |
| 223542 | Abuse of Api that causes spamming users and possible DOS due to missing rate limit on contact form | none | $0 | [Abuse of Api that causes spamming users and possible DOS due to missing rate limit on contact form](223542-abuse-of-api-that-causes-spamming-users-and-possible-dos-due.md) |
| 223331 | Cross-site Scripting (XSS) - Stored | low | $0 | [[demo.weblate.org] Stored Self-XSS via Editor Link in Profile](223331-demo-weblate-org-stored-self-xss-via-editor-link-in-profile.md) |
| 224291 | Command Injection - Generic | low | $0 | [CSV Injection with the CVS export feature - Glossary](224291-csv-injection-with-the-cvs-export-feature-glossary.md) |
| 223630 | Content Spoofing | low | $0 | [Content Spoofing](223630-content-spoofing.md) |
| 224287 | Man-in-the-Middle | low | $0 | [Email verification over an unencrypted channel](224287-email-verification-over-an-unencrypted-channel.md) |
| 1454552 | hosted.weblate.org display of unfiltered results | none | $0 | [hosted.weblate.org display of unfiltered results](1454552-hosted-weblate-org-display-of-unfiltered-results.md) |
| 279945 | Improper validation of unicode characters#2 | none | $0 | [Improper validation of unicode characters#2](279945-improper-validation-of-unicode-characters-2.md) |
| 229584 | Captcha bypass at registration | low | $0 | [Captcha bypass at registration](229584-captcha-bypass-at-registration.md) |
| 229869 | Adding Email lacks Password validation | low | $0 | [Adding Email lacks Password validation](229869-adding-email-lacks-password-validation.md) |
| 229987 | Improper Authentication - Generic | n/a | $0 | [Password token validation in https://demo.weblate.org/](229987-password-token-validation-in-https-demo-weblate-org.md) |
| 223384 | Cleartext Storage of Sensitive Information | none | $0 | [Directory Listing ](223384-directory-listing.md) |
| 224186 | Email spoofing at weblate.org | n/a | $0 | [Email spoofing at weblate.org](224186-email-spoofing-at-weblate-org.md) |
| 225722 | 7BO: Binary Option Robot URL should be HTTPS | n/a | $0 | [7BO: Binary Option Robot URL should be HTTPS](225722-7bo-binary-option-robot-url-should-be-https.md) |
| 223367 | Cross-Site Request Forgery (CSRF) | medium | $0 | [CSRF - Changing the full name / adding a secondary email identity of an account via a GET request](223367-csrf-changing-the-full-name-adding-a-secondary-email-identit.md) |
| 223618 | Weak Cryptography for Passwords | low | $0 | [Null Password - Setting a new password doesn't check for empty spaces](223618-null-password-setting-a-new-password-doesn-t-check-for-empty.md) |
| 223851 | Weak Cryptography for Passwords | low | $0 | [Setting a password with a single character](223851-setting-a-password-with-a-single-character.md) |
| 224006 | Violation of Secure Design Principles | none | $0 | [HttpOnly Flag not set ](224006-httponly-flag-not-set.md) |
| 223609 | Improper Authentication - Generic | low | $0 | [Notify user about password change](223609-notify-user-about-password-change.md) |
| 223692 | Cross-site Scripting (XSS) - Generic | low | $0 | [Self XSS at translation page through Editor Link at demo.weblate.org](223692-self-xss-at-translation-page-through-editor-link-at-demo-web.md) |
| 223343 | Information Disclosure | low | $0 | [Already Registered Email Disclosure](223343-already-registered-email-disclosure.md) |
| 223718 | Open Redirect | medium | $0 | [Open redirect in Signing in via Social Sites](223718-open-redirect-in-signing-in-via-social-sites.md) |
| 225540 | Improper Certificate Validation | none | $0 | [Incorrect HTTPS Certificate](225540-incorrect-https-certificate.md) |
| 225555 | UI Redressing (Clickjacking) | n/a | $0 | [ClickJacking on Debug](225555-clickjacking-on-debug.md) |
| 225769 | Facebook share URL should be HTTPS | n/a | $0 | [Facebook share URL should be HTTPS](225769-facebook-share-url-should-be-https.md) |
| 223557 | Abuse of Api that causes spamming users and possible DOS due to missing rate limit | low | $0 | [Abuse of Api that causes spamming users and possible DOS due to missing rate limit](223557-abuse-of-api-that-causes-spamming-users-and-possible-dos-due.md) |
| 223931 | Violation of Secure Design Principles | low | $0 | [Specify maximal length in new comment](223931-specify-maximal-length-in-new-comment.md) |
| 223723 | Cross-site Scripting (XSS) - Generic | low | $0 | [weblate.org: X-XSS-Protection not enabled](223723-weblate-org-x-xss-protection-not-enabled.md) |
| 223396 | Cross-site Scripting (XSS) - Generic | low | $0 | [hosted.weblate.org: X-XSS-Protection not enabled](223396-hosted-weblate-org-x-xss-protection-not-enabled.md) |
| 224015 | Violation of Secure Design Principles | none | $0 | [Specify maximal length in translation](224015-specify-maximal-length-in-translation.md) |
| 223653 | Inadequate Encryption Strength | low | $0 | [demo.weblate.org is vulnerable to SWEET32 Vulnerability](223653-demo-weblate-org-is-vulnerable-to-sweet32-vulnerability.md) |
| 223362 | Violation of Secure Design Principles | low | $0 | [Improper Password Reset Policy on https://hosted.weblate.org/](223362-improper-password-reset-policy-on-https-hosted-weblate-org.md) |
| 225495 | Path Traversal | medium | $0 | [full path disclosure at hosted.weblate.org/admin/accounts/profile/ ](225495-full-path-disclosure-at-hosted-weblate-org-admin-accounts-pr.md) |
| 228471 | Information Disclosure | none | $0 | [DNSSEC Zone Walk using NSEC Records](228471-dnssec-zone-walk-using-nsec-records.md) |
| 257384 | Violation of Secure Design Principles | none | $0 | [No rate limit or captcha to identify humans](257384-no-rate-limit-or-captcha-to-identify-humans.md) |
| 231062 | Violation of Secure Design Principles | none | $0 | [CSP "script-src" includes "unsafe-inline" in weblate.org and demo.weblate.org](231062-csp-script-src-includes-unsafe-inline-in-weblate-org-and-dem.md) |
| 2370002 | Information Disclosure | low | $0 | [Information Disclosure](2370002-information-disclosure.md) |
