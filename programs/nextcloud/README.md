# Nextcloud

Disclosed reports: **624**

| ID | Temuan | Severity | Bounty | Writeup |
| --- | --- | --- | ---: | --- |
| 1170024 | Improper Authentication - Generic | high | $4000 | [Attacker can obtain write access to any federated share/public link](1170024-attacker-can-obtain-write-access-to-any-federated-share-publ.md) |
| 3489490 | Improper Authentication - Generic | high | $2500 | [Authentication Bypass in ID4me handling via Missing JWT Signature Verification in User OIDC](3489490-authentication-bypass-in-id4me-handling-via-missing-jwt-sign.md) |
| 1189162 | End to end encryption public key is not properly verified on Desktop and Android | medium | $1500 | [End to end encryption public key is not properly verified on Desktop and Android](1189162-end-to-end-encryption-public-key-is-not-properly-verified-on.md) |
| 1302155 | Path Traversal | high | $1250 | [Arbitrary read of all SVG files on a Nextcloud server](1302155-arbitrary-read-of-all-svg-files-on-a-nextcloud-server.md) |
| 1200700 | User deletion is not handled properly everywhere | medium | $1000 | [User deletion is not handled properly everywhere](1200700-user-deletion-is-not-handled-properly-everywhere.md) |
| 1078002 | Resource Injection | medium | $1000 | [Nextcloud Desktop Client RCE via malicious URI schemes](1078002-nextcloud-desktop-client-rce-via-malicious-uri-schemes.md) |
| 1193321 | Improper Access Control - Generic | high | $1000 | [Scoped apptokens can be changed by that very apptoken](1193321-scoped-apptokens-can-be-changed-by-that-very-apptoken.md) |
| 2419776 | Improper Authentication - Generic | medium | $1000 | [Ability to by-pass second factor ](2419776-ability-to-by-pass-second-factor.md) |
| 1679267 | Improper Certificate Validation | medium | $1000 | [Desktop client does not verify received singed certificate in end to end encryption](1679267-desktop-client-does-not-verify-received-singed-certificate-i.md) |
| 1050244 | Two-factor authentication enforcement bypass | high | $750 | [Two-factor authentication enforcement bypass](1050244-two-factor-authentication-enforcement-bypass.md) |
| 1167916 | Improper Access Control - Generic | low | $750 | [Default Nextcloud Server and Android Client leak sharee searches to Nextcloud](1167916-default-nextcloud-server-and-android-client-leak-sharee-sear.md) |
| 1668028 | Cross-site Scripting (XSS) - Generic | low | $750 | [XSS in Desktop Client in the notifications](1668028-xss-in-desktop-client-in-the-notifications.md) |
| 2289425 | Improper Access Control - Generic | high | $750 | [Can reshare read&share only folder with more permissions](2289425-can-reshare-read-share-only-folder-with-more-permissions.md) |
| 1878391 | Improper Verification of Cryptographic Signature | medium | $750 | [ID4ME does not validate signature or expiration](1878391-id4me-does-not-validate-signature-or-expiration.md) |
| 1265709 | Improper Restriction of Authentication Attempts | medium | $750 | [Lack of bruteforce protection for TOTP 2FA](1265709-lack-of-bruteforce-protection-for-totp-2fa.md) |
| 248656 | Improper Authentication - Generic | high | $750 | [bypass of 2FA](248656-bypass-of-2fa.md) |
| 1167853 | Improper Access Control - Generic | medium | $750 | [Trusted servers exchange can be triggered by attacker](1167853-trusted-servers-exchange-can-be-triggered-by-attacker.md) |
| 819807 | Insecure Direct Object Reference (IDOR) | high | $500 | [Missing ownership check on remote wipe endpoint](819807-missing-ownership-check-on-remote-wipe-endpoint.md) |
| 1878381 | Cross-Site Request Forgery (CSRF) | medium | $500 | [CSRF protection on OIDC login is broken](1878381-csrf-protection-on-oidc-login-is-broken.md) |
| 1724016 | Improper Access Control - Generic | medium | $500 | [Download permissions can be changed by resharer](1724016-download-permissions-can-be-changed-by-resharer.md) |
| 1987062 | Improper Restriction of Authentication Attempts | high | $500 | [Password reset endpoint is not brute force protected](1987062-password-reset-endpoint-is-not-brute-force-protected.md) |
| 2447316 | Improper Access Control - Generic | medium | $500 | [User can copy locked folders and gain access to the contents](2447316-user-can-copy-locked-folders-and-gain-access-to-the-contents.md) |
| 1356508 | Improper Access Control - Generic | medium | $500 | [Read-only users can restore old versions](1356508-read-only-users-can-restore-old-versions.md) |
| 1918525 | Improper Restriction of Authentication Attempts | medium | $500 | [Brute force protection allows to send more requests than intended](1918525-brute-force-protection-allows-to-send-more-requests-than-int.md) |
| 2290680 | Improper Access Control - Generic | medium | $500 | [Re-emergence of Security Vulnerability in Nextcloud Version 28 Previously Fixed in 25.0.4](2290680-re-emergence-of-security-vulnerability-in-nextcloud-version.md) |
| 1258448 | Improper Restriction of Authentication Attempts | medium | $500 | [Missing brute force protection on OAuth2 API controller](1258448-missing-brute-force-protection-on-oauth2-api-controller.md) |
| 1167929 | Improper Access Control - Generic | low | $500 | [File drop public link can also be converted to federated share](1167929-file-drop-public-link-can-also-be-converted-to-federated-sha.md) |
| 216812 | Cross-site Scripting (XSS) - Reflected | low | $450 | [Reflected XSS in error pages (NC-SA-2017-008)](216812-reflected-xss-in-error-pages-nc-sa-2017-008.md) |
| 1914115 | Improper Access Control - Generic | high | $400 | [End-to-end encrypted file-drops can be made inaccessible](1914115-end-to-end-encrypted-file-drops-can-be-made-inaccessible.md) |
| 1173436 | Information Disclosure | low | $350 | [Default settings leak federated cloud id to lookup server of all users](1173436-default-settings-leak-federated-cloud-id-to-lookup-server-of.md) |
| 903424 | Cryptographic Issues - Generic | medium | $300 | [SSL certificate not validated when registering with a provider](903424-ssl-certificate-not-validated-when-registering-with-a-provid.md) |
| 146067 | Improper Authentication - Generic | n/a | $300 | [Read-only share recipient can restore old versions of file](146067-read-only-share-recipient-can-restore-old-versions-of-file.md) |
| 191979 | Privilege Escalation | low | $300 | [Limitation of app specific password scope can be bypassed (NC-SA-2017-009)](191979-limitation-of-app-specific-password-scope-can-be-bypassed-nc.md) |
| 3620539 | Improper Access Control - Generic | medium | $270 | [Public shares remain accessible via alternate endpoints after owner account is disabled](3620539-public-shares-remain-accessible-via-alternate-endpoints-afte.md) |
| 3617729 | Privacy Violation | medium | $250 | [Mail contact autocomplete bypasses administrator-configured user enumeration restrictions and expose member information outside the intended scope](3617729-mail-contact-autocomplete-bypasses-administrator-configured.md) |
| 2380133 | Improper Access Control - Generic | low | $250 | [Can download files on Android app without permission](2380133-can-download-files-on-android-app-without-permission.md) |
| 3400143 | Insufficiently Protected Credentials | medium | $250 | [Credential Disclosure via Unvalidated directDownloadUrl (Missing DontAddCredentialsAttribute)](3400143-credential-disclosure-via-unvalidated-directdownloadurl-miss.md) |
| 2307625 | Code Injection | n/a | $250 | [Code injection in Nextcloud Desktop Client for macOS](2307625-code-injection-in-nextcloud-desktop-client-for-macos.md) |
| 2484499 | Information Disclosure | medium | $250 | [Incomplete sanitization in SVG preview provider](2484499-incomplete-sanitization-in-svg-preview-provider.md) |
| 1702864 | Server-Side Request Forgery (SSRF) | medium | $250 | [SSRF via filter bypass due to lax checking on IPs](1702864-ssrf-via-filter-bypass-due-to-lax-checking-on-ips.md) |
| 1608039 | Server-Side Request Forgery (SSRF) | low | $250 | [SSRF via potential filter bypass with too lax local domain checking](1608039-ssrf-via-potential-filter-bypass-with-too-lax-local-domain-c.md) |
| 1878255 | Improper Access Control - Generic | low | $250 | [Nextcloud mail does not respect download permissions in shares](1878255-nextcloud-mail-does-not-respect-download-permissions-in-shar.md) |
| 2457588 | Open Redirect | medium | $250 | [Event create can create attachments that link to other websites ](2457588-event-create-can-create-attachments-that-link-to-other-websi.md) |
| 1161401 | Information Disclosure | low | $250 | [Notification implicit PendingIntent in com.nextcloud.client allows to access contacts](1161401-notification-implicit-pendingintent-in-com-nextcloud-client.md) |
| 672623 | Violation of Secure Design Principles | low | $250 | [Username and Access Token Disclousure](672623-username-and-access-token-disclousure.md) |
| 1192470 | Clients do not verify server public key | low | $250 | [Clients do not verify server public key](1192470-clients-do-not-verify-server-public-key.md) |
| 3576823 | Server-Side Request Forgery (SSRF) | medium | $250 | [SSRF on Nextcloud Whiteboard Application via Recordings to Unauthorised Access to Whiteboards](3576823-ssrf-on-nextcloud-whiteboard-application-via-recordings-to-u.md) |
| 1595006 | Server-Side Request Forgery (SSRF) | medium | $250 | [Unauthenticated SSRF in 3rd party module "cerdic/csstidy"](1595006-unauthenticated-ssrf-in-3rd-party-module-cerdic-csstidy.md) |
| 213227 | Cross-site Scripting (XSS) - Generic | low | $250 | [DOM XSS vulnerability in search dialogue (NC-SA-2017-007)](213227-dom-xss-vulnerability-in-search-dialogue-nc-sa-2017-007.md) |
| 590319 | Path Traversal | medium | $250 | [Linux client is vulnerable to directory traversal when downloading files](590319-linux-client-is-vulnerable-to-directory-traversal-when-downl.md) |
| 1688199 | Uncontrolled Resource Consumption | medium | $250 | [Database resource exhaustion for logged-in users via sharee recommendations with circles](1688199-database-resource-exhaustion-for-logged-in-users-via-sharee.md) |
| 1965156 | Improper Access Control - Generic | low | $250 | [Text does not respect 'Allow download' permissions](1965156-text-does-not-respect-allow-download-permissions.md) |
| 1408692 | Path Traversal | low | $250 | [Access to arbitrary file of the Nextcloud Android app from within the Nextcloud Android app](1408692-access-to-arbitrary-file-of-the-nextcloud-android-app-from-w.md) |
| 2067572 | Improper Access Control - Generic | high | $250 | [New AppPassword can be generated without password confirmation](2067572-new-apppassword-can-be-generated-without-password-confirmati.md) |
| 1189174 | Improper Access Control - Generic | low | $250 | [End to end encryption folder locking is not properly protected](1189174-end-to-end-encryption-folder-locking-is-not-properly-protect.md) |
| 838510 | user can bypass password enforcement when federated sharing is enabled | n/a | $250 | [user can bypass password enforcement when federated sharing is enabled](838510-user-can-bypass-password-enforcement-when-federated-sharing.md) |
| 2021684 | Issuer not verified from obtained token in user_oidc  | medium | $250 | [Issuer not verified from obtained token in user_oidc ](2021684-issuer-not-verified-from-obtained-token-in-user-oidc.md) |
| 3599383 | Improper Access Control - Generic | medium | $200 | [Arbitrary Board Preference Injection via Deck Config API](3599383-arbitrary-board-preference-injection-via-deck-config-api.md) |
| 3484601 | Insecure Direct Object Reference (IDOR) | low | $200 | [Team membership information returned on API level based on ID](3484601-team-membership-information-returned-on-api-level-based-on-i.md) |
| 1450368 | Improper Access Control - Generic | low | $200 | [com.nextcloud.client bypass the protection lock in andoid app v 3.18.1 latest version.](1450368-com-nextcloud-client-bypass-the-protection-lock-in-andoid-ap.md) |
| 673724 | Improper Access Control - Generic | low | $200 | [Circle email-members have still access to a shared folder/file after they are removed from the circle](673724-circle-email-members-have-still-access-to-a-shared-folder-fi.md) |
| 203594 | Information Disclosure | low | $183 | [Calendar and addressbook names disclosed (NC-SA-2017-012)](203594-calendar-and-addressbook-names-disclosed-nc-sa-2017-012.md) |
| 3625210 | Improper Authentication - Generic | medium | $150 | [PIN bypass in PassCodeActivity via back button](3625210-pin-bypass-in-passcodeactivity-via-back-button.md) |
| 3572848 | Improper Access Control - Generic | medium | $150 | [Group restriction bypass via bearer token in user_oidc (SETTING_RESTRICT_LOGIN_TO_GROUPS not enforced in Backend::getCurrentUserId)](3572848-group-restriction-bypass-via-bearer-token-in-user-oidc-setti.md) |
| 3511998 | Insecure Direct Object Reference (IDOR) | low | $150 | [Private circle can be added to another circle via API despite visibility restriction](3511998-private-circle-can-be-added-to-another-circle-via-api-despit.md) |
| 3357808 | Cross-site Scripting (XSS) - Stored | medium | $150 | [Stored XSS Vulnerability via SVG File](3357808-stored-xss-vulnerability-via-svg-file.md) |
| 3610332 | Business Logic Errors | medium | $150 | [Approval app's file-freshness check can be bypassed by omitting the etag parameter, allowing approval of unreviewed file changes](3610332-approval-app-s-file-freshness-check-can-be-bypassed-by-omitt.md) |
| 3513471 | Information Disclosure | medium | $150 | [Unauthenticated testing endpoint of notify_push expose internal IP](3513471-unauthenticated-testing-endpoint-of-notify-push-expose-inter.md) |
| 291764 | SQL Injection | low | $150 | [SQL Injection found in NextCloud Android App Content Provider](291764-sql-injection-found-in-nextcloud-android-app-content-provide.md) |
| 662204 | Cross-site Scripting (XSS) - Stored | low | $150 | [Persistent XSS via filename in projects](662204-persistent-xss-via-filename-in-projects.md) |
| 3040887 | Improper Access Control - Generic | medium | $150 | [Users can modify tags on files that do not belong to them](3040887-users-can-modify-tags-on-files-that-do-not-belong-to-them.md) |
| 916704 | Insecure Direct Object Reference (IDOR) | medium | $150 | [Access control missing while viewing the attachments in the "All boards"](916704-access-control-missing-while-viewing-the-attachments-in-the.md) |
| 3534050 | Improper Authentication - Generic | low | $150 | [Activity app does not verify federated file activity received from remote servers ](3534050-activity-app-does-not-verify-federated-file-activity-receive.md) |
| 1194606 | Improper Access Control - Generic | high | $150 | [Virtual Data Room / Hide download on collabora is easy to bypass](1194606-virtual-data-room-hide-download-on-collabora-is-easy-to-bypa.md) |
| 1724021 | Improper Access Control - Generic | medium | $150 | [Secure view trivial to bypass](1724021-secure-view-trivial-to-bypass.md) |
| 1977222 | Open Redirect | medium | $150 | [Open redirect on "Unsupported browser" warning](1977222-open-redirect-on-unsupported-browser-warning.md) |
| 662218 | Improper Authentication - Generic | low | $150 | [Talk - Leak of password-protected room name via already existent resource addition](662218-talk-leak-of-password-protected-room-name-via-already-existe.md) |
| 1215263 | Code Injection | medium | $125 | [Download of file with arbitrary extension via injection into attachment header](1215263-download-of-file-with-arbitrary-extension-via-injection-into.md) |
| 622170 | Code Injection | medium | $100 | [Arbitrary code execution in desktop client via OpenSSL config](622170-arbitrary-code-execution-in-desktop-client-via-openssl-confi.md) |
| 2388183 | Improper Access Control - Generic | n/a | $100 | [Easy way to create a new Deck board without permission ](2388183-easy-way-to-create-a-new-deck-board-without-permission.md) |
| 2479325 | Information Disclosure | low | $100 | [Events information leaked with shared calendars on recurrence exceptions](2479325-events-information-leaked-with-shared-calendars-on-recurrenc.md) |
| 1784162 | Violation of Secure Design Principles | low | $100 | [OAuth2 "authorization_code" is valid indefinetly](1784162-oauth2-authorization-code-is-valid-indefinetly.md) |
| 588562 | Uncontrolled Resource Consumption | medium | $100 | [Memory Leak in OCUtil.dll library in Desktop client can lead to DoS](588562-memory-leak-in-ocutil-dll-library-in-desktop-client-can-lead.md) |
| 3507273 | Information Disclosure | low | $100 | [Email Enumeration via Password-Protected Share Identity Verification](3507273-email-enumeration-via-password-protected-share-identity-veri.md) |
| 2508422 | Information Disclosure | high | $100 | [Mail auto configurator can be tricked into sending account information to wrong servers ](2508422-mail-auto-configurator-can-be-tricked-into-sending-account-i.md) |
| 2245437 | Improper Authentication - Generic | low | $100 | [App PIN code can be bypassed in Files iOS](2245437-app-pin-code-can-be-bypassed-in-files-ios.md) |
| 2120667 | Improper Access Control - Generic | medium | $100 | [ Bypass password confirmation via Context-dependent access control (CDCA)](2120667-bypass-password-confirmation-via-context-dependent-access-co.md) |
| 2107934 | Improper Access Control - Generic | low | $100 | [Admins can change authentication details of user configured external storage](2107934-admins-can-change-authentication-details-of-user-configured.md) |
| 1994324 | Cleartext Storage in a File or on Disk | medium | $100 | [OAuth2 client_secret stored in plain text in the database](1994324-oauth2-client-secret-stored-in-plain-text-in-the-database.md) |
| 575562 | Cross-site Scripting (XSS) - Stored | low | $100 | [Blind Stored XSS on iOS App due to Unsanitized Webview](575562-blind-stored-xss-on-ios-app-due-to-unsanitized-webview.md) |
| 1675014 | Improper Access Control - Generic | low | $100 | [Profile of disabled user stays accessible](1675014-profile-of-disabled-user-stays-accessible.md) |
| 819863 | Cross-site Scripting (XSS) - Generic | low | $100 | [XSS in PDF Viewer](819863-xss-in-pdf-viewer.md) |
| 3385434 | Use of Insufficiently Random Values | low | $100 | [Predictable proposal participant tokens enable unauthorized access and vote submission](3385434-predictable-proposal-participant-tokens-enable-unauthorized.md) |
| 1215251 | Information Disclosure | medium | $100 | [Bypass of privacy filter / tracking pixel blocker](1215251-bypass-of-privacy-filter-tracking-pixel-blocker.md) |
| 808287 | Business Logic Errors | low | $100 | [Unrestricted file upload on the image of contacts](808287-unrestricted-file-upload-on-the-image-of-contacts.md) |
| 1181962 | Session Fixation | medium | $100 | [Session fixation on public talk links](1181962-session-fixation-on-public-talk-links.md) |
| 840598 | Improper Restriction of Authentication Attempts | medium | $100 | [Possible denial of service when entering a loooong password](840598-possible-denial-of-service-when-entering-a-loooong-password.md) |
| 894876 | Cross-site Scripting (XSS) - Stored | low | $100 | [XSS through image upload of contacts using svg file](894876-xss-through-image-upload-of-contacts-using-svg-file.md) |
| 2326618 | Deck app allows to spoof file extensions by using RTLO characters | medium | $100 | [Deck app allows to spoof file extensions by using RTLO characters](2326618-deck-app-allows-to-spoof-file-extensions-by-using-rtlo-chara.md) |
| 518669 | SQL Injection | low | $100 | [SQLi allow query restriction bypass on exposed FileContentProvider](518669-sqli-allow-query-restriction-bypass-on-exposed-filecontentpr.md) |
| 736867 | Server-Side Request Forgery (SSRF) | medium | $100 | [SSRF protection bypass](736867-ssrf-protection-bypass.md) |
| 297751 | Insecure Direct Object Reference (IDOR) | low | $100 | [Registered users can change app password permissions for any user](297751-registered-users-can-change-app-password-permissions-for-any.md) |
| 1691195 | Improper Access Control - Generic | low | $100 | [Missing rate limiting on password reset functionality allows to send lot of emails](1691195-missing-rate-limiting-on-password-reset-functionality-allows.md) |
| 1192159 | public webdav endpoint not bruteforce protected | low | $100 | [public webdav endpoint not bruteforce protected](1192159-public-webdav-endpoint-not-bruteforce-protected.md) |
| 1200785 | Ransomware protection is missing extentions take 2 | low | $100 | [Ransomware protection is missing extentions take 2](1200785-ransomware-protection-is-missing-extentions-take-2.md) |
| 896522 | Cross-site Scripting (XSS) - Reflected | medium | $100 | [Reflected XSS when renaming a file with a vulnerable name which results in an error](896522-reflected-xss-when-renaming-a-file-with-a-vulnerable-name-wh.md) |
| 388515 | Improper Access Control - Generic | medium | $100 | [Access control issue -- [Allow file system access not validated when using session auth]](388515-access-control-issue-allow-file-system-access-not-validated.md) |
| 720306 | Code Injection | critical | $100 | [Docker image with FPM is vulnerable to CVE-2019-11043](720306-docker-image-with-fpm-is-vulnerable-to-cve-2019-11043.md) |
| 3293290 | Cross-site Scripting (XSS) - Stored | low | $100 | [Stored XSS in contacts app via organisation and title field](3293290-stored-xss-in-contacts-app-via-organisation-and-title-field.md) |
| 592864 | CRLF Injection | medium | $100 | [Non-admin users can trigger writes to memcached by entering a malicious server as a share URL](592864-non-admin-users-can-trigger-writes-to-memcached-by-entering.md) |
| 1406926 | Business Logic Errors | low | $100 | [bypass forced password protection via circles app](1406926-bypass-forced-password-protection-via-circles-app.md) |
| 1189168 | Android app does not clear end to end encryption keys | low | $100 | [Android app does not clear end to end encryption keys](1189168-android-app-does-not-clear-end-to-end-encryption-keys.md) |
| 534541 | Improper Access Control - Generic | low | $100 | [Combination of content provider allows private data disclosure](534541-combination-of-content-provider-allows-private-data-disclosu.md) |
| 3625932 | Privilege Escalation | low | $100 | [Unauthorised access with hidden public link creation when sharing to a Team External Member](3625932-unauthorised-access-with-hidden-public-link-creation-when-sh.md) |
| 1192144 | Add to your nextcloud endpoint is not properly protected | low | $100 | [Add to your nextcloud endpoint is not properly protected](1192144-add-to-your-nextcloud-endpoint-is-not-properly-protected.md) |
| 427835 | Server-Side Request Forgery (SSRF) | medium | $100 | [Server-Side request forgery in New-Subscription feature of the calendar app](427835-server-side-request-forgery-in-new-subscription-feature-of-t.md) |
| 1403614 | Cross-Site Request Forgery (CSRF) | low | $100 | [Possibility to force an admin to install recommended applications](1403614-possibility-to-force-an-admin-to-install-recommended-applica.md) |
| 1173684 | Uncontrolled Resource Consumption | medium | $100 | [index.php/apps/files_sharing/shareinfo endpoint is not properly protected](1173684-index-php-apps-files-sharing-shareinfo-endpoint-is-not-prope.md) |
| 232347 | Code Injection | low | $100 | [[FG-VD-17-063] NextCloud Insufficient Attack Protection Vulnerability Notification](232347-fg-vd-17-063-nextcloud-insufficient-attack-protection-vulner.md) |
| 1606961 | Weak Cryptography for Passwords | low | $100 | [Generated passwords are not fully validated by HIBPValidator](1606961-generated-passwords-are-not-fully-validated-by-hibpvalidator.md) |
| 1520685 | Privacy Violation | low | $100 | [Moderator can enable cam/mic remotely if  cam/mic-permission was disabled while user has activated cam/mic](1520685-moderator-can-enable-cam-mic-remotely-if-cam-mic-permission.md) |
| 447494 | Improper Access Control - Generic | medium | $100 | [Share recipient can modify a share's expiration date](447494-share-recipient-can-modify-a-share-s-expiration-date.md) |
| 1210424 | Improper Access Control - Generic | low | $100 | [Federated editing allows iframing possibly malicious remotes](1210424-federated-editing-allows-iframing-possibly-malicious-remotes.md) |
| 164027 | Cross-site Scripting (XSS) - Generic | n/a | $100 | [Reflected Self-XSS Vulnerability in the Comment section of Files Information](164027-reflected-self-xss-vulnerability-in-the-comment-section-of-f.md) |
| 242727 | Information Disclosure | low | $75 | [Android content provider exposes password-protected share password hashes](242727-android-content-provider-exposes-password-protected-share-pa.md) |
| 486693 | Session Fixation | medium | $50 | [2FA Session not expires after the password reset](486693-2fa-session-not-expires-after-the-password-reset.md) |
| 428660 | Business Logic Errors | low | $50 | [Gallery: No feedback for invalid password](428660-gallery-no-feedback-for-invalid-password.md) |
| 146133 | Improper Authentication - Generic | n/a | $50 | [Authentication Issue](146133-authentication-issue.md) |
| 490946 | Improper Authentication - Generic | low | $50 | [Bypassing lock protection](490946-bypassing-lock-protection.md) |
| 428010 | Information Disclosure | medium | $50 | [Talk / spreed: Disclosure of Room names and participants for password protected rooms](428010-talk-spreed-disclosure-of-room-names-and-participants-for-pa.md) |
| 231917 | Information Disclosure | medium | $50 | [Shared file link - password protection bypass under certain conditions](231917-shared-file-link-password-protection-bypass-under-certain-co.md) |
| 154827 | Violation of Secure Design Principles | low | $50 | [More content spoofing through dir param in the files app](154827-more-content-spoofing-through-dir-param-in-the-files-app.md) |
| 179073 | Violation of Secure Design Principles | low | $50 | [Content Spoofing in "files" app](179073-content-spoofing-in-files-app.md) |
| 851807 | Code Injection | high | $0 | [Code injection possible with malformed Nextcloud Talk chat commands](851807-code-injection-possible-with-malformed-nextcloud-talk-chat-c.md) |
| 642515 | Improper Access Control - Generic | medium | $0 | [User can delete data in shared folders he's not autorized to access](642515-user-can-delete-data-in-shared-folders-he-s-not-autorized-to.md) |
| 258084 | Information Disclosure | medium | $0 | [Access to all files of remote user through shared file](258084-access-to-all-files-of-remote-user-through-shared-file.md) |
| 546753 | OS Command Injection | high | $0 | [Remote Code Execution via Extract App Plugin](546753-remote-code-execution-via-extract-app-plugin.md) |
| 2946927 | Sensitive Information Disclosure via Back Button Post Logout on https://apps.nextcloud.com/account/ | low | $0 | [Sensitive Information Disclosure via Back Button Post Logout on https://apps.nextcloud.com/account/](2946927-sensitive-information-disclosure-via-back-button-post-logout.md) |
| 889243 | Improper Privilege Management | medium | $0 | [Re-Sharing allows increase of privileges](889243-re-sharing-allows-increase-of-privileges.md) |
| 3521434 | Improper Access Control - Generic | low | $0 | [View-only guests could see deleted Collectives pages in the trashbin](3521434-view-only-guests-could-see-deleted-collectives-pages-in-the.md) |
| 3360354 | Insecure Direct Object Reference (IDOR) | low | $0 | [WebAuthn app was updated based on public key](3360354-webauthn-app-was-updated-based-on-public-key.md) |
| 2248328 | Deserialization of Untrusted Data | critical | $0 | [RCE on Wordpress website](2248328-rce-on-wordpress-website.md) |
| 997070 | Business Logic Errors | medium | $0 | [No rate limiting for confirmation email lead to huge Mass mailings](997070-no-rate-limiting-for-confirmation-email-lead-to-huge-mass-ma.md) |
| 3462991 | SQL Injection | high | $0 | [SQL Injection in Column Type Parameter Allows Arbitrary SQL Execution](3462991-sql-injection-in-column-type-parameter-allows-arbitrary-sql.md) |
| 508487 | SQL Injection | critical | $0 | [Arbitrary SQL command injection](508487-arbitrary-sql-command-injection.md) |
| 3799010 | Insecure Direct Object Reference (IDOR) | medium | $0 | [TaskProcessing callback authorization bypass allows ex-members to post as Assistant Talk Bot](3799010-taskprocessing-callback-authorization-bypass-allows-ex-membe.md) |
| 2311179 | Information Exposure Through Directory Listing | medium | $0 | [Directory Listing of publicly available assets](2311179-directory-listing-of-publicly-available-assets.md) |
| 719426 | File-drop content is visible through the gallery app | medium | $0 | [File-drop content is visible through the gallery app](719426-file-drop-content-is-visible-through-the-gallery-app.md) |
| 2376929 | Improper Access Control - Generic | medium | $0 | [ID4me feature of OpenID connect app available even when disabled ](2376929-id4me-feature-of-openid-connect-app-available-even-when-disa.md) |
| 3483708 | Improper Access Control - Generic | medium | $0 | [Valid share tokens allow to access tempory upload files of share owner](3483708-valid-share-tokens-allow-to-access-tempory-upload-files-of-s.md) |
| 3399016 | Improper Null Termination | none | $0 | [Improper input validation On Exported deep-link handler crashes `FileDisplayActivity` on crafted external URL — Denial-of-Service](3399016-improper-input-validation-on-exported-deep-link-handler-cras.md) |
| 3599470 | Business Logic Errors | low | $0 | [Improper input validation in emoji field leads to sidebar UI denial of service](3599470-improper-input-validation-in-emoji-field-leads-to-sidebar-ui.md) |
| 3249624 | Path Traversal | medium | $0 | [Path Traversal Vulnerability in Nextcloud Tables Enables Arbitrary File Exfiltration of Any Files Supported by PhpSpreadsheet Library](3249624-path-traversal-vulnerability-in-nextcloud-tables-enables-arb.md) |
| 3304830 | Insecure Direct Object Reference (IDOR) | low | $0 | [Files drop share links for end-to-end encrypted folders allowed to drop files into other folders of the share owner ](3304830-files-drop-share-links-for-end-to-end-encrypted-folders-allo.md) |
| 331489 | Information Disclosure | low | $0 | [Extremly simple way to bypass Nextcloud-Client PIN/Fingerprint lock](331489-extremly-simple-way-to-bypass-nextcloud-client-pin-fingerpri.md) |
| 3275810 | Insecure Direct Object Reference (IDOR) | low | $0 | [Calendar app allowed booking appointments without the generated token](3275810-calendar-app-allowed-booking-appointments-without-the-genera.md) |
| 3486747 | Privacy Violation | medium | $0 | [SVG filter primitives bypass remote image blocking, enabling email tracking without consent.](3486747-svg-filter-primitives-bypass-remote-image-blocking-enabling.md) |
| 1879549 | Improper Restriction of Authentication Attempts | high | $0 | [Basic auth header on WebDAV requests is not bruteforce protected](1879549-basic-auth-header-on-webdav-requests-is-not-bruteforce-prote.md) |
| 685990 | Cleartext Storage of Sensitive Information | low | $0 | [Clear text storage of proxy parameters and passwords](685990-clear-text-storage-of-proxy-parameters-and-passwords.md) |
| 2248689 | Authentication bypass in Global Site Selector allows an attacker to log in as any user | critical | $0 | [Authentication bypass in Global Site Selector allows an attacker to log in as any user](2248689-authentication-bypass-in-global-site-selector-allows-an-atta.md) |
| 2254151 | Business Logic Errors | medium | $0 | [Notes app can be tricked into using a received share created before the user logged in](2254151-notes-app-can-be-tricked-into-using-a-received-share-created.md) |
| 3623149 | Server-Side Request Forgery (SSRF) | medium | $0 | [SSRF via User-Controlled Push proxyServer in Notifications Push Registration](3623149-ssrf-via-user-controlled-push-proxyserver-in-notifications-p.md) |
| 3357036 | Mail stored HTML injection in subject text | medium | $0 | [Mail stored HTML injection in subject text](3357036-mail-stored-html-injection-in-subject-text.md) |
| 968232 | Cross-site Scripting (XSS) - Stored | low | $0 | [Stored XSS in collabora via user name](968232-stored-xss-in-collabora-via-user-name.md) |
| 2778441 | Business Logic Errors | medium | $0 | [ Exposing debug.log file leads to server full path disclosure](2778441-exposing-debug-log-file-leads-to-server-full-path-disclosure.md) |
| 3443563 | Information Disclosure | medium | $0 | [Roundcube Webmail Style Sanitizer can be bypassed using CSS Character Escapes](3443563-roundcube-webmail-style-sanitizer-can-be-bypassed-using-css.md) |
| 2058337 | Uncontrolled Resource Consumption | medium | $0 | [Inviting excessive long email addresses to a calendar event makes the server unresponsive](2058337-inviting-excessive-long-email-addresses-to-a-calendar-event.md) |
| 2212627 | Improper Access Control - Generic | high | $0 | [Delete external storage of any user](2212627-delete-external-storage-of-any-user.md) |
| 3590586 | Resource Injection | medium | $0 | [position: fixed !important bypasses CSS sanitizer's fixed-position mitigation, enabling full-viewport phishing overlays.](3590586-position-fixed-important-bypasses-css-sanitizer-s-fixed-posi.md) |
| 2925666 | Improper Access Control - Generic | low | $0 | [Blind SSRF Vulnerability in Appstore Release Upload Form](2925666-blind-ssrf-vulnerability-in-appstore-release-upload-form.md) |
| 1997029 | Path Traversal | medium | $0 | [Path traversal allows tricking the Talk Android app into writing files into it's root directory ](1997029-path-traversal-allows-tricking-the-talk-android-app-into-wri.md) |
| 2305880 | Violation of Secure Design Principles | low | $0 | [Email not verified when changing afterwards on apps.nextcloud.com](2305880-email-not-verified-when-changing-afterwards-on-apps-nextclou.md) |
| 209520 | Open Redirect | n/a | $0 | [http://www.nextcloud.com/wp-includes/js/swfupload/swfupload.swf allows open redirect / site defacement](209520-http-www-nextcloud-com-wp-includes-js-swfupload-swfupload-sw.md) |
| 3479692 | Unauthenticated SSRF via Public Reference API -Sharing Token Bypass | n/a | $0 | [Unauthenticated SSRF via Public Reference API -Sharing Token Bypass](3479692-unauthenticated-ssrf-via-public-reference-api-sharing-token.md) |
| 2247457 | Improper Access Control - Generic | medium | $0 | [Can download files by zipping the folder](2247457-can-download-files-by-zipping-the-folder.md) |
| 2299069 | XML External Entities (XXE) | n/a | $0 | [xmlrpc.php &wp-cron.php files are enabled, and will used for (DDOS),(DOS) and broutforce users attack.](2299069-xmlrpc-php-wp-cron-php-files-are-enabled-and-will-used-for-d.md) |
| 3382343 | Insecure Direct Object Reference (IDOR) | medium | $0 | [BOLA/IDOR in Out-of-Office API allows any authenticated user to read other users' absence data](3382343-bola-idor-in-out-of-office-api-allows-any-authenticated-user.md) |
| 765291 | Path Traversal | high | $0 | [Remote code execution via path traversal in Zip extraction in the Extract app](765291-remote-code-execution-via-path-traversal-in-zip-extraction-i.md) |
| 3594137 | Cross-site Scripting (XSS) - Stored | medium | $0 | [Stored XSS in attachment-display exploitable through SameSite](3594137-stored-xss-in-attachment-display-exploitable-through-samesit.md) |
| 3338748 | Improper Authentication - Generic | medium | $0 | [Approval app allows users to request approval for other users file ](3338748-approval-app-allows-users-to-request-approval-for-other-user.md) |
| 1727424 | Uncontrolled Resource Consumption | low | $0 | [No password length limit when creating a user as an administrator](1727424-no-password-length-limit-when-creating-a-user-as-an-administ.md) |
| 2890071 | Insufficient Logging | medium | $0 | [admin_audit does not log actions on files in a group folder](2890071-admin-audit-does-not-log-actions-on-files-in-a-group-folder.md) |
| 3247499 | Improper Access Control - Generic | medium | $0 | [Deck app allowed user with "Can share" permission to modify permissions of other non-owners](3247499-deck-app-allowed-user-with-can-share-permission-to-modify-pe.md) |
| 2497947 | Use of a Broken or Risky Cryptographic Algorithm | medium | $0 | [Invisible Salamanders Attack against end_to_end_encryption in Nextcloud](2497947-invisible-salamanders-attack-against-end-to-end-encryption-i.md) |
| 2115212 | Server-Side Request Forgery (SSRF) | medium | $0 | [DNS pin middleware can be tricked into DNS rebinding allowing SSRF](2115212-dns-pin-middleware-can-be-tricked-into-dns-rebinding-allowin.md) |
| 452854 | Improper Access Control - Generic | critical | $0 | [Expired reshare links allow access to all files in share](452854-expired-reshare-links-allow-access-to-all-files-in-share.md) |
| 3518758 | Insecure Direct Object Reference (IDOR) | n/a | $0 | [IDOR on ██████ via direct photo URL leads to unauthorized access to deleted and other users' photos](3518758-idor-on-via-direct-photo-url-leads-to-unauthorized-access-to.md) |
| 3367676 | tabnabbing in roundcube webmail | n/a | $0 | [tabnabbing in roundcube webmail](3367676-tabnabbing-in-roundcube-webmail.md) |
| 2446531 | Use of a Broken or Risky Cryptographic Algorithm | medium | $0 | [Weak ssh algorithms and CVE-2023-48795 Discovered on various subdomains of nextcloud.com](2446531-weak-ssh-algorithms-and-cve-2023-48795-discovered-on-various.md) |
| 1869714 | Server-Side Request Forgery (SSRF) | low | $0 | [Blind SSRF in Mail App](1869714-blind-ssrf-in-mail-app.md) |
| 515484 | Cross-site Scripting (XSS) - Reflected | low | $0 | [[Reflected XSS] In Request URL](515484-reflected-xss-in-request-url.md) |
| 3674940 | Improper Access Control - Generic | medium | $0 | [Critical broken access control: API-only delegated admin can enumerate all Team Folders and grant access to arbitrary groups](3674940-critical-broken-access-control-api-only-delegated-admin-can.md) |
| 3590583 | Resource Injection | medium | $0 | [Unquoted body background attribute enables CSS injection that bypasses remote image blocking](3590583-unquoted-body-background-attribute-enables-css-injection-tha.md) |
| 194329 | Violation of Secure Design Principles | n/a | $0 | [No session logout after changing password & alsoandroid sessions not shown in sessions list so they can be deleted](194329-no-session-logout-after-changing-password-alsoandroid-sessio.md) |
| 1784681 | Insecure Direct Object Reference (IDOR) | medium | $0 | [Ability to read any emails through IDOR on Nextcloud Mail](1784681-ability-to-read-any-emails-through-idor-on-nextcloud-mail.md) |
| 858255 | Cross-site Scripting (XSS) - Generic | medium | $0 | [Cross site scripting - XSRF Token](858255-cross-site-scripting-xsrf-token.md) |
| 508493 | Privilege Escalation | high | $0 | [Group admins can remove arbitrary data from "data" directory (including admin data)](508493-group-admins-can-remove-arbitrary-data-from-data-directory-i.md) |
| 226097 | I am because bug | critical | $0 | [I am because bug](226097-i-am-because-bug.md) |
| 3770482 | Improper Access Control - Generic | medium | $0 | [files_lock: a write-share collaborator can place a TYPE_TOKEN lock that permanently denies the file owner, survives share revocation and account delet](3770482-files-lock-a-write-share-collaborator-can-place-a-type-token.md) |
| 2705507 | Insecure Direct Object Reference (IDOR) | low | $0 | [Share information of Tables app is not limited to affected users ](2705507-share-information-of-tables-app-is-not-limited-to-affected-u.md) |
| 2230915 | Improper Restriction of Authentication Attempts | medium | $0 | [Bruteforce protection in password verification can be bypassed](2230915-bruteforce-protection-in-password-verification-can-be-bypass.md) |
| 3137895 | Insecure Direct Object Reference (IDOR) | medium | $0 | [Missing ownership check in Tables app allows moving columns into tables of other users](3137895-missing-ownership-check-in-tables-app-allows-moving-columns.md) |
| 3138721 | Insecure Direct Object Reference (IDOR) | medium | $0 | [Tables app allowed users to view columns metadata information of any table](3138721-tables-app-allowed-users-to-view-columns-metadata-informatio.md) |
| 2720030 | Open Redirect | n/a | $0 | [Open redirect when logging in with user_oidc](2720030-open-redirect-when-logging-in-with-user-oidc.md) |
| 2210038 | Cross-site Scripting (XSS) - Stored | low | $0 | [HTML injection in search UI when selecting a circle with HTML in the display name](2210038-html-injection-in-search-ui-when-selecting-a-circle-with-htm.md) |
| 1784645 | Improper Access Control - Generic | low | $0 | [Passcode bypass on Talk Android app](1784645-passcode-bypass-on-talk-android-app.md) |
| 469668 | Cleartext Storage of Sensitive Information | low | $0 | [Passwords being stored as plain text in logging](469668-passwords-being-stored-as-plain-text-in-logging.md) |
| 2376909 | Information Disclosure | low | $0 | [Possible to enumerate valid files in password protected shares/files drop shares as well as spam folder with files](2376909-possible-to-enumerate-valid-files-in-password-protected-shar.md) |
| 2376900 | Information Disclosure | low | $0 | [Attachments folder for Text app is accessible on Files Drop/Password protected shares](2376900-attachments-folder-for-text-app-is-accessible-on-files-drop.md) |
| 2112973 | Insecure Direct Object Reference (IDOR) | medium | $0 | [Enabling Birthday Contact to any user](2112973-enabling-birthday-contact-to-any-user.md) |
| 1067824 | Information Disclosure | n/a | $0 | [Database error shown to the user when using a long guest name in richdocuments](1067824-database-error-shown-to-the-user-when-using-a-long-guest-nam.md) |
| 633266 | Code Injection | low | $0 | [Code injection in macOS Desktop Client ](633266-code-injection-in-macos-desktop-client.md) |
| 230328 | Insecure Direct Object Reference (IDOR) | medium | $0 | [IDOR unsubscribe Anyone from NextClouds Newsletters by knowing their Email ](230328-idor-unsubscribe-anyone-from-nextclouds-newsletters-by-knowi.md) |
| 2554079 | Information Disclosure | medium | $0 | [External storage - global credentials returned to the client side in plaintext](2554079-external-storage-global-credentials-returned-to-the-client-s.md) |
| 2250398 | Business Logic Errors | medium | $0 | [Non-admin users can reset app allowlist to the default](2250398-non-admin-users-can-reset-app-allowlist-to-the-default.md) |
| 2101165 | Cleartext Storage of Sensitive Information | medium | $0 | [user_ldap app logs user passwords in the log file on level debug](2101165-user-ldap-app-logs-user-passwords-in-the-log-file-on-level-d.md) |
| 3247386 | Insecure Direct Object Reference (IDOR) | medium | $0 | [Participants were able to blindly delete poll drafts of other users by ID](3247386-participants-were-able-to-blindly-delete-poll-drafts-of-othe.md) |
| 2597504 | Improper Certificate Validation | medium | $0 | [X-E2EE-SIGNATURE verification can be bypassed, leading to loss of confidentiality of end-to-end encrypted files](2597504-x-e2ee-signature-verification-can-be-bypassed-leading-to-los.md) |
| 2094473 | Improper Restriction of Authentication Attempts | medium | $0 | [Password of talk conversations can be bruteforced](2094473-password-of-talk-conversations-can-be-bruteforced.md) |
| 1509216 | CRLF Injection | medium | $0 | [SMTP Command Injection in Appointment Emails via Newlines](1509216-smtp-command-injection-in-appointment-emails-via-newlines.md) |
| 630146 | Cross-Site Request Forgery (CSRF) | low | $0 | [CSRF vulnerability that allows an attacker to modify encryption settings](630146-csrf-vulnerability-that-allows-an-attacker-to-modify-encrypt.md) |
| 3590576 | Remote File Inclusion | medium | $0 | [SMIL values and by attributes bypass remote image blocking via unvalidated resource-loading animations, enabling email tracking without consent](3590576-smil-values-and-by-attributes-bypass-remote-image-blocking-v.md) |
| 3508852 | Business Logic Errors | low | $0 | [Application Data Hiding via Invalid `iconName` Causing Frontend Crash in Nextcloud Tables](3508852-application-data-hiding-via-invalid-iconname-causing-fronten.md) |
| 2902856 | Server-Side Request Forgery (SSRF) | medium | $0 | [[nextcloud/mail] Blind SSRF to Internal Network via "List-Unsubscribe" SMTP Header when allow_local_remote_servers is allowed](2902856-nextcloud-mail-blind-ssrf-to-internal-network-via-list-unsub.md) |
| 1331728 | Information Disclosure | medium | $0 | [Cards in Deck are readable by any user](1331728-cards-in-deck-are-readable-by-any-user.md) |
| 1741430 | Cross-Site Request Forgery (CSRF) | medium | $0 | [CSRF vulnerability in Nextcloud Desktop Client 3.6.1 on Windows when clicking malicious link ](1741430-csrf-vulnerability-in-nextcloud-desktop-client-3-6-1-on-wind.md) |
| 1142918 | Leak arbitrary file under nextcloud android client privacy directory | medium | $0 | [Leak arbitrary file under nextcloud android client privacy directory](1142918-leak-arbitrary-file-under-nextcloud-android-client-privacy-d.md) |
| 429747 | https://help.nextcloud.com::: Web cache poisoning attack | high | $0 | [https://help.nextcloud.com::: Web cache poisoning attack](429747-https-help-nextcloud-com-web-cache-poisoning-attack.md) |
| 2671404 | Nextcloud Tables app - inserting rows to an arbitrary table possible | medium | $0 | [Nextcloud Tables app - inserting rows to an arbitrary table possible](2671404-nextcloud-tables-app-inserting-rows-to-an-arbitrary-table-po.md) |
| 1841408 | Improper Access Control - Generic | low | $0 | [Error in  Booking an appointment reveals the full path of the website](1841408-error-in-booking-an-appointment-reveals-the-full-path-of-the.md) |
| 1842114 | Improper Restriction of Authentication Attempts | medium | $0 | [Missing brute force protection on password confirmation modal](1842114-missing-brute-force-protection-on-password-confirmation-moda.md) |
| 145355 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [Stored XSS on Share-popup of a directory's Gallery-view](145355-stored-xss-on-share-popup-of-a-directory-s-gallery-view.md) |
| 3913007 | Buffer Over-read | none | $0 | [SMTP header injection via C-escape `\r` in the recipient display name](3913007-smtp-header-injection-via-c-escape-r-in-the-recipient-displa.md) |
| 3301553 | Improper Authentication - Generic | medium | $0 | [Cross-User Lock/Unlock via Absolute DAV Path](3301553-cross-user-lock-unlock-via-absolute-dav-path.md) |
| 3521639 | Integer Overflow | low | $0 | [Improper Input Validation and Integer Overflow in timeamount parameter of files_retention app](3521639-improper-input-validation-and-integer-overflow-in-timeamount.md) |
| 1924212 | Improper Restriction of Authentication Attempts | medium | $0 | [Improper restriction of excessive authentication attempts on WebDAV endpoint ](1924212-improper-restriction-of-excessive-authentication-attempts-on.md) |
| 1978882 | Business Logic Errors | high | $0 | [User scoped external storage can be used to gather credentials of other users ](1978882-user-scoped-external-storage-can-be-used-to-gather-credentia.md) |
| 1154003 | Improper Restriction of Authentication Attempts | low | $0 | [Ratelimiting can be bypassed using IPv6 subnets](1154003-ratelimiting-can-be-bypassed-using-ipv6-subnets.md) |
| 3112033 | Improper Handling of Unexpected Data Type | medium | $0 | [Calendar attachments of local files are offered to downloaded](3112033-calendar-attachments-of-local-files-are-offered-to-downloade.md) |
| 2251074 | Improper Handling of URL Encoding (Hex Encoding) | medium | $0 | [Improper handling of request URLs in nextcloud/guests allows guest users to bypass app allowlist](2251074-improper-handling-of-request-urls-in-nextcloud-guests-allows.md) |
| 1516377 | CRLF Injection | medium | $0 | [SMTP Command Injection in iCalendar Attachments to Emails via Newlines](1516377-smtp-command-injection-in-icalendar-attachments-to-emails-vi.md) |
| 788257 | Improper Access Control - Generic | high | $0 | ["Secure View" aka "Hide Download" can be bypassed easily](788257-secure-view-aka-hide-download-can-be-bypassed-easily.md) |
| 3485178 | Business Logic Errors | low | $0 | [Deck app: Invalid tag color is accepted by API and breaks frontend UI](3485178-deck-app-invalid-tag-color-is-accepted-by-api-and-breaks-fro.md) |
| 2263044 | Open Redirect | low | $0 | [Open redirect in user_saml via RelayState parameter](2263044-open-redirect-in-user-saml-via-relaystate-parameter.md) |
| 1847368 | Improper Access Control - Generic | low | $0 | [Full Passcode bypass on Nextcloud App iOS](1847368-full-passcode-bypass-on-nextcloud-app-ios.md) |
| 1755555 | Insecure Direct Object Reference (IDOR) | low | $0 | [Possibility to delete files attached to deck cards of other users](1755555-possibility-to-delete-files-attached-to-deck-cards-of-other.md) |
| 998422 | Cross-site Scripting (XSS) - Stored | low | $0 | [XSS through image upload of contacts using svg file with png extension ](998422-xss-through-image-upload-of-contacts-using-svg-file-with-png.md) |
| 3521646 | Business Logic Errors | low | $0 | [Missing Duplicate Check allowing Multiple Retention Rules per System Tag](3521646-missing-duplicate-check-allowing-multiple-retention-rules-pe.md) |
| 2058556 | Cross-site Scripting (XSS) - Generic | none | $0 | [Self XSS when sending HTML as a comment in the Deck app](2058556-self-xss-when-sending-html-as-a-comment-in-the-deck-app.md) |
| 2211561 | Cross-site Scripting (XSS) - DOM | medium | $0 | [Self XSS when pasting HTML into Text app with Ctrl+Shift+V](2211561-self-xss-when-pasting-html-into-text-app-with-ctrl-shift-v.md) |
| 1687005 | Cleartext Transmission of Sensitive Information | low | $0 | [[user_oidc] Unencrypted Communications](1687005-user-oidc-unencrypted-communications.md) |
| 1222873 | Improper Access Control - Generic | low | $0 | [Sensitive files/ data exists  post deletion of user account](1222873-sensitive-files-data-exists-post-deletion-of-user-account.md) |
| 812754 | Uncontrolled Resource Consumption | high | $0 | [Denial of Service by requesting to reset a password](812754-denial-of-service-by-requesting-to-reset-a-password.md) |
| 237184 | Session Fixation | low | $0 | [Session fixation in password protected public download.](237184-session-fixation-in-password-protected-public-download.md) |
| 343111 | Use of a Key Past its Expiration Date | medium | $0 | [OAuth2 Access Token and App Password Security Vulnerability](343111-oauth2-access-token-and-app-password-security-vulnerability.md) |
| 211213 | Open Redirect | n/a | $0 | [https://xmpp.nextcloud.com///;@www.google.com allows open redirect](211213-https-xmpp-nextcloud-com-www-google-com-allows-open-redirect.md) |
| 3913012 | Buffer Under-read | none | $0 | [Persistent SMTP header injection via identity `organization` / `name`](3913012-persistent-smtp-header-injection-via-identity-organization-n.md) |
| 1946298 | Improper Access Control - Generic | low | $0 | [Missing permission check when removing a photo from an album](1946298-missing-permission-check-when-removing-a-photo-from-an-album.md) |
| 2110945 | Improper Restriction of Authentication Attempts | medium | $0 | [Memcached used as RateLimiter backend is no-op](2110945-memcached-used-as-ratelimiter-backend-is-no-op.md) |
| 1596459 | Improper Access Control - Generic | low | $0 | [Talk Android broadcast receiver is not protected by broadcastPermission allowing malicious apps to communicate](1596459-talk-android-broadcast-receiver-is-not-protected-by-broadcas.md) |
| 1687410 | Cross-site Scripting (XSS) - Stored | low | $0 | [[user_oidc] Stored XSS via Authorization Endpoint - Safari-Only](1687410-user-oidc-stored-xss-via-authorization-endpoint-safari-only.md) |
| 1358977 | Business Logic Errors | medium | $0 | [When sharing a Deck card in conversation the metaData can be manipulated to open arbitrary URL](1358977-when-sharing-a-deck-card-in-conversation-the-metadata-can-be.md) |
| 145524 | Server side request forgery (SSRF) on nextcloud implementation. | n/a | $0 | [Server side request forgery (SSRF) on nextcloud implementation.](145524-server-side-request-forgery-ssrf-on-nextcloud-implementation.md) |
| 3696266 | Path Traversal | medium | $0 | [Path Traversal in Nextcloud Talk Android Exposes User Credentials and Private Data via FileProvider](3696266-path-traversal-in-nextcloud-talk-android-exposes-user-creden.md) |
| 2289333 | Improper Access Control - Generic | medium | $0 | [see card comments after remove shared board](2289333-see-card-comments-after-remove-shared-board.md) |
| 1825679 | Improper Authentication - Generic | low | $0 | [App pin of the Android app can be bypassed via 3rdparty apps generating deep links](1825679-app-pin-of-the-android-app-can-be-bypassed-via-3rdparty-apps.md) |
| 1745766 | Improper Access Control - Generic | low | $0 | [Disabled download shares still allow download through preview images](1745766-disabled-download-shares-still-allow-download-through-previe.md) |
| 1337422 | Information Disclosure | medium | $0 | [Folder architecture and Filesizes of private file drop shares can be getten](1337422-folder-architecture-and-filesizes-of-private-file-drop-share.md) |
| 145392 | Violation of Secure Design Principles | n/a | $0 | [Response Header injection using redirect_uri together with PHP that utilizes Header Folding according to RFC1945 and Internet Explorer 11](145392-response-header-injection-using-redirect-uri-together-with-p.md) |
| 146278 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [Log pollution can lead to HTML Injection.](146278-log-pollution-can-lead-to-html-injection.md) |
| 3568116 | Improper Access Control - Generic | low | $0 | [FederationController::remoteWopiToken() returns full Wopi entity without token type validation](3568116-federationcontroller-remotewopitoken-returns-full-wopi-entit.md) |
| 1895976 | Improper Access Control - Generic | medium | $0 | [Users can set up workflows using restricted and invisible system tags](1895976-users-can-set-up-workflows-using-restricted-and-invisible-sy.md) |
| 1894653 | Improper Restriction of Authentication Attempts | low | $0 | [Missing brute force protection for passwords of password protected share links](1894653-missing-brute-force-protection-for-passwords-of-password-pro.md) |
| 1850407 | Improper Access Control - Generic | medium | $0 | [Chat room member disclosure via autocomplete API](1850407-chat-room-member-disclosure-via-autocomplete-api.md) |
| 1720822 | Violation of Secure Design Principles | n/a | $0 | [Suspicious login app ships old league/flysystem version](1720822-suspicious-login-app-ships-old-league-flysystem-version.md) |
| 1561471 | Cleartext Storage of Sensitive Information | low | $0 | [Password disclosure in initial setup of Mail App](1561471-password-disclosure-in-initial-setup-of-mail-app.md) |
| 685552 | Cross-site Scripting (XSS) - Generic | medium | $0 | [XSS in desktop client via invalid server address on login form](685552-xss-in-desktop-client-via-invalid-server-address-on-login-fo.md) |
| 619484 | Privilege Escalation | medium | $0 | [User with read-only access to a share can gain write access to sub-folders in the share](619484-user-with-read-only-access-to-a-share-can-gain-write-access.md) |
| 458696 | Improper Access Control - Generic | medium | $0 | [xmlrpc.php is enabled - Nextcloud](458696-xmlrpc-php-is-enabled-nextcloud.md) |
| 605915 | Cross-site Scripting (XSS) - Reflected | medium | $0 | [Reflected XSS / Markup Injection in `index.php/svg/core/logo/logo` parameter `color`](605915-reflected-xss-markup-injection-in-index-php-svg-core-logo-lo.md) |
| 3506873 | Improper Access Control - Generic | medium | $0 | [Shared smart albums in the Photos app can expose files outside the album owner's configured source folders](3506873-shared-smart-albums-in-the-photos-app-can-expose-files-outsi.md) |
| 2108342 | Information Disclosure | medium | $0 | [Error when editing a calendar appointment returns stacktrace and query](2108342-error-when-editing-a-calendar-appointment-returns-stacktrace.md) |
| 1261413 | Information Disclosure | critical | $0 | [HEIC image preview can be used to invoke Imagick](1261413-heic-image-preview-can-be-used-to-invoke-imagick.md) |
| 1767439 | Information Disclosure | low | $0 | [Exposed Log File Lead to Full Internal path disclosure at [https://nextcloud.com/wp-content/debug.log] ](1767439-exposed-log-file-lead-to-full-internal-path-disclosure-at-ht.md) |
| 827816 | Improper Access Control - Generic | high | $0 | [Missing server side controls when editing the board’s sharing permissions per user](827816-missing-server-side-controls-when-editing-the-board-s-sharin.md) |
| 922470 | Business Logic Errors | low | $0 | [No rate limiting on sinup page](922470-no-rate-limiting-on-sinup-page.md) |
| 952349 | Improper Restriction of Authentication Attempts | medium | $0 | [Possible denial of service when entering a loooong password](952349-possible-denial-of-service-when-entering-a-loooong-password.md) |
| 167481 | Information Disclosure | n/a | $0 | [Android - Possible to intercept broadcasts about uploaded files](167481-android-possible-to-intercept-broadcasts-about-uploaded-file.md) |
| 3303283 | Server-Side Request Forgery (SSRF) | medium | $0 | [Unauthenticated blind SSRF in Circles signature verification bypasses Nextcloud local-address protections](3303283-unauthenticated-blind-ssrf-in-circles-signature-verification.md) |
| 1895874 | Server-Side Request Forgery (SSRF) | medium | $0 | [Responsive Server-side Request Forgery (SSRF)](1895874-responsive-server-side-request-forgery-ssrf.md) |
| 1916565 | Twitter Account hijack @nextcloudfrance | medium | $0 | [Twitter Account hijack @nextcloudfrance](1916565-twitter-account-hijack-nextcloudfrance.md) |
| 1784310 | Privacy Violation | low | $0 | [Messages can still be seen on conversation after expiring when cron is misconfigured](1784310-messages-can-still-be-seen-on-conversation-after-expiring-wh.md) |
| 1706248 | Privacy Violation | medium | $0 | [Guests can continue to receive video streams from call after being removed from a conversation](1706248-guests-can-continue-to-receive-video-streams-from-call-after.md) |
| 1094063 | Improper Access Control - Generic | medium | $0 | [Take over a mail account due missing validation of account id](1094063-take-over-a-mail-account-due-missing-validation-of-account-i.md) |
| 867052 | Improper Access Control - Generic | medium | $0 | [Access Control: Inject tasks into other users decks](867052-access-control-inject-tasks-into-other-users-decks.md) |
| 696360 | Information Disclosure | low | $0 | [Exposing debug.log file leads to server full path disclosure](696360-exposing-debug-log-file-leads-to-server-full-path-disclosure.md) |
| 229599 | Email Spoofing Vulnerability from nextcloud. | high | $0 | [Email Spoofing Vulnerability from nextcloud.](229599-email-spoofing-vulnerability-from-nextcloud.md) |
| 1832126 | Improper Access Control - Generic | low | $0 | [Existance of calendars and addressbooks can be checked by unauthenticated users ](1832126-existance-of-calendars-and-addressbooks-can-be-checked-by-un.md) |
| 1913095 | Server-Side Request Forgery (SSRF) | low | $0 | [Blind SSRF as normal user from mailapp](1913095-blind-ssrf-as-normal-user-from-mailapp.md) |
| 1767503 | Insecure Storage of Sensitive Information | medium | $0 | [Reference caching can leak data to unauthorized users](1767503-reference-caching-can-leak-data-to-unauthorized-users.md) |
| 165229 | Privilege Escalation | medium | $0 | [Nextcloud 10.0 privilege escalation issue - Normal user can mask external storage shared by admin    ](165229-nextcloud-10-0-privilege-escalation-issue-normal-user-can-ma.md) |
| 508490 | Privacy Violation | medium | $0 | [Nextcloud domain and name of every user leaked to lookup server](508490-nextcloud-domain-and-name-of-every-user-leaked-to-lookup-ser.md) |
| 666557 | Violation of Secure Design Principles | low | $0 | [Content Spoofing /Text Injection in https://docs.nextcloud.com](666557-content-spoofing-text-injection-in-https-docs-nextcloud-com.md) |
| 633245 | Privilege Escalation | low | $0 | [Delete permission can be added on reshare](633245-delete-permission-can-be-added-on-reshare.md) |
| 261138 | Cross-site Scripting (XSS) - Stored | low | $0 | [Stored XSS in OAuth redirect URI ](261138-stored-xss-in-oauth-redirect-uri.md) |
| 168054 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [Unauthenticated Stored xss ](168054-unauthenticated-stored-xss.md) |
| 3334165 | Improper Authentication - Generic | low | $0 | [ Nextcloud Tables v1 Share Enumeration Without Authorization (Regression of CVE-2024-52507)](3334165-nextcloud-tables-v1-share-enumeration-without-authorization.md) |
| 1893186 | Cross-site Scripting (XSS) - Reflected | medium | $0 | [Reflected XSS vulnerability with full CSP bypass in Nextcloud installations using recommended bundle](1893186-reflected-xss-vulnerability-with-full-csp-bypass-in-nextclou.md) |
| 1720043 | Code Injection | medium | $0 | [Desktop client can be tricked into opening/executing local files when clicking a nc://open/ link](1720043-desktop-client-can-be-tricked-into-opening-executing-local-f.md) |
| 1736390 | Server-Side Request Forgery (SSRF) | low | $0 | [Mail app - blind SSRF via imapHost parameter](1736390-mail-app-blind-ssrf-via-imaphost-parameter.md) |
| 1450117 | Insecure Direct Object Reference (IDOR) | medium | $0 | [Nextcloud Deck : Possibility for anyone to add a stack with existing tasks on anyone's board](1450117-nextcloud-deck-possibility-for-anyone-to-add-a-stack-with-ex.md) |
| 1023787 | Cross-site Scripting (XSS) - Stored | low | $0 | [Stored XSS in markdown file with Nextcloud Talk using Internet Explorer](1023787-stored-xss-in-markdown-file-with-nextcloud-talk-using-intern.md) |
| 697959 | Only the file extensions are checked, not the MIME types as configured | medium | $0 | [Only the file extensions are checked, not the MIME types as configured](697959-only-the-file-extensions-are-checked-not-the-mime-types-as-c.md) |
| 222058 | Violation of Secure Design Principles | low | $0 | [Content Spoofing/Text Injection in https://demo.nextcloud.com](222058-content-spoofing-text-injection-in-https-demo-nextcloud-com.md) |
| 218733 | Design Issues on ( ███ ) Lead to show ( IPS of Users )  | medium | $0 | [Design Issues on ( ███ ) Lead to show ( IPS of Users ) ](218733-design-issues-on-lead-to-show-ips-of-users.md) |
| 3524971 | Information Disclosure | low | $0 | [Users with read-only access to a Nextcloud Table can enumerate its share recipients via the Tables API](3524971-users-with-read-only-access-to-a-nextcloud-table-can-enumera.md) |
| 3636758 | Improper Authentication - Generic | low | $0 | [Cross-room signaling injection enabling unauthorized force-mute](3636758-cross-room-signaling-injection-enabling-unauthorized-force-m.md) |
| 2047168 | Improper Access Control - Generic | medium | $0 | [Any (non-admin) user from an instance can destroy any (user and/or global) external filesystem](2047168-any-non-admin-user-from-an-instance-can-destroy-any-user-and.md) |
| 1806275 | Plaintext Storage of a Password | low | $0 | [Mail app stores cleartext password in database until OAUTH2 setup is done](1806275-mail-app-stores-cleartext-password-in-database-until-oauth2.md) |
| 1820864 | Uncontrolled Resource Consumption | low | $0 | [No password length restriction in reset password endpoint](1820864-no-password-length-restriction-in-reset-password-endpoint.md) |
| 1596059 | Uncontrolled Resource Consumption | low | $0 | [Missing character limitation allows to put generate a database error](1596059-missing-character-limitation-allows-to-put-generate-a-databa.md) |
| 1588562 | Uncontrolled Resource Consumption | low | $0 | [Missing length validation of user displayname allows to generate an SQL error](1588562-missing-length-validation-of-user-displayname-allows-to-gene.md) |
| 1604606 | Information Exposure Through Debug Information | low | $0 | [Information exposure in in guzzlehttp/guzzle (https://github.com/nextcloud/3rdparty/tree/master/guzzlehttp/guzzle)](1604606-information-exposure-in-in-guzzlehttp-guzzle-https-github-co.md) |
| 1200815 | Business Logic Errors | low | $0 | [Federated share accepting/declining is not logged in audit log](1200815-federated-share-accepting-declining-is-not-logged-in-audit-l.md) |
| 1596673 | Privacy Violation | low | $0 | [Lack of Brute force protection while joining video call in talk section which is password protected](1596673-lack-of-brute-force-protection-while-joining-video-call-in-t.md) |
| 896511 | Cross-site Scripting (XSS) - Stored | medium | $0 | [XSS in image metadata field](896511-xss-in-image-metadata-field.md) |
| 507172 | Improper Access Control - Generic | low | $0 | [Able to bypass "Device credentials" Lock](507172-able-to-bypass-device-credentials-lock.md) |
| 504731 | Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG) | medium | $0 | [ Predictable Random Number Generator](504731-predictable-random-number-generator.md) |
| 461308 | Deserialization of Untrusted Data | n/a | $0 | [Remote attacker can impersonate Social users via ActivityPub API](461308-remote-attacker-can-impersonate-social-users-via-activitypub.md) |
| 220946 | Information Disclosure | n/a | $0 | [https://portal.nextcloud.com/.htaccess file is readable](220946-https-portal-nextcloud-com-htaccess-file-is-readable.md) |
| 201489 | Wordpress 4.7.1 | low | $0 | [Wordpress 4.7.1](201489-wordpress-4-7-1.md) |
| 198012 | Information Disclosure | n/a | $0 | [Disclosure of administrators via JSON on nextcloud.com Wordpress](198012-disclosure-of-administrators-via-json-on-nextcloud-com-wordp.md) |
| 197878 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [WordPress <= 4.6.1 Stored XSS Via Theme File](197878-wordpress-4-6-1-stored-xss-via-theme-file.md) |
| 146424 | Violation of Secure Design Principles | n/a | $0 | [No Rate Limiting on stats.nextcloud.com login](146424-no-rate-limiting-on-stats-nextcloud-com-login.md) |
| 3772818 | Code Injection | low | $0 | [Code injection allows unprivileged local attacker to execute arbitrary code in Nextcloud's OAuth/web renderer process](3772818-code-injection-allows-unprivileged-local-attacker-to-execute.md) |
| 2052795 | Improper Authentication - Generic | n/a | $0 | [No Rate Limit On Forgot Password on https://apps.nextcloud.com](2052795-no-rate-limit-on-forgot-password-on-https-apps-nextcloud-com.md) |
| 1745755 | Improper Access Control - Generic | low | $0 | [Hide download previews are accessible without a watermark](1745755-hide-download-previews-are-accessible-without-a-watermark.md) |
| 1746582 | Server-Side Request Forgery (SSRF) | low | $0 | [Mail app - blind SSRF via smtpHost parameter](1746582-mail-app-blind-ssrf-via-smtphost-parameter.md) |
| 1741525 | Server-Side Request Forgery (SSRF) | low | $0 | [Mail app - Blind SSRF via Sierve server fonctionnality and sieveHost parameter](1741525-mail-app-blind-ssrf-via-sierve-server-fonctionnality-and-sie.md) |
| 1712329 | Improper Authentication - Generic | n/a | $0 | [[nextcloud/server] Moment.js vulnerable to Inefficient Regular Expression Complexity](1712329-nextcloud-server-moment-js-vulnerable-to-inefficient-regular.md) |
| 388527 | Cross-site Scripting (XSS) - Generic | low | $0 | [Self xss](388527-self-xss.md) |
| 476526 | Violation of Secure Design Principles | medium | $0 | [WordPress vulnerable to multiple attacks at https://nextcloud.com](476526-wordpress-vulnerable-to-multiple-attacks-at-https-nextcloud.md) |
| 761329 | Improper Access Control - Generic | medium | $0 | [Update App Store: Django account high jacking vulnerability](761329-update-app-store-django-account-high-jacking-vulnerability.md) |
| 498878 | User Editable nextcloud Wiki pages of Public Repositories | high | $0 | [User Editable nextcloud Wiki pages of Public Repositories](498878-user-editable-nextcloud-wiki-pages-of-public-repositories.md) |
| 522876 | Improper Access Control - Generic | high | $0 | [In Dockerized Environments, Failing to Read config.php Grants Any Anonymous User Full Admin Access](522876-in-dockerized-environments-failing-to-read-config-php-grants.md) |
| 341372 | Information Disclosure | medium | $0 | [The session token in the URL](341372-the-session-token-in-the-url.md) |
| 226037 | Wordpress Vulnerable to Potential Unauthorized Password Reset | low | $0 | [Wordpress Vulnerable to Potential Unauthorized Password Reset](226037-wordpress-vulnerable-to-potential-unauthorized-password-rese.md) |
| 213056 | Violation of Secure Design Principles | n/a | $0 | [Invalid request may lead content spoofing for phishing](213056-invalid-request-may-lead-content-spoofing-for-phishing.md) |
| 171497 | Violation of Secure Design Principles | low | $0 | [Content spoofing in lookup.nextcloud.com](171497-content-spoofing-in-lookup-nextcloud-com.md) |
| 3943436 | Business Logic Errors | low | $0 | [Unauthenticated attacker can book appointments at arbitrary times, including outside availability and in the past](3943436-unauthenticated-attacker-can-book-appointments-at-arbitrary.md) |
| 1765631 | Path Traversal: 'dir\..\..\filename' | medium | $0 | [Potential directory traversal in OC\Files\Node\Folder::getFullPath](1765631-potential-directory-traversal-in-oc-files-node-folder-getful.md) |
| 1788222 | Improper Access Control - Generic | medium | $0 | [Document content of files can be obtained through Collabora for files of other users](1788222-document-content-of-files-can-be-obtained-through-collabora.md) |
| 1699740 | Improper Certificate Validation | low | $0 | [nextcloudcmd incorrectly trusts bad TLS certificates](1699740-nextcloudcmd-incorrectly-trusts-bad-tls-certificates.md) |
| 1641088 | Privacy Violation | medium | $0 | [Last video frame is still sent after video is disabled in a call](1641088-last-video-frame-is-still-sent-after-video-is-disabled-in-a.md) |
| 1153138 | Uncontrolled Resource Consumption | medium | $0 | [Improper input-size validation on the user new session name can result in server-side DDoS.](1153138-improper-input-size-validation-on-the-user-new-session-name.md) |
| 1390331 | SQL Injection | high | $0 | [SQL injextion via vulnerable doctrine/dbal version](1390331-sql-injextion-via-vulnerable-doctrine-dbal-version.md) |
| 1261225 | Incorrect Calculation of Buffer Size | low | $0 | [High memory usage for generating preview of broken image](1261225-high-memory-usage-for-generating-preview-of-broken-image.md) |
| 1332433 | Code Injection | critical | $0 | [RCE on 17 different Docker containers on your network](1332433-rce-on-17-different-docker-containers-on-your-network.md) |
| 1200810 | Admin audit is not properly logging unsetting of expiration date | low | $0 | [Admin audit is not properly logging unsetting of expiration date](1200810-admin-audit-is-not-properly-logging-unsetting-of-expiration.md) |
| 1039805 | Clickjacking URLS | n/a | $0 | [Clickjacking URLS](1039805-clickjacking-urls.md) |
| 681468 | Improper Restriction of Authentication Attempts | n/a | $0 | [The password recovery let users know whether an email address exists or not in the website](681468-the-password-recovery-let-users-know-whether-an-email-addres.md) |
| 317711 | Improper Authentication - Generic | low | $0 | [twofactor_auth bypassable if provider fails to load](317711-twofactor-auth-bypassable-if-provider-fails-to-load.md) |
| 221298 | Information Disclosure | n/a | $0 | [GIT Detected](221298-git-detected.md) |
| 196878 | Information Disclosure | medium | $0 | [bug reporting template encourages users to paste config file with passwords](196878-bug-reporting-template-encourages-users-to-paste-config-file.md) |
| 192786 | Cross-site Scripting (XSS) - Generic | high | $0 | [Reflected XSS in U2F plugin by shipping the example endpoints](192786-reflected-xss-in-u2f-plugin-by-shipping-the-example-endpoint.md) |
| 199286 | Group admin can remove user from all his groups via API | none | $0 | [Group admin can remove user from all his groups via API](199286-group-admin-can-remove-user-from-all-his-groups-via-api.md) |
| 145950 | Improper Authentication - Generic | n/a | $0 | [Uploading files to a folder where invited user don't have any EDIT privilege](145950-uploading-files-to-a-folder-where-invited-user-don-t-have-an.md) |
| 145727 | Improper Authentication - Generic | n/a | $0 | [Bruteforcing help.nextcloud.com](145727-bruteforcing-help-nextcloud-com.md) |
| 3511955 | Improper Access Control - Generic | medium | $0 | [Unauthorized users can enumerate internal team resources via the Teams API when a team is visible to everyone](3511955-unauthorized-users-can-enumerate-internal-team-resources-via.md) |
| 3533697 | Improper Access Control - Generic | low | $0 | [Public collectives allow to create pages](3533697-public-collectives-allow-to-create-pages.md) |
| 1901396 | Uncontrolled Resource Consumption | medium | $0 | [Dos in Form Submission at https://nextcloud.com/instant-trial/](1901396-dos-in-form-submission-at-https-nextcloud-com-instant-trial.md) |
| 1808079 | Improper Access Control - Generic | medium | $0 | [Permissions not respected when copying entire group folders](1808079-permissions-not-respected-when-copying-entire-group-folders.md) |
| 1913951 | No rate limit while adding Additional emails feature | low | $0 | [No rate limit while adding Additional emails feature](1913951-no-rate-limit-while-adding-additional-emails-feature.md) |
| 1708873 | Cleartext Transmission of Sensitive Information | n/a | $0 | [Vulnerable moment-timezone version shipped](1708873-vulnerable-moment-timezone-version-shipped.md) |
| 1338781 | Information Disclosure | medium | $0 | [User files is disclosed when someone called while the screen is locked](1338781-user-files-is-disclosed-when-someone-called-while-the-screen.md) |
| 1202590 | Improper Access Control - Generic | medium | $0 | [Webauthn tokens are not removed on user deletion](1202590-webauthn-tokens-are-not-removed-on-user-deletion.md) |
| 1167958 | Improper Access Control - Generic | low | $0 | [Nextcloud deck sharee search leaks searches to lookupserver by default](1167958-nextcloud-deck-sharee-search-leaks-searches-to-lookupserver.md) |
| 661051 | Violation of Secure Design Principles | low | $0 | [Message Authentication Codes calculated by the Default Encryption Module allow an attacker to silently overwrite blocks in a file](661051-message-authentication-codes-calculated-by-the-default-encry.md) |
| 852841 | Cryptographic Issues - Generic | low | $0 | [Reduced purmations on encryption](852841-reduced-purmations-on-encryption.md) |
| 820146 | PHPUnit is included in groupfolders release package potentially causing RCE | n/a | $0 | [PHPUnit is included in groupfolders release package potentially causing RCE](820146-phpunit-is-included-in-groupfolders-release-package-potentia.md) |
| 889795 | Improper Access Control - Generic | none | $0 | [Allows any user to share their "Root" level folder by sharing "."](889795-allows-any-user-to-share-their-root-level-folder-by-sharing.md) |
| 803734 | Improper Certificate Validation | medium | $0 | [Mail does not verify IMAP/SMTP host connected via TLS](803734-mail-does-not-verify-imap-smtp-host-connected-via-tls.md) |
| 244092 | Plaintext Storage of a Password | high | $0 | [Password of failed (2FA) login attempt is stored in log](244092-password-of-failed-2fa-login-attempt-is-stored-in-log.md) |
| 631227 | Code Injection | none | $0 | [Some HTML Tags are Getting Executed in com.nextcloud.client](631227-some-html-tags-are-getting-executed-in-com-nextcloud-client.md) |
| 166581 | Privilege Escalation | high | $0 | [Privilege escalation - Normal user can somehow make admin to delete shared folders](166581-privilege-escalation-normal-user-can-somehow-make-admin-to-d.md) |
| 169680 | Privilege Escalation | medium | $0 | [Bypass permissions](169680-bypass-permissions.md) |
| 187460 | Information Disclosure | low | $0 | [Files Drop: WebDAV endpoint is leaking existence of resources](187460-files-drop-webdav-endpoint-is-leaking-existence-of-resources.md) |
| 163338 | Cross-site Scripting (XSS) - Generic | medium | $0 | [\OCA\DAV\CardDAV\ImageExportPlugin allows serving arbitrary data with user-defined or empty mimetype](163338-oca-dav-carddav-imageexportplugin-allows-serving-arbitrary-d.md) |
| 161924 | Improper Authentication - Generic | n/a | $0 | [Password Reset Link issue](161924-password-reset-link-issue.md) |
| 145734 | Information Disclosure | n/a | $0 | [help.nextcloud Email Address/Username enumeration](145734-help-nextcloud-email-address-username-enumeration.md) |
| 3159877 | Information Disclosure | none | $0 | [Information disclosure via Desktop client when attempting to lock a file inside a end-to-end encrypted directory ](3159877-information-disclosure-via-desktop-client-when-attempting-to.md) |
| 1924355 | Cross-site Scripting (XSS) - Reflected | low | $0 | [Notes attachments render HTML in preview mode](1924355-notes-attachments-render-html-in-preview-mode.md) |
| 1402249 | CRLF Injection | medium | $0 | [Control character filtering misses leading and trailing whitespace in file and folder names](1402249-control-character-filtering-misses-leading-and-trailing-whit.md) |
| 1337178 | Business Logic Errors | medium | $0 | [objectId in share location can be set to open arbitrary URL or Deeplinks](1337178-objectid-in-share-location-can-be-set-to-open-arbitrary-url.md) |
| 1061591 | Improper Access Control - Generic | high | $0 | [Acting under any different user via DB-stored credentials](1061591-acting-under-any-different-user-via-db-stored-credentials.md) |
| 921717 | Improper Access Control - Generic | medium | $0 | [Improper access control to messages of Social app](921717-improper-access-control-to-messages-of-social-app.md) |
| 220385 | Delete All Data of Any User | low | $0 | [Delete All Data of Any User](220385-delete-all-data-of-any-user.md) |
| 690796 | Information Exposure Through Directory Listing | low | $0 | [Directory listing is enabled that exposes non public data through multiple path ](690796-directory-listing-is-enabled-that-exposes-non-public-data-th.md) |
| 625199 | Information Disclosure | high | $0 | [Wordpress Users Disclosure](625199-wordpress-users-disclosure.md) |
| 504759 | Uncontrolled Resource Consumption | n/a | $0 | [Uploading large avatar images cause excessive CPU usage](504759-uploading-large-avatar-images-cause-excessive-cpu-usage.md) |
| 457032 | Improper Access Control - Generic | medium | $0 | [Github wikis are editable by anyone ](457032-github-wikis-are-editable-by-anyone.md) |
| 199714 | Improper Authentication - Generic | low | $0 | [Missing Rate Limit for Current Password field in nextcloud.com](199714-missing-rate-limit-for-current-password-field-in-nextcloud-c.md) |
| 213789 | Cryptographic Issues - Generic | low | $0 | [Update php-saml library to 2.10.5](213789-update-php-saml-library-to-2-10-5.md) |
| 197877 | Information Disclosure | n/a | $0 | [User Information Disclosure via REST API](197877-user-information-disclosure-via-rest-api.md) |
| 153905 | Privilege Escalation | low | $0 | [IDOR - Disable sharing](153905-idor-disable-sharing.md) |
| 149798 | Violation of Secure Design Principles | low | $0 | [Content (Text) Injection at NextCloud Server 9.0.52 - via http://custom_nextcloud_url/remote.php/dav/files/ ](149798-content-text-injection-at-nextcloud-server-9-0-52-via-http-c.md) |
| 4004074 | Privilege Escalation | medium | $0 | [Nextcloud subadmin → admin takeover when allowed_admin_ranges is set: SubAdmin::isUserAccessible() classifies the admin target via IP-gated isAdmin()](4004074-nextcloud-subadmin-admin-takeover-when-allowed-admin-ranges.md) |
| 1579820 | Insecure Direct Object Reference (IDOR) | medium | $0 | [Ownership check missing when updating or deleting attachments](1579820-ownership-check-missing-when-updating-or-deleting-attachment.md) |
| 1210458 | Serverinfo endpoints are not bruteforce protected nor are tokens properly generated | low | $0 | [Serverinfo endpoints are not bruteforce protected nor are tokens properly generated](1210458-serverinfo-endpoints-are-not-bruteforce-protected-nor-are-to.md) |
| 1167919 | Improper Access Control - Generic | low | $0 | [Default Nextcloud server config and iOS Nextcloud client leak sharee searches to Nextcloud](1167919-default-nextcloud-server-config-and-ios-nextcloud-client-lea.md) |
| 1167767 | Improper Access Control - Generic | medium | $0 | [Unexpected federated shares added via public link](1167767-unexpected-federated-shares-added-via-public-link.md) |
| 1169335 | Weak Cryptography for Passwords | low | $0 | [Password policy changes not enforced for existing passwords](1169335-password-policy-changes-not-enforced-for-existing-passwords.md) |
| 888261 | Improper Access Control - Generic | low | $0 | [The password of a mail share is not set if the password is given when the share is created (Nextcloud < 18)](888261-the-password-of-a-mail-share-is-not-set-if-the-password-is-g.md) |
| 906322 | Improper Access Control - Generic | n/a | $0 | [Github wikis are editable by anyone https://github.com/nextcloud/bookmarks/wiki](906322-github-wikis-are-editable-by-anyone-https-github-com-nextclo.md) |
| 261297 | Violation of Secure Design Principles | none | $0 | [Disabled user can reset their password  ](261297-disabled-user-can-reset-their-password.md) |
| 331302 | Improper Access Control - Generic | low | $0 | [Improper protection of FileContentProvider](331302-improper-protection-of-filecontentprovider.md) |
| 228825 | Code Injection | critical | $0 | [(Authenticated) RCE by bypassing of the .htaccess blacklist](228825-authenticated-rce-by-bypassing-of-the-htaccess-blacklist.md) |
| 746541 | Server-Side Request Forgery (SSRF) | medium | $0 | [SSRF on local storage of iOS mobile](746541-ssrf-on-local-storage-of-ios-mobile.md) |
| 347782 | UI Redressing (Clickjacking) | low | $0 | [Click Jacking Nextcloud](347782-click-jacking-nextcloud.md) |
| 476615 | Information Disclosure | low | $0 | [Private/confidential setting of calendar events is ignored on activity stream](476615-private-confidential-setting-of-calendar-events-is-ignored-o.md) |
| 271253 | Improper Authentication - Generic | n/a | $0 | [NextCloud is also Accepting OCTET-STREAM Type of Documents instead of jpg or Imge Files Only](271253-nextcloud-is-also-accepting-octet-stream-type-of-documents-i.md) |
| 358339 | Improper Access Control - Generic | low | $0 | [File access control rules not enforced on image files](358339-file-access-control-rules-not-enforced-on-image-files.md) |
| 308156 | Email Notification should be get while changing password on apps.nextcloud.com | n/a | $0 | [Email Notification should be get while changing password on apps.nextcloud.com](308156-email-notification-should-be-get-while-changing-password-on.md) |
| 269705 | Violation of Secure Design Principles | low | $0 | [WordPress < 4.8.2 vulnerable to multiple attacks](269705-wordpress-4-8-2-vulnerable-to-multiple-attacks.md) |
| 157434 | Cross-site Scripting (XSS) - Stored | low | $0 | [XSS on IOS app via HTML rendering](157434-xss-on-ios-app-via-html-rendering.md) |
| 173721 | Cross-site Scripting (XSS) - Generic | medium | $0 | [Bad content-type in response header when getting document can lead to html injection](173721-bad-content-type-in-response-header-when-getting-document-ca.md) |
| 145896 | Improper Authentication - Generic | n/a | $0 | [Password reset link remains valid after email change](145896-password-reset-link-remains-valid-after-email-change.md) |
| 165686 | Cross-site Scripting (XSS) - Generic | medium | $0 | [Reflected XSS in Gallery App](165686-reflected-xss-in-gallery-app.md) |
| 163421 | Information Disclosure | n/a | $0 | [Wordpress: Directory Traversal / Denial of Serivce](163421-wordpress-directory-traversal-denial-of-serivce.md) |
| 163342 | Violation of Secure Design Principles | n/a | $0 | [Expired SSL certificate ](163342-expired-ssl-certificate.md) |
| 3642236 | Improper Access Control - Generic | medium | $0 | [Tables application does not respect sharing limitations set by admin](3642236-tables-application-does-not-respect-sharing-limitations-set.md) |
| 1781751 | Violation of Secure Design Principles | low | $0 | [Ability to control the filename when uploading a logo or favicon on theming](1781751-ability-to-control-the-filename-when-uploading-a-logo-or-fav.md) |
| 1169033 | Phishing | medium | $0 | [Targeted phishing attacks in Login flow v2](1169033-targeted-phishing-attacks-in-login-flow-v2.md) |
| 1726445 | A vulnerability classified as critical has been found in gsi-openssh-server 7.9p1 on Fedora (Connectivity Software) on server (http://95.217.64.181:22 | low | $0 | [A vulnerability classified as critical has been found in gsi-openssh-server 7.9p1 on Fedora (Connectivity Software) on server (http://95.217.64.181:22](1726445-a-vulnerability-classified-as-critical-has-been-found-in-gsi.md) |
| 1354334 | Information Disclosure | low | $0 | [Error in Deleting Deck cards attachment reveals the full path of the website](1354334-error-in-deleting-deck-cards-attachment-reveals-the-full-pat.md) |
| 1246721 | Information Disclosure | low | $0 | [Text app leaks file path of shared files](1246721-text-app-leaks-file-path-of-shared-files.md) |
| 1241460 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [ApiService#fetch serves content as text/html and inline Content-Disposition](1241460-apiservice-fetch-serves-content-as-text-html-and-inline-cont.md) |
| 859136 | Malicious apps can crash Nextcloud Android client by sending malformed intents  | n/a | $0 | [Malicious apps can crash Nextcloud Android client by sending malformed intents ](859136-malicious-apps-can-crash-nextcloud-android-client-by-sending.md) |
| 1102780 | Improper Access Control - Generic | high | $0 | [bypassing dashboard without account + Information disclosure trough websockets ](1102780-bypassing-dashboard-without-account-information-disclosure-t.md) |
| 1108420 | Cross-site Scripting (XSS) - Generic | low | $0 | [HTML Injection on "polls" app - comments section (possibly XSS)](1108420-html-injection-on-polls-app-comments-section-possibly-xss.md) |
| 928280 | Code Injection | medium | $0 | [Formula Injection vulnerability in CSV export feature](928280-formula-injection-vulnerability-in-csv-export-feature.md) |
| 794407 | Insufficiently Protected Credentials | high | $0 | [nextcloud-snap CircleCI project has vulnerable configuration which can lead to exposing secrets](794407-nextcloud-snap-circleci-project-has-vulnerable-configuration.md) |
| 1018146 | Uncontrolled Resource Consumption | medium | $0 | [Potential DDoS when posting long data into workflow validation rules](1018146-potential-ddos-when-posting-long-data-into-workflow-validati.md) |
| 1022211 | Leaked of Profile Image from URL changing | n/a | $0 | [Leaked of Profile Image from URL changing](1022211-leaked-of-profile-image-from-url-changing.md) |
| 986459 | Improper Authentication - Generic | high | $0 | [Recently change email but still login with old email](986459-recently-change-email-but-still-login-with-old-email.md) |
| 225777 | Cross-site Scripting (XSS) - Generic | low | $0 | [DOMPurify 0.8.9 released](225777-dompurify-0-8-9-released.md) |
| 385037 | Missing SPF flags for customerupdates.nextcloud.com | medium | $0 | [Missing SPF flags for customerupdates.nextcloud.com](385037-missing-spf-flags-for-customerupdates-nextcloud-com.md) |
| 439828 | Event privacy level does not work in Thunderbird | medium | $0 | [Event privacy level does not work in Thunderbird](439828-event-privacy-level-does-not-work-in-thunderbird.md) |
| 793532 | Phishing | medium | $0 | [Email Spoofing](793532-email-spoofing.md) |
| 231524 | Cross-site Scripting (XSS) - Stored | low | $0 | [HTML injection and limited XSS via logo image upload - Nextcloud 12.0.0](231524-html-injection-and-limited-xss-via-logo-image-upload-nextclo.md) |
| 225098 | Information Exposure Through an Error Message | low | $0 | [SQL exception in JSON format](225098-sql-exception-in-json-format.md) |
| 631206 | Violation of Secure Design Principles | medium | $0 | [Passcode Protection in Android Devices Can be Bypassed.](631206-passcode-protection-in-android-devices-can-be-bypassed.md) |
| 478957 | Cross-site Scripting (XSS) - Stored | medium | $0 | [Stored XSS/HTML injection in autocomplete suggestions for sharing](478957-stored-xss-html-injection-in-autocomplete-suggestions-for-sh.md) |
| 214340 | Content spoofing due to the improper behavior of the 403 page | n/a | $0 | [Content spoofing due to the improper behavior of the 403 page](214340-content-spoofing-due-to-the-improper-behavior-of-the-403-pag.md) |
| 213360 | Violation of Secure Design Principles | low | $0 | [Content Spoofing/Text Injection in nextcloud.com](213360-content-spoofing-text-injection-in-nextcloud-com.md) |
| 145604 | Violation of Secure Design Principles | n/a | $0 | [Avatar image upload and bypass  real image verification ](145604-avatar-image-upload-and-bypass-real-image-verification.md) |
| 145452 | Improper Authentication - Generic | n/a | $0 | [Share owner has no possibility to list all existing derived shares](145452-share-owner-has-no-possibility-to-list-all-existing-derived.md) |
| 188132 | Information Disclosure | low | $0 | [Wordpress Version Disclosure Bug On Nextcloud](188132-wordpress-version-disclosure-bug-on-nextcloud.md) |
| 156510 | Information Disclosure | n/a | $0 | [Directory listening enabled in: 88.198.160.130](156510-directory-listening-enabled-in-88-198-160-130.md) |
| 2050059 | Information Disclosure | none | $0 | [Nextcloud All-In-One path disclosure of internal frontend](2050059-nextcloud-all-in-one-path-disclosure-of-internal-frontend.md) |
| 1697281 | Use of Incorrectly-Resolved Name or Reference | medium | $0 | [Name collision of shared folders](1697281-name-collision-of-shared-folders.md) |
| 1690510 | Improper Removal of Sensitive Information Before Storage or Transfer | low | $0 | [the complete server installation path is visible in cloud/user endpoint](1690510-the-complete-server-installation-path-is-visible-in-cloud-us.md) |
| 1745702 | Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG) | low | $0 | [Insecure randomness for default password in file sharing when password policy app is disabled](1745702-insecure-randomness-for-default-password-in-file-sharing-whe.md) |
| 1596148 | Uncontrolled Resource Consumption | low | $0 | [Calendar name length not validated before writing to database](1596148-calendar-name-length-not-validated-before-writing-to-databas.md) |
| 1711847 | Resource Injection | low | $0 | [XSS in Desktop Client in call notification popup](1711847-xss-in-desktop-client-in-call-notification-popup.md) |
| 1707977 | Resource Injection | low | $0 | [XSS in Desktop Client via user status and information](1707977-xss-in-desktop-client-via-user-status-and-information.md) |
| 1129996 | Improper Access Control - Generic | medium | $0 | [Create alias does not validate account id](1129996-create-alias-does-not-validate-account-id.md) |
| 1195593 | Talk discloses turn server to anybody | low | $0 | [Talk discloses turn server to anybody](1195593-talk-discloses-turn-server-to-anybody.md) |
| 855304 | Improper Restriction of Authentication Attempts | n/a | $0 | [No set limit to try to login in "https://auth.nextcloud.com/auth/realms/master/protocol/openid-connect/auth" page.](855304-no-set-limit-to-try-to-login-in-https-auth-nextcloud-com-aut.md) |
| 1081211 | Improper Access Control - Generic | medium | $0 | [[nextcloud.com] Control character allowed in Submit Question](1081211-nextcloud-com-control-character-allowed-in-submit-question.md) |
| 742588 | Cryptographic Issues - Generic | medium | $0 | [Downgrade encryption scheme and break integrity through known-plaintext attack](742588-downgrade-encryption-scheme-and-break-integrity-through-know.md) |
| 229170 | UI Redressing (Clickjacking) | medium | $0 | [RTLO character allowed in shared files](229170-rtlo-character-allowed-in-shared-files.md) |
| 752353 | Information Disclosure | n/a | $0 | [Anonymous file drop page ignores user profile visibility restrictions](752353-anonymous-file-drop-page-ignores-user-profile-visibility-res.md) |
| 678727 | Code Injection | high | $0 | [potential RCE and XSS via file upload requiring user account and default settings](678727-potential-rce-and-xss-via-file-upload-requiring-user-account.md) |
| 237232 | Information Disclosure | medium | $0 | [Unauthenticated 'display name' information leak on enumeration of login names](237232-unauthenticated-display-name-information-leak-on-enumeration.md) |
| 722748 | Improper Authentication - Generic | medium | $0 | [Bypass configured 2FA provider with another provider that can be set up at login](722748-bypass-configured-2fa-provider-with-another-provider-that-ca.md) |
| 509390 | Man-in-the-Middle | medium | $0 | [Missing DNSSEC](509390-missing-dnssec.md) |
| 205908 | Improper Authentication - Generic | none | $0 | [LDAP login possible even though account doesn't match user filter](205908-ldap-login-possible-even-though-account-doesn-t-match-user-f.md) |
| 579116 | Cross-Site Request Forgery (CSRF) | medium | $0 | [Vulnerable W3 Total Cache plugin version in use on nextcloud.com](579116-vulnerable-w3-total-cache-plugin-version-in-use-on-nextcloud.md) |
| 383117 | Cross-site Scripting (XSS) - Generic | none | $0 | [HTML injection with AutoComplete suggestions](383117-html-injection-with-autocomplete-suggestions.md) |
| 269449 | Information Disclosure | n/a | $0 | [Banner Grabbing - Apache Server Version Disclousure](269449-banner-grabbing-apache-server-version-disclousure.md) |
| 145343 | Command Injection - Generic | n/a | $0 | [Possible RCE](145343-possible-rce.md) |
| 224927 | Violation of Secure Design Principles | medium | $0 | [Missing Rate Limiting protection leading to mass triggering of e-mails](224927-missing-rate-limiting-protection-leading-to-mass-triggering.md) |
| 174896 | Privilege Escalation | medium | $0 | [Dav sharing permissions issue](174896-dav-sharing-permissions-issue.md) |
| 212770 | Violation of Secure Design Principles | n/a | $0 | [Content spoofing due to the improper behavior of the 403 page](212770-content-spoofing-due-to-the-improper-behavior-of-the-403-pag.md) |
| 211206 | Version 4.7.2 of wordpress is vulnerable | high | $0 | [Version 4.7.2 of wordpress is vulnerable](211206-version-4-7-2-of-wordpress-is-vulnerable.md) |
| 198773 | Drone Nextcloud | n/a | $0 | [Drone Nextcloud](198773-drone-nextcloud.md) |
| 205250 | Violation of Secure Design Principles | n/a | $0 | [Missing SPF Flags on nextcloud.com](205250-missing-spf-flags-on-nextcloud-com.md) |
| 198673 | Violation of Secure Design Principles | n/a | $0 | [HTTP-Basic Authentication on logs.nextcloud.com](198673-http-basic-authentication-on-logs-nextcloud-com.md) |
| 175085 | Violation of Secure Design Principles | n/a | $0 | [URI scheme bypass in mail app lead to HTML content spoof and opener control](175085-uri-scheme-bypass-in-mail-app-lead-to-html-content-spoof-and.md) |
| 163106 | Information Disclosure | n/a | $0 | [Information Disclosure of .htaccess file in Private Server/Subdomain](163106-information-disclosure-of-htaccess-file-in-private-server-su.md) |
| 146106 | Information Disclosure | n/a | $0 | [Email ID Disclosure.](146106-email-id-disclosure.md) |
| 145745 | Privilege Escalation | n/a | $0 | [Business/Functional logic bypass: Remove admins from admin group.](145745-business-functional-logic-bypass-remove-admins-from-admin-gr.md) |
| 145517 | Information Disclosure | n/a | $0 | [Vulnerable Javascript library](145517-vulnerable-javascript-library.md) |
| 145344 | Violation of Secure Design Principles | n/a | $0 | [nextcloud.com: Content Injection  Custom 404 Error](145344-nextcloud-com-content-injection-custom-404-error.md) |
| 3682163 | Improper Access Control - Generic | medium | $0 | [Files Confidential tagging can be bypassed with # in filename ](3682163-files-confidential-tagging-can-be-bypassed-with-in-filename.md) |
| 1954711 | Improper Restriction of Authentication Attempts | medium | $0 | [user_oidc app is missing bruteforce protection](1954711-user-oidc-app-is-missing-bruteforce-protection.md) |
| 1806223 | Uncontrolled Resource Consumption | medium | $0 | [Reference fetch can saturate the server bandwidth for 10 seconds](1806223-reference-fetch-can-saturate-the-server-bandwidth-for-10-sec.md) |
| 1794462 | Website PHP source code returned in javascript | medium | $0 | [Website PHP source code returned in javascript](1794462-website-php-source-code-returned-in-javascript.md) |
| 1652903 | Cleartext Storage of Sensitive Information | medium | $0 | [Exception logging in Sharepoint app reveals clear-text connection details](1652903-exception-logging-in-sharepoint-app-reveals-clear-text-conne.md) |
| 1596918 | Privacy Violation | low | $0 | [Brute force protections don't work](1596918-brute-force-protections-don-t-work.md) |
| 1607601 | Uncontrolled Resource Consumption | low | $0 | [@nextcloud/logger NPM package brings vulnerable ansi-regex version](1607601-nextcloud-logger-npm-package-brings-vulnerable-ansi-regex-ve.md) |
| 1214158 | Improper Restriction of Authentication Attempts | none | $0 | [Ratelimits do not apply to OCS DataResponse](1214158-ratelimits-do-not-apply-to-ocs-dataresponse.md) |
| 1200989 | No admin audit entry for enabling/disabling 2FA | low | $0 | [No admin audit entry for enabling/disabling 2FA](1200989-no-admin-audit-entry-for-enabling-disabling-2fa.md) |
| 1147611 | Uncontrolled Resource Consumption | high | $0 | [DoS due to improper input validation can break the admin access into the user data will disallow him from editing that user's data.](1147611-dos-due-to-improper-input-validation-can-break-the-admin-acc.md) |
| 915585 | Improper Certificate Validation | medium | $0 | [Social App does not validate server certificates for outgoing connections](915585-social-app-does-not-validate-server-certificates-for-outgoin.md) |
| 924393 | Improper Authentication - Generic | medium | $0 | [PIN for passwordless WebAuthn is asked for but not verified](924393-pin-for-passwordless-webauthn-is-asked-for-but-not-verified.md) |
| 919429 | Information Disclosure | n/a | $0 | [Full path disclosure vulnerability  via Upload .htaccess file](919429-full-path-disclosure-vulnerability-via-upload-htaccess-file.md) |
| 390728 | Cross-site Scripting (XSS) - Stored | low | $0 | [Stored XSS on scan.nextcloud.com](390728-stored-xss-on-scan-nextcloud-com.md) |
| 664200 | Business Logic Errors | n/a | $0 | [SignUp using Fake Email](664200-signup-using-fake-email.md) |
| 358102 | Information Disclosure | low | $0 | [Disclosed Version of PORTS SSH\|HTTP\|SSL](358102-disclosed-version-of-ports-ssh-http-ssl.md) |
| 348801 | Information Disclosure | n/a | $0 | [Banner Grabbing - Apache Server Version Disclosure](348801-banner-grabbing-apache-server-version-disclosure.md) |
| 260221 | Information Exposure Through Directory Listing | none | $0 | [Information Exposure Through Directory Listing](260221-information-exposure-through-directory-listing.md) |
| 222762 | UI Redressing (Clickjacking) | critical | $0 | [Clickjacking In https://demo.nextcloud.com](222762-clickjacking-in-https-demo-nextcloud-com.md) |
| 226896 | Nextcloud Server Remote Command Execution | high | $0 | [Nextcloud Server Remote Command Execution](226896-nextcloud-server-remote-command-execution.md) |
| 222080 | Improper Access Control - Generic | low | $0 | [The email API to reset password is unlimited and can be used as a email bomb](222080-the-email-api-to-reset-password-is-unlimited-and-can-be-used.md) |
| 152499 | Information Disclosure | n/a | $0 | [Information disclosure](152499-information-disclosure.md) |
| 213358 | Server-Side Request Forgery (SSRF) | n/a | $0 | [SSRF at apps.nextcloud.com/developer/apps/releases/new](213358-ssrf-at-apps-nextcloud-com-developer-apps-releases-new.md) |
| 173622 | Privilege Escalation | none | $0 | [Bypassing quota limit ](173622-bypassing-quota-limit.md) |
| 194564 | Code Injection | none | $0 | [Review remote code execution in SwiftMailer](194564-review-remote-code-execution-in-swiftmailer.md) |
| 174524 | Uncontrolled Resource Consumption | low | $0 | [Filename enumeration && DoS](174524-filename-enumeration-dos.md) |
| 200762 | Violation of Secure Design Principles | n/a | $0 | [Email Spoofing](200762-email-spoofing.md) |
| 190870 | Cross-site Scripting (XSS) - Generic | high | $0 | [Stored XSS on new Calling plugin (spreed)](190870-stored-xss-on-new-calling-plugin-spreed.md) |
| 148897 | Cross-site Scripting (XSS) - Generic | medium | $0 | [[Thirdparty] Stored XSS in chat module - nextcloud server 9.0.51 installed in ubuntu 14.0.4 LTS](148897-thirdparty-stored-xss-in-chat-module-nextcloud-server-9-0-51.md) |
| 177335 | Violation of Secure Design Principles | none | $0 | [Content spoofing due to the improper behavior of the 403 page in Private Server](177335-content-spoofing-due-to-the-improper-behavior-of-the-403-pag.md) |
| 154529 | Privilege Escalation | n/a | $0 | [Bookmarks: Delete all existing bookmarks of a user](154529-bookmarks-delete-all-existing-bookmarks-of-a-user.md) |
| 145409 | Uncontrolled Resource Consumption | n/a | $0 | [help.nextcloud.com: Known DoS condition (null pointer deref) in Nginx running](145409-help-nextcloud-com-known-dos-condition-null-pointer-deref-in.md) |
| 145730 | Improper Authentication - Generic | n/a | $0 | [newsletter.nextcloud.com: Bypass firewall protection](145730-newsletter-nextcloud-com-bypass-firewall-protection.md) |
| 145458 | Memory Corruption - Generic | n/a | $0 | [nextcloud.com: Mail Bombing ( No Rate Limiting On Sending Emails On Contact us Page)](145458-nextcloud-com-mail-bombing-no-rate-limiting-on-sending-email.md) |
| 145375 | Violation of Secure Design Principles | n/a | $0 | [stats.nextcloud.com: Content Injection](145375-stats-nextcloud-com-content-injection.md) |
| 146179 | Command Injection - Generic | n/a | $0 | [REG: Content provider information leakage](146179-reg-content-provider-information-leakage.md) |
| 146093 | Information Disclosure | n/a | $0 | [WordPress Vulnerabilities: User Enumeration, Vulnerable Akismet Plugin, XML-RPC Interface available](146093-wordpress-vulnerabilities-user-enumeration-vulnerable-akisme.md) |
| 145396 | Information Disclosure | n/a | $0 | [Enumeration of subscribed users and unauthenticated email unsubscriptions on https://newsletter.nextcloud.com/?p=unsubscribe](145396-enumeration-of-subscribed-users-and-unauthenticated-email-un.md) |
| 145495 | Information Disclosure | n/a | $0 | [nextcloud.com: Directory listening for 'wp-includes' forders](145495-nextcloud-com-directory-listening-for-wp-includes-forders.md) |
| 3679640 | Uncontrolled Resource Consumption | high | $0 | [Unauthenticated Persistent Denial-of-Service via Federated Share Injection](3679640-unauthenticated-persistent-denial-of-service-via-federated-s.md) |
| 1994328 | Missing Encryption of Sensitive Data | low | $0 | [App stores client secret unencrypted in database](1994328-app-stores-client-secret-unencrypted-in-database.md) |
| 1789602 | Cross-site Scripting (XSS) - Generic | none | $0 | [Contacts only sanitizes PHOTO svg if mime type is all lower case](1789602-contacts-only-sanitizes-photo-svg-if-mime-type-is-all-lower.md) |
| 1476709 | Information Exposure Through Directory Listing | medium | $0 | [Information Exposure Through Directory Listing vulnerability](1476709-information-exposure-through-directory-listing-vulnerability.md) |
| 1167817 | Improper Authentication - Generic | medium | $0 | [Federated shares are not password protected](1167817-federated-shares-are-not-password-protected.md) |
| 1195568 | Ransomware protection is missing extentions | low | $0 | [Ransomware protection is missing extentions](1195568-ransomware-protection-is-missing-extentions.md) |
| 1200992 | No admin audit log for auth tokens | low | $0 | [No admin audit log for auth tokens](1200992-no-admin-audit-log-for-auth-tokens.md) |
| 1183302 | Default Nextcloud allows http federated shares | medium | $0 | [Default Nextcloud allows http federated shares](1183302-default-nextcloud-allows-http-federated-shares.md) |
| 1173411 | Information Disclosure | none | $0 | [Nextcloud update checks leaks information](1173411-nextcloud-update-checks-leaks-information.md) |
| 867164 | Storing Passwords in a Recoverable Format | high | $0 | [External storage app saves password for all users in the database](867164-external-storage-app-saves-password-for-all-users-in-the-dat.md) |
| 882258 | Insecure Direct Object Reference (IDOR) | low | $0 | [New users can read all Nextcloud Deck data from previous user with same username](882258-new-users-can-read-all-nextcloud-deck-data-from-previous-use.md) |
| 747726 | Improper Access Control - Generic | n/a | $0 | [Bypassing Passcode/Device credentials](747726-bypassing-passcode-device-credentials.md) |
| 743505 | Insufficiently Protected Credentials | medium | $0 | [Improper confidentiality protection of server-side encryption keys](743505-improper-confidentiality-protection-of-server-side-encryptio.md) |
| 895730 | Information Disclosure | low | $0 | [Contacts menu (not app) fails to restrict (to local groups) for contacts from federated servers](895730-contacts-menu-not-app-fails-to-restrict-to-local-groups-for.md) |
| 165353 | Violation of Secure Design Principles | medium | $0 | [**minor issue ** -Nextcloud 10.0 session issue with desktop client and android client](165353-minor-issue-nextcloud-10-0-session-issue-with-desktop-client.md) |
| 369979 | Violation of Secure Design Principles | n/a | $0 | [Missing X-Content-Type-Options ](369979-missing-x-content-type-options.md) |
| 476439 | Information Disclosure | low | $0 | [Password authentication at newsletter.nextcloud.com discloses username list](476439-password-authentication-at-newsletter-nextcloud-com-disclose.md) |
| 341074 | Improper Restriction of Authentication Attempts | high | $0 | [Bruteforce in admin panel](341074-bruteforce-in-admin-panel.md) |
| 475114 | Improper Access Control - Generic | n/a | $0 | [Github repo's wiki publicly editable](475114-github-repo-s-wiki-publicly-editable.md) |
| 685491 | Cross-site Scripting (XSS) - Stored | medium | $0 | [Persistent XSS on favorite via filename](685491-persistent-xss-on-favorite-via-filename.md) |
| 498852 | Cross-site Scripting (XSS) - Stored | medium | $0 | [XSS On Nextcloud Integrated with zimbra drive](498852-xss-on-nextcloud-integrated-with-zimbra-drive.md) |
| 669365 | Insecure Storage of Sensitive Information | low | $0 | [Veracode and security audit record are publicly available](669365-veracode-and-security-audit-record-are-publicly-available.md) |
| 561805 | W3 Total Cache plugin multiple vulnerabilities | n/a | $0 | [W3 Total Cache plugin multiple vulnerabilities](561805-w3-total-cache-plugin-multiple-vulnerabilities.md) |
| 462441 | Information Disclosure | medium | $0 | [Retrieval and alteration of exposed media on Android Oreo ](462441-retrieval-and-alteration-of-exposed-media-on-android-oreo.md) |
| 237860 | Uncontrolled Resource Consumption | high | $0 | [ci.nextcloud.com: CVE-2015-5477 BIND9 TKEY Vulnerability + Exploit (Denial of Service)](237860-ci-nextcloud-com-cve-2015-5477-bind9-tkey-vulnerability-expl.md) |
| 222805 | Violation of Secure Design Principles | low | $0 | [Content (Text) Injection at https://nextcloud.com](222805-content-text-injection-at-https-nextcloud-com.md) |
| 145488 | Improper Authentication - Generic | n/a | $0 | [failure to invalidate session on password change](145488-failure-to-invalidate-session-on-password-change.md) |
| 153799 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [xss for admin of https://newsletter.nextcloud.com](153799-xss-for-admin-of-https-newsletter-nextcloud-com.md) |
| 188195 | Violation of Secure Design Principles | medium | $0 | [Login Hints on Admin Panel](188195-login-hints-on-admin-panel.md) |
| 155189 | Violation of Secure Design Principles | n/a | $0 | [demo.nextcloud.com: Content spoofing due to default Apache Error Page](155189-demo-nextcloud-com-content-spoofing-due-to-default-apache-er.md) |
| 151847 | Improper Authentication - Generic | n/a | $0 | [The application uses basic authentication.](151847-the-application-uses-basic-authentication.md) |
| 145462 | Improper Authentication - Generic | n/a | $0 | [No rate limiting on password protected shared file link](145462-no-rate-limiting-on-password-protected-shared-file-link.md) |
| 145402 | Improper Authentication - Generic | n/a | $0 | [No permission set on Activities [Android App]](145402-no-permission-set-on-activities-android-app.md) |
| 145722 | Improper Authentication - Generic | n/a | $0 | [Bruteforce attack is possible on newsletter.nextcloud.com](145722-bruteforce-attack-is-possible-on-newsletter-nextcloud-com.md) |
| 145853 | Violation of Secure Design Principles | n/a | $0 | [Content injection in subdomain](145853-content-injection-in-subdomain.md) |
| 145850 | Violation of Secure Design Principles | n/a | $0 | [Content Spoofing/Text Injection - docs.nextcloud.org](145850-content-spoofing-text-injection-docs-nextcloud-org.md) |
| 145612 | Violation of Secure Design Principles | n/a | $0 | [No captcha on newsletter.nextcloudcom leaves vulnerable to email spammers](145612-no-captcha-on-newsletter-nextcloudcom-leaves-vulnerable-to-e.md) |
| 145374 | Violation of Secure Design Principles | n/a | $0 | [Content Spoofing](145374-content-spoofing.md) |
| 145603 | Information Disclosure | n/a | $0 | [https://newsletter.nextcloud.com Directory listening and Information Disclosure](145603-https-newsletter-nextcloud-com-directory-listening-and-infor.md) |
| 3566607 | Improper Privilege Management | medium | $0 | [No password confirmation required when using apptoken on sensitive endpoint](3566607-no-password-confirmation-required-when-using-apptoken-on-sen.md) |
| 1173670 | Improper Access Control - Generic | low | $0 | [Trusted server shared secret stored unencrypted in the database](1173670-trusted-server-shared-secret-stored-unencrypted-in-the-datab.md) |
| 549831 | Insecure Storage of Sensitive Information | n/a | $0 | [External Storage - WebDAV - New user has access to storage from deleted user (same user-ID)](549831-external-storage-webdav-new-user-has-access-to-storage-from.md) |
| 949712 | Uncontrolled Resource Consumption | low | $0 | [DoS attack against the client when entering a long password](949712-dos-attack-against-the-client-when-entering-a-long-password.md) |
| 473144 | Resource Injection | low | $0 | [Content spoofing on https://surveyserver.nextcloud.com](473144-content-spoofing-on-https-surveyserver-nextcloud-com.md) |
| 732431 | Insufficiently Protected Credentials | high | $0 | [Improper integrity protection of server-side encryption keys](732431-improper-integrity-protection-of-server-side-encryption-keys.md) |
| 885041 | Plaintext Storage of a Password | low | $0 | [The password of a mail share is not hashed if the password is given when the share is created](885041-the-password-of-a-mail-share-is-not-hashed-if-the-password-i.md) |
| 380102 | Memory Corruption - Generic | medium | $0 | [Missing memory corruption protection on Windows release built](380102-missing-memory-corruption-protection-on-windows-release-buil.md) |
| 264426 | Plaintext Storage of a Password | low | $0 | [Nextcloud logs ldap passwords](264426-nextcloud-logs-ldap-passwords.md) |
| 696198 | Information Disclosure | low | $0 | [WordPress Plugin Insert or Embed Articulate Content into WordPress Remote Code Execution (UNAUTHORIZED)](696198-wordpress-plugin-insert-or-embed-articulate-content-into-wor.md) |
| 374053 | Cleartext Transmission of Sensitive Information | n/a | $0 | [Accessing to download.nextcloud.com from original ip adreess \| insecure Download](374053-accessing-to-download-nextcloud-com-from-original-ip-adreess.md) |
| 222838 | Cross-site Scripting (XSS) - Generic | low | $0 | [Stored XSS in Gallery application (NC-SA-2017-010)](222838-stored-xss-in-gallery-application-nc-sa-2017-010.md) |
| 218876 | Information Exposure Through Directory Listing | medium | $0 | [Share tokens for public calendars disclosed (NC-SA-2017-011)](218876-share-tokens-for-public-calendars-disclosed-nc-sa-2017-011.md) |
| 222667 | Server-Side Request Forgery (SSRF) | medium | $0 | [Possible SSRF in email server settings(SMTP mode)](222667-possible-ssrf-in-email-server-settings-smtp-mode.md) |
| 223759 | Information Disclosure | n/a | $0 | [information disclose](223759-information-disclose.md) |
| 222660 | Improper Access Control - Generic | medium | $0 | [The email API to test email-server settings is unlimited and can be used as a email bomb](222660-the-email-api-to-test-email-server-settings-is-unlimited-and.md) |
| 221043 | Cross-Site Request Forgery (CSRF) | medium | $0 | [CSRF token validation is missing](221043-csrf-token-validation-is-missing.md) |
| 215372 | Server version/OS type disclosure via HTTP Response Header | low | $0 | [Server version/OS type disclosure via HTTP Response Header](215372-server-version-os-type-disclosure-via-http-response-header.md) |
| 199445 | Cryptographic Issues - Generic | n/a | $0 | [Nextcloud.com is vulnerable to SWEET32 attack](199445-nextcloud-com-is-vulnerable-to-sweet32-attack.md) |
| 188205 | Improper Authentication - Generic | high | $0 | [BruteForce in to Admin Account](188205-bruteforce-in-to-admin-account.md) |
| 155690 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [Arbitrary File Upload in Logo & Log in image Theming setting.](155690-arbitrary-file-upload-in-logo-log-in-image-theming-setting.md) |
| 164520 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [Reflected Self-XSS Vulnerability in the Comment section of Files (Different-payloads)](164520-reflected-self-xss-vulnerability-in-the-comment-section-of-f.md) |
| 152925 | Violation of Secure Design Principles | n/a | $0 | [Content spoofing in cloud.nextcloud.com](152925-content-spoofing-in-cloud-nextcloud-com.md) |
| 161299 | Violation of Secure Design Principles | n/a | $0 | [Content Injection - apps.nextcloud.com](161299-content-injection-apps-nextcloud-com.md) |
| 145463 | Violation of Secure Design Principles | n/a | $0 | [Nextcloud server software: Content Spoofing](145463-nextcloud-server-software-content-spoofing.md) |
| 146314 | Information Disclosure | n/a | $0 | [Deny access to download.nextcloud.com + folders](146314-deny-access-to-download-nextcloud-com-folders.md) |
| 145854 | Violation of Secure Design Principles | n/a | $0 | [Content Injection in subdomain](145854-content-injection-in-subdomain.md) |
| 145849 | Violation of Secure Design Principles | n/a | $0 | [Content Injection 404 page](145849-content-injection-404-page.md) |
| 145583 | Cross-Site Request Forgery (CSRF) | n/a | $0 | [Lost Password CSRF](145583-lost-password-csrf.md) |
| 145552 | Cryptographic Issues - Generic | n/a | $0 | [Directory Listing On download.nextcloud.com & Practical Attacks on PGP (Pretty Good Privacy) ](145552-directory-listing-on-download-nextcloud-com-practical-attack.md) |
| 145430 | help.nextcloud.com: Session Management Issue | n/a | $0 | [help.nextcloud.com: Session Management Issue](145430-help-nextcloud-com-session-management-issue.md) |
| 1211061 | Insecure Storage of Sensitive Information | medium | $0 | [Leaking sensitive information through JSON  file path.](1211061-leaking-sensitive-information-through-json-file-path.md) |
| 812028 | Cross-site Scripting (XSS) - Generic | low | $0 | [xss on setup config page ](812028-xss-on-setup-config-page.md) |
| 865777 | Business Logic Errors | high | $0 | [Bypass hide download Nextcloud Share](865777-bypass-hide-download-nextcloud-share.md) |
| 961997 | Denial of Service when entring an Array in email at seetings | medium | $0 | [Denial of Service when entring an Array in email at seetings](961997-denial-of-service-when-entring-an-array-in-email-at-seetings.md) |
| 255822 | Uncontrolled Resource Consumption | medium | $0 | [WebDAV Empty Property search leads to full CPU usage](255822-webdav-empty-property-search-leads-to-full-cpu-usage.md) |
| 279717 | Broken link for wrong domain entry may be leveraged for Phishing, Misinformation, Serving Malware | low | $0 | [Broken link for wrong domain entry may be leveraged for Phishing, Misinformation, Serving Malware](279717-broken-link-for-wrong-domain-entry-may-be-leveraged-for-phis.md) |
| 710996 | UI Redressing (Clickjacking) | low | $0 | [Nextcloud Clickjacking Vulnerability](710996-nextcloud-clickjacking-vulnerability.md) |
| 658011 | UI Redressing (Clickjacking) | n/a | $0 | [Clickjacking on https://download.nextcloud.com](658011-clickjacking-on-https-download-nextcloud-com.md) |
| 662155 | UI Redressing (Clickjacking) | none | $0 | [Clickjacking on https://download.nextcloud.com/](662155-clickjacking-on-https-download-nextcloud-com.md) |
| 403909 | Information Exposure Through Directory Listing | low | $0 | [Information Exposure Through Directory Listing - https://apps.nextcloud.com/static/](403909-information-exposure-through-directory-listing-https-apps-ne.md) |
| 218199 | Information Exposure Through Directory Listing | low | $0 | [Directory Listing In Subdomain Of nextcloud.com](218199-directory-listing-in-subdomain-of-nextcloud-com.md) |
| 224108 | Cross Site Scripting | n/a | $0 | [Cross Site Scripting](224108-cross-site-scripting.md) |
| 153251 | Violation of Secure Design Principles | n/a | $0 | [[Nextcloud 9.0.53] Content Spoofing in 'trustDomain' parameter](153251-nextcloud-9-0-53-content-spoofing-in-trustdomain-parameter.md) |
| 177713 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [xss on demo.nextcloud.com due to outdated version](177713-xss-on-demo-nextcloud-com-due-to-outdated-version.md) |
| 163823 | Uncontrolled Resource Consumption | n/a | $0 | [Slow Http attack on nextcloud(DOS)](163823-slow-http-attack-on-nextcloud-dos.md) |
| 156425 | Violation of Secure Design Principles | n/a | $0 | [demo.nextcloud.com: Content spoofing due to default Apache Error Page](156425-demo-nextcloud-com-content-spoofing-due-to-default-apache-er.md) |
| 161323 | Violation of Secure Design Principles | n/a | $0 | [Content Injection - demo.nextcloud.com](161323-content-injection-demo-nextcloud-com.md) |
| 667613 | Information Disclosure | low | $0 | [Username Enumeration](667613-username-enumeration.md) |
| 661768 | UI Redressing (Clickjacking) | none | $0 | [Clickjacking on https://nextcloud.com/](661768-clickjacking-on-https-nextcloud-com.md) |
| 380782 | Privilege Escalation | n/a | $0 | [Ubuntu 12.04 Privilege Escalation](380782-ubuntu-12-04-privilege-escalation.md) |
