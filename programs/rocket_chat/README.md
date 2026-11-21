# Rocket.Chat

Disclosed reports: **98**

| ID | Temuan | Severity | Bounty | Writeup |
| --- | --- | --- | ---: | --- |
| 3564655 | SQL Injection | critical | $0 | [Complete authentication bypass to admin permissions](3564655-complete-authentication-bypass-to-admin-permissions.md) |
| 3779690 | Cross-site Scripting (XSS) - Stored | medium | $0 | [Stored XSS in Rocket.Chat HTML File Export — Unauthenticated Entry via LiveChat](3779690-stored-xss-in-rocket-chat-html-file-export-unauthenticated-e.md) |
| 2028450 | Insecure Direct Object Reference (IDOR) | low | $0 | [IDOR vulnerability leads to Deleting message after leaving/getting banned from group using message ID](2028450-idor-vulnerability-leads-to-deleting-message-after-leaving-g.md) |
| 3734326 | Insecure Direct Object Reference (IDOR) | high | $0 | [Autotranslate DDP Method Exposes Private Messages Without Authentication or Room Access Check](3734326-autotranslate-ddp-method-exposes-private-messages-without-au.md) |
| 219957 | Cross-site Scripting (XSS) - Stored | critical | $0 | [XSS via /api/v1/chat.postMessage ](219957-xss-via-api-v1-chat-postmessage.md) |
| 842625 | Insecure Direct Object Reference (IDOR) | critical | $0 | [account takeover on 3.0.1 version](842625-account-takeover-on-3-0-1-version.md) |
| 433792 | SQL Injection | n/a | $0 | [Blind SQL injection in third-party software, that allows to reveal user statistic from rocket.chat and possibly hack into the rocketchat.agilecrm.com](433792-blind-sql-injection-in-third-party-software-that-allows-to-r.md) |
| 501081 | Improper Access Control - Generic | critical | $0 | [Guest Privilege Escalation to admin group](501081-guest-privilege-escalation-to-admin-group.md) |
| 1886954 | Server-Side Request Forgery (SSRF) | high | $0 | [Unauthenticated full-read SSRF via Twilio integration](1886954-unauthenticated-full-read-ssrf-via-twilio-integration.md) |
| 3687142 | Improper Access Control - Generic | critical | $0 | [Unauthenticated reading of every file via livechat auth and predicting MongoDB ObjectId()](3687142-unauthenticated-reading-of-every-file-via-livechat-auth-and.md) |
| 3514640 | Path Traversal | high | $0 | [Unauthenticated Path Traversal (LFI) via /custom-sounds/ when CustomSounds uses FileSystem storage](3514640-unauthenticated-path-traversal-lfi-via-custom-sounds-when-cu.md) |
| 501084 | Improper Access Control - Generic | medium | $0 | [Upload of Avatars for other Users](501084-upload-of-avatars-for-other-users.md) |
| 3713682 | Insecure Direct Object Reference (IDOR) | medium | $0 | [IDOR: autotranslate.translateMessage Full Message Content Leak](3713682-idor-autotranslate-translatemessage-full-message-content-lea.md) |
| 735638 | Cross-site Scripting (XSS) - Stored | critical | $0 | [Account takeover via XSS](735638-account-takeover-via-xss.md) |
| 3589551 | Improper Access Control - Generic | medium | $0 | [RBAC bypass on App log endpoints via `permissionRequired` typo — any authenticated user reads admin-only Enterprise App logs](3589551-rbac-bypass-on-app-log-endpoints-via-permissionrequired-typo.md) |
| 943725 | Remote Code Execution in Rocket.Chat-Desktop | critical | $0 | [Remote Code Execution in Rocket.Chat-Desktop](943725-remote-code-execution-in-rocket-chat-desktop.md) |
| 3827674 | Improper Authentication - Generic | critical | $0 | [Authentication Bypass via XML Signature Wrapping in SAML SSO](3827674-authentication-bypass-via-xml-signature-wrapping-in-saml-sso.md) |
| 399166 | Code Injection | medium | $0 | [Remote code execution by hijacking an unclaimed S3 bucket in Rocket.Chat's installation script.](399166-remote-code-execution-by-hijacking-an-unclaimed-s3-bucket-in.md) |
| 3611837 | Improper Authentication - Generic | high | $0 | [Unauthenticated file deletion via deleteFileMessage DDP method allows permanent destruction of any uploaded file](3611837-unauthenticated-file-deletion-via-deletefilemessage-ddp-meth.md) |
| 501077 | Improper Access Control - Generic | medium | $0 | [Online Status of arbitrary users can be changed](501077-online-status-of-arbitrary-users-can-be-changed.md) |
| 3418031 | Open Redirect | medium | $0 | [Open Redirect in Rocket.Chat](3418031-open-redirect-in-rocket-chat.md) |
| 1447619 | Improper Authentication - Generic | critical | $0 | [Authentication Bypass in login-token Authentication Method](1447619-authentication-bypass-in-login-token-authentication-method.md) |
| 899964 | OS Command Injection | critical | $0 | [XSS leads to RCE on the RocketChat desktop client.](899964-xss-leads-to-rce-on-the-rocketchat-desktop-client.md) |
| 1071102 | Improper Authentication - Generic | high | $0 | [Registration bypass with leaked Invite Token](1071102-registration-bypass-with-leaked-invite-token.md) |
| 2580062 | Information Disclosure | medium | $0 | [NoSQL injection leaks visitor token and livechat messages](2580062-nosql-injection-leaks-visitor-token-and-livechat-messages.md) |
| 3473145 | Server-Side Request Forgery (SSRF) | high | $0 | [Unauthenticated SSRF in Voxtelesys integration ('checkUrlForSsrf' Bypass via DNS rebinding)](3473145-unauthenticated-ssrf-in-voxtelesys-integration-checkurlforss.md) |
| 3393664 | Server-Side Request Forgery (SSRF) | high | $0 | [SSRF via improper validation after DNS name resolution in the link-preview feature](3393664-ssrf-via-improper-validation-after-dns-name-resolution-in-th.md) |
| 833470 | Code Injection | medium | $0 | [[Security Vulnerability Rocket.chat] HTML Injection into Email via Signup](833470-security-vulnerability-rocket-chat-html-injection-into-email.md) |
| 3383079 | Server-Side Request Forgery (SSRF) | medium | $0 | [SSRF via Improper Redirect Validation in Rocket.Chat oEmbed Function](3383079-ssrf-via-improper-redirect-validation-in-rocket-chat-oembed.md) |
| 1701378 | Improper Authentication - Generic | low | $0 | [Bypassing 2FA with conventional session management - open.rocket.chat](1701378-bypassing-2fa-with-conventional-session-management-open-rock.md) |
| 1014459 | Cross-site Scripting (XSS) - DOM | high | $0 | [Stored XSS in any message (leads to priv esc for all users and file leak + rce via electron app)](1014459-stored-xss-in-any-message-leads-to-priv-esc-for-all-users-an.md) |
| 2546437 | Use of Insufficiently Random Values | high | $0 | [The initial E2EE password generated by Rocket.Chat mobile can be recovered in a practical timescale.](2546437-the-initial-e2ee-password-generated-by-rocket-chat-mobile-ca.md) |
| 1631258 | Command Injection - Generic | critical | $0 | [Rocket.Chat Server RCE](1631258-rocket-chat-server-rce.md) |
| 728004 | UI Redressing (Clickjacking) | low | $0 | [Clickjacking in the admin page](728004-clickjacking-in-the-admin-page.md) |
| 1130721 | Pre-Auth Blind NoSQL Injection leading to Remote Code Execution | critical | $0 | [Pre-Auth Blind NoSQL Injection leading to Remote Code Execution](1130721-pre-auth-blind-nosql-injection-leading-to-remote-code-execut.md) |
| 1031613 | Code Injection | medium | $0 | [CSS Injection in Message Avatar](1031613-css-injection-in-message-avatar.md) |
| 1757663 | Improper Access Control - Generic | high | $0 | [Low authorization level at server side API operation e2e.updateGroupKey, let an attacker break the E2E architecture.](1757663-low-authorization-level-at-server-side-api-operation-e2e-upd.md) |
| 382666 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [Blind XSS in the rocket.chat registration email](382666-blind-xss-in-the-rocket-chat-registration-email.md) |
| 1063114 | Information Disclosure | medium | $0 | [Unread Messages can leak Message IDs](1063114-unread-messages-can-leak-message-ids.md) |
| 843171 | Code Injection | high | $0 | [Desktop app RCE (#276031 bypass)](843171-desktop-app-rce-276031-bypass.md) |
| 3852135 | NoSQL Injection | high | $0 | [DDP methods getThreadsList / getThreadMessages leaks private thread content to any authenticated low privilege user (unpatched sibling of #1446767)](3852135-ddp-methods-getthreadslist-getthreadmessages-leaks-private-t.md) |
| 1584034 | UI Redressing (Clickjacking) | medium | $0 | [Clickjacking at open.rocket.chat](1584034-clickjacking-at-open-rocket-chat.md) |
| 899954 | Cross-site Scripting (XSS) - Stored | critical | $0 | [XSS in message attachment fileds.](899954-xss-in-message-attachment-fileds.md) |
| 3872858 | Cross-site Scripting (XSS) - DOM | low | $0 | [Stored HTML Injection (CWE-79) via Livechat Visitor Name](3872858-stored-html-injection-cwe-79-via-livechat-visitor-name.md) |
| 812064 | Improper Authentication - Generic | high | $0 | [SAML authentication bypass](812064-saml-authentication-bypass.md) |
| 1380157 | Content-Security Policy bypass with File Uploads | high | $0 | [Content-Security Policy bypass with File Uploads](1380157-content-security-policy-bypass-with-file-uploads.md) |
| 943737 | Arbitrary file read in Rocket.Chat-Desktop | medium | $0 | [Arbitrary file read in Rocket.Chat-Desktop](943737-arbitrary-file-read-in-rocket-chat-desktop.md) |
| 386614 | Cleartext Storage of Sensitive Information | none | $0 | [Slack Token exposed over internet (Github)](386614-slack-token-exposed-over-internet-github.md) |
| 1063164 | Improper Access Control - Generic | medium | $0 | [Unauthenticated clients can modify Livechat Business Hours](1063164-unauthenticated-clients-can-modify-livechat-business-hours.md) |
| 924151 | OS Command Injection | critical | $0 | [Insecure use of shell.openExternal() in Rocket.Chat Desktop App leading to RCE](924151-insecure-use-of-shell-openexternal-in-rocket-chat-desktop-ap.md) |
| 1130874 | Post-Auth Blind NoSQL Injection in the users.list API leads to Remote Code Execution | high | $0 | [Post-Auth Blind NoSQL Injection in the users.list API leads to Remote Code Execution](1130874-post-auth-blind-nosql-injection-in-the-users-list-api-leads.md) |
| 766346 | Use of Hard-coded Credentials | medium | $0 | [API Keys Hardcoded in Github repository](766346-api-keys-hardcoded-in-github-repository.md) |
| 276031 | Code Injection | high | $0 | [Remote Code Execution in Rocket.Chat Desktop](276031-remote-code-execution-in-rocket-chat-desktop.md) |
| 1379400 | Cross-site Scripting (XSS) - Stored | high | $0 | [XSS in various MessageTypes](1379400-xss-in-various-messagetypes.md) |
| 1091118 | Cross-site Scripting (XSS) - Generic | low | $0 | [Blind XSS](1091118-blind-xss.md) |
| 1089116 | Information Disclosure | low | $0 | [Hi! Security Team Rocket.Chat, It's possible to get information about the users emails without authentication](1089116-hi-security-team-rocket-chat-it-s-possible-to-get-informatio.md) |
| 1060837 | Improper Access Control - Generic | medium | $0 | [Improper ACL in Message Starring](1060837-improper-acl-in-message-starring.md) |
| 1967109 | Cleartext Transmission of Sensitive Information | low | $0 | [Rocket.Chat Desktop client fails to open browser on 3rd party external actions from PDF documents](1967109-rocket-chat-desktop-client-fails-to-open-browser-on-3rd-part.md) |
| 1757676 | SQL Injection | high | $0 | [NoSQL injection in listEmojiCustom method call](1757676-nosql-injection-in-listemojicustom-method-call.md) |
| 962902 | Cross-site Scripting (XSS) - DOM | medium | $0 | [Session Hijack via Self-XSS](962902-session-hijack-via-self-xss.md) |
| 724153 | Cross-site Scripting (XSS) - Stored | low | $0 | [XSS (leads to arbitrary file read in Rocket.Chat-Desktop)](724153-xss-leads-to-arbitrary-file-read-in-rocket-chat-desktop.md) |
| 368927 | Open Redirect | medium | $0 | [Open redirect open.rocket.chat/file-upload/ID/filename.svg](368927-open-redirect-open-rocket-chat-file-upload-id-filename-svg.md) |
| 1406479 | Information Disclosure | high | $0 | [Moving private messages into vision with updateMessage method](1406479-moving-private-messages-into-vision-with-updatemessage-metho.md) |
| 1581059 | SQL Injection | critical | $0 | [Regex account takeover](1581059-regex-account-takeover.md) |
| 1390782 | Phishing | low | $0 | [Possible Domain Takeover on AWS Instance.](1390782-possible-domain-takeover-on-aws-instance.md) |
| 491892 | Improper Access Control - Generic | critical | $0 | [Broken access control on apps ](491892-broken-access-control-on-apps.md) |
| 1062538 | Information Disclosure | high | $0 | [Pinning leaks message content](1062538-pinning-leaks-message-content.md) |
| 1049367 | Path Traversal | critical | $0 | [Server-side RCE through directory traversal-based arbitrary file write](1049367-server-side-rce-through-directory-traversal-based-arbitrary.md) |
| 1448268 | Improper Authentication - Generic | high | $0 | [TOTP 2 Factor Authentication Bypass](1448268-totp-2-factor-authentication-bypass.md) |
| 1379645 | Impersonation in Sequential Messages | medium | $0 | [Impersonation in Sequential Messages](1379645-impersonation-in-sequential-messages.md) |
| 1844777 | Cross-site Scripting (XSS) - Reflected | high | $0 | [Reflected Cross-Site Scripting(CVE-2022-32770 )](1844777-reflected-cross-site-scripting-cve-2022-32770.md) |
| 384517 | Cross-site Scripting (XSS) - Stored | medium | $0 | [XSS (stored) Wizard is saving executable code](384517-xss-stored-wizard-is-saving-executable-code.md) |
| 1445810 | Information Disclosure | medium | $0 | [Mute User can disclose private channel members to unauthorized users](1445810-mute-user-can-disclose-private-channel-members-to-unauthoriz.md) |
| 992280 | Improper Access Control - Generic | low | $0 | [Improper Access Control - Generic](992280-improper-access-control-generic.md) |
| 1126414 | Improper Authentication - Generic | medium | $0 | [Bypass local authentication (PIN code)](1126414-bypass-local-authentication-pin-code.md) |
| 1031525 | UI Redressing (Clickjacking) | medium | $0 | [User Impersonation through sendMessage options](1031525-user-impersonation-through-sendmessage-options.md) |
| 1781131 | Cross-site Scripting (XSS) - Stored | medium | $0 | [Cross-Site-Scripting in "Search Messages"](1781131-cross-site-scripting-in-search-messages.md) |
| 1379451 | Messages can be hidden regardless of server configuration | medium | $0 | [Messages can be hidden regardless of server configuration](1379451-messages-can-be-hidden-regardless-of-server-configuration.md) |
| 534887 | Code Injection | critical | $0 | [Custom crafted message object in Meteor.Call allows remote code execution and impersonation](534887-custom-crafted-message-object-in-meteor-call-allows-remote-c.md) |
| 1132202 | Cross-site Scripting (XSS) - Stored | high | $0 | [Post-Auth Stored XSS with User Interaction leads to Remote Code Execution](1132202-post-auth-stored-xss-with-user-interaction-leads-to-remote-c.md) |
| 1049375 | Improper Access Control - Generic | critical | $0 | [SAML authentication bypass through unauthenticated `addSamlProvider` Meteor Call](1049375-saml-authentication-bypass-through-unauthenticated-addsamlpr.md) |
| 1781102 | OS Command Injection | high | $0 | [Insecure use of shell.openExternal() leads to RCE in Rocket.Chat-Desktop](1781102-insecure-use-of-shell-openexternal-leads-to-rce-in-rocket-ch.md) |
| 1446767 | Information Disclosure | high | $0 | [API route chat.getThreadsList leaks private message content](1446767-api-route-chat-getthreadslist-leaks-private-message-content.md) |
| 1401268 | Cross-site Scripting (XSS) - Stored | high | $0 | [Persistent CSS injection with ’marked’ markdown parser in Rocket.Chat](1401268-persistent-css-injection-with-marked-markdown-parser-in-rock.md) |
| 4059370 | Improper Access Control - Generic | medium | $0 | [Mass assignment in chat.sendMessage allows unprivileged users to forge message state: persistent room DoS, stored HTML injection, and cross-user write](4059370-mass-assignment-in-chat-sendmessage-allows-unprivileged-user.md) |
| 1461340 | Uncontrolled Resource Consumption | medium | $0 | [Maliciously crafted message can cause Rocket.Chat server to stop responding](1461340-maliciously-crafted-message-can-cause-rocket-chat-server-to.md) |
| 1379635 | Retrospective change of message timestamp and order | medium | $0 | [Retrospective change of message timestamp and order](1379635-retrospective-change-of-message-timestamp-and-order.md) |
| 1458020 | Information Disclosure | medium | $0 | [NoSQL-Injection discloses S3 File Upload URLs](1458020-nosql-injection-discloses-s3-file-upload-urls.md) |
| 1140631 | Information Disclosure | medium | $0 | [REST API gets `query` as parameter and executes it](1140631-rest-api-gets-query-as-parameter-and-executes-it.md) |
| 1410246 | Information Disclosure | high | $0 | [getUserMentionsByChannel leaks messages with mention from private channel](1410246-getusermentionsbychannel-leaks-messages-with-mention-from-pr.md) |
| 917946 | Privilege Escalation | medium | $0 | [It is possible to elevate privileges for any authenticated user to view permissions matrix and view Direct messages without appropriate permissions.](917946-it-is-possible-to-elevate-privileges-for-any-authenticated-u.md) |
| 832217 | Classic Buffer Overflow | high | $0 | [Android App Crashes while sending message to users/ on channel ](832217-android-app-crashes-while-sending-message-to-users-on-channe.md) |
| 1410357 | getUsersOfRoom discloses users in private channels | medium | $0 | [getUsersOfRoom discloses users in private channels](1410357-getusersofroom-discloses-users-in-private-channels.md) |
| 1517377 | Cleartext Transmission of Sensitive Information | medium | $0 | [Rocket.chat user info security issue](1517377-rocket-chat-user-info-security-issue.md) |
| 1447440 | Information Disclosure | medium | $0 | [getRoomRoles Method leaks Channel Owner](1447440-getroomroles-method-leaks-channel-owner.md) |
| 1406953 | Information Disclosure | medium | $0 | [Message ID Enumeration with Action Link Handler](1406953-message-id-enumeration-with-action-link-handler.md) |
| 1377105 | Information Disclosure | medium | $0 | [Message ID Enumeration with Regular Expression in getReadReceipts Meteor method](1377105-message-id-enumeration-with-regular-expression-in-getreadrec.md) |
| 1394399 | Cleartext Storage of Sensitive Information | medium | $0 | [Unintended information disclosure in the Hubot Log files](1394399-unintended-information-disclosure-in-the-hubot-log-files.md) |
