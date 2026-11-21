# Mozilla

Disclosed reports: **79**

| ID | Temuan | Severity | Bounty | Writeup |
| --- | --- | --- | ---: | --- |
| 3782701 | Code Injection | critical | $12000 | [Unauthenticated RCE in Taskcluster web-server via GraphQL filter argument (sift $where)](3782701-unauthenticated-rce-in-taskcluster-web-server-via-graphql-fi.md) |
| 2255750 | Code Injection | critical | $8000 | [Remote code execution and exfiltration of secret tokens by poisoning the mozilla/fxa CI build cache](2255750-remote-code-execution-and-exfiltration-of-secret-tokens-by-p.md) |
| 2995025 | Path Traversal | high | $6000 | [Mozilla VPN Clients: RCE via file write and path traversal](2995025-mozilla-vpn-clients-rce-via-file-write-and-path-traversal.md) |
| 4000084 | Improper Authentication - Generic | high | $4000 | [A disabled account's API key still works on BMO's Mojolicious /rest/ routes, including for security-group bugs filed after the disable](4000084-a-disabled-account-s-api-key-still-works-on-bmo-s-mojoliciou.md) |
| 3988961 | Cross-site Scripting (XSS) - Stored | high | $3000 | [Stored XSS on the public Pontoon dashboards: the latest-activity tooltip re-parses a contributor's account address as HTML](3988961-stored-xss-on-the-public-pontoon-dashboards-the-latest-activ.md) |
| 3734676 | Authentication Bypass by Capture-replay | medium | $2000 | [Taskcluster web-server OAuth2 authorization codes are reusable and the exchange handler checks the wrong expiry column](3734676-taskcluster-web-server-oauth2-authorization-codes-are-reusab.md) |
| 2467999 | Information Disclosure | critical | $1000 | [Jira Credential Disclosure within Mozilla Slack](2467999-jira-credential-disclosure-within-mozilla-slack.md) |
| 1984060 | Improper Access Control - Generic | medium | $1000 | [After the upload of an private file, using transformations, the file becomes public without the possibility of changing it.](1984060-after-the-upload-of-an-private-file-using-transformations-th.md) |
| 2197244 | Improper Authentication - Generic | medium | $1000 | [Account deletion using the /v1/account/destroy API endpoint using account password without 2FA verification](2197244-account-deletion-using-the-v1-account-destroy-api-endpoint-u.md) |
| 2109320 | Content Spoofing | medium | $1000 | [Potential Spoofing Risk through Firefox Private Relay Service](2109320-potential-spoofing-risk-through-firefox-private-relay-servic.md) |
| 2137154 | Insecure Storage of Sensitive Information | high | $1000 | [Mozilla Mastodon Staging Instance Admin API Key Disclosure Through Slack](2137154-mozilla-mastodon-staging-instance-admin-api-key-disclosure-t.md) |
| 1880929 | Brute Force | medium | $1000 | [Email  user account in indexacao waybackurl](1880929-email-user-account-in-indexacao-waybackurl.md) |
| 1880896 | Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS) | medium | $1000 | [HTML Injection / Reflected Cross-Site Scripting with CSP on https://accounts.firefox.com/settings](1880896-html-injection-reflected-cross-site-scripting-with-csp-on-ht.md) |
| 3279441 | Improper Input Validation | low | $500 | [Bypass of Restricted Keyword "Mozilla" in Display Name Field via Unicode Homoglyphs on addons.allizom.org](3279441-bypass-of-restricted-keyword-mozilla-in-display-name-field-v.md) |
| 2899858 | Misconfiguration | medium | $500 | [Subdomain takeover on a subdomain under firefox.com](2899858-subdomain-takeover-on-a-subdomain-under-firefox-com.md) |
| 2706358 | Misconfiguration | medium | $500 | [[ addons-preview-cdn.mozilla.net ] A subdomain takeover is available via unregistered domain in Fastly](2706358-addons-preview-cdn-mozilla-net-a-subdomain-takeover-is-avail.md) |
| 2513333 | Cross-Site Request Forgery (CSRF) | low | $500 | [csrftoken not unique to session or specific user and csrfmiddlewaretoken  can be altered](2513333-csrftoken-not-unique-to-session-or-specific-user-and-csrfmid.md) |
| 2221404 | Code Injection | low | $500 | [RCE on worker host due to unsanitized "env" variable name in task definition on community-tc.services.mozilla.com](2221404-rce-on-worker-host-due-to-unsanitized-env-variable-name-in-t.md) |
| 1913263 | Cross-Site Scripting (XSS) | low | $500 | [HTML Injection at https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net/user/unsubscribe](1913263-html-injection-at-https-stage-firefoxmonitor-nonprod-cloudop.md) |
| 2256548 | Exposure of Sensitive Information Due to Incompatible Policies | low | $250 | [Exposure of account recovery hint by querying by user email](2256548-exposure-of-account-recovery-hint-by-querying-by-user-email.md) |
| 3243860 | Cleartext Storage of Sensitive Information | medium | $200 | [Microsoft `x-apikey` Exposed in Mozilla CI Public Logs](3243860-microsoft-x-apikey-exposed-in-mozilla-ci-public-logs.md) |
| 2147132 | CRLF Injection | low | $200 | [Security bug https://bugzilla.mozilla.org/oauth/authorize - CRLF Header injection via "redirect_uri" parameter](2147132-security-bug-https-bugzilla-mozilla-org-oauth-authorize-crlf.md) |
| 3154983 | Insecure Direct Object Reference (IDOR) | high | $0 | [IDOR: Account Deletion via Session Misbinding – Attacker Can Delete Victim Account](3154983-idor-account-deletion-via-session-misbinding-attacker-can-de.md) |
| 2915647 | Information Disclosure | critical | $0 | [Netlify Authentication Token Exposed in Public Mozilla CI Logs](2915647-netlify-authentication-token-exposed-in-public-mozilla-ci-lo.md) |
| 1987011 | Improper Access Control - Generic | medium | $0 | [[Hubs] - Broken access control in placing objects in hubs room](1987011-hubs-broken-access-control-in-placing-objects-in-hubs-room.md) |
| 3175695 | Improper Input Validation | low | $0 | [Bypass "No Links" Restriction in Biography via Protocol-Relative URL (//)](3175695-bypass-no-links-restriction-in-biography-via-protocol-relati.md) |
| 2387297 | Information Disclosure | medium | $0 | [Bypass Email Verification on Add Email Monitoring](2387297-bypass-email-verification-on-add-email-monitoring.md) |
| 2209130 | SQL Injection | critical | $0 | [SQL Injection on prod.oidc-proxy.prod.webservices.mozgcp.net via invite_code parameter - Mozilla social inscription](2209130-sql-injection-on-prod-oidc-proxy-prod-webservices-mozgcp-net.md) |
| 2712583 | Business Logic Errors | medium | $0 | [ Bypass Email verification for monitoring at `monitor.mozilla.org`](2712583-bypass-email-verification-for-monitoring-at-monitor-mozilla.md) |
| 2382484 | Insecure Direct Object Reference (IDOR) | high | $0 | [IDOR on Delete Email address features](2382484-idor-on-delete-email-address-features.md) |
| 1888545 | Insecure Direct Object Reference (IDOR) | medium | $0 | [IDOR - send a message on behalf of other user ](1888545-idor-send-a-message-on-behalf-of-other-user.md) |
| 2269867 | Misconfiguration | medium | $0 | [Subdomain takeover on one of the subdomain under mozaws.net](2269867-subdomain-takeover-on-one-of-the-subdomain-under-mozaws-net.md) |
| 2401648 | Information Disclosure | critical | $0 | [two aws access key and secret key and database username and password exposed ](2401648-two-aws-access-key-and-secret-key-and-database-username-and.md) |
| 1987687 | Cleartext Transmission of Sensitive Information | low | $0 | [Leakage of traffic in plaintext towards the IP address of VPN server](1987687-leakage-of-traffic-in-plaintext-towards-the-ip-address-of-vp.md) |
| 2686750 | Improper Link Resolution Before File Access ('Link Following') | medium | $0 | [MozillaVPN: Elevation of Privilege via a Logic Vulnerability](2686750-mozillavpn-elevation-of-privilege-via-a-logic-vulnerability.md) |
| 3025797 | Privilege Escalation | low | $0 | [[Privilege Escalation] User can Pin\|Unpin Any Comment on Any Project or Locale](3025797-privilege-escalation-user-can-pin-unpin-any-comment-on-any-p.md) |
| 2383486 | Improper Access Control - Generic | low | $0 | [Insecure S3 Bucket Exposing Git Directory in Mozilla Foundation Infographics Project](2383486-insecure-s3-bucket-exposing-git-directory-in-mozilla-foundat.md) |
| 1976449 | Cache Poisoning | low | $0 | [DOS via cache poisoning on [developer.mozilla.org]](1976449-dos-via-cache-poisoning-on-developer-mozilla-org.md) |
| 2015554 | Server-Side Request Forgery (SSRF) | none | $0 | [Internal Blind Server-Side Request Forgery (SSRF) allows scanning internal ports](2015554-internal-blind-server-side-request-forgery-ssrf-allows-scann.md) |
| 2696294 | Private Emails of Moz Workers Leaked in Public file | none | $0 | [Private Emails of Moz Workers Leaked in Public file](2696294-private-emails-of-moz-workers-leaked-in-public-file.md) |
| 2545012 | Misconfiguration | medium | $0 | [Subdomain takeover on one of the subdomains under mozaws.net](2545012-subdomain-takeover-on-one-of-the-subdomains-under-mozaws-net.md) |
| 2412983 | Information Disclosure | none | $0 | [sentry Auth Token exposed publicly in docker hub image ](2412983-sentry-auth-token-exposed-publicly-in-docker-hub-image.md) |
| 1913309 | Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition') | low | $0 | [Race condition leads to add more than 5 email at Data breaches monitor system at https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net](1913309-race-condition-leads-to-add-more-than-5-email-at-data-breach.md) |
| 1987680 | Cleartext Transmission of Sensitive Information | medium | $0 | [Leaking VPN traffic through non-RFC1918 local IP addresses](1987680-leaking-vpn-traffic-through-non-rfc1918-local-ip-addresses.md) |
| 2131215 | Misconfiguration | medium | $0 | [Subdomain takeover on one of the subdomain under mozaws.net](2131215-subdomain-takeover-on-one-of-the-subdomain-under-mozaws-net.md) |
| 2030076 | Cleartext Storage of Sensitive Information | critical | $0 | [Mozilla FuzzManager API Token Exposed in Git Commit](2030076-mozilla-fuzzmanager-api-token-exposed-in-git-commit.md) |
| 2735646 | Information Disclosure | high | $0 | [User API Key leakage in Github commit leads to unauthorized access to sql.telemetry.mozilla.org](2735646-user-api-key-leakage-in-github-commit-leads-to-unauthorized.md) |
| 3020021 | Privilege Escalation | medium | $0 | [[Vertical Privilege Escalation] User can Unapproved any Approved Translation at [/translations/unapprove/]](3020021-vertical-privilege-escalation-user-can-unapproved-any-approv.md) |
| 2737309 | Information Disclosure | low | $0 | [Information disclosure on password cancel endpoint ](2737309-information-disclosure-on-password-cancel-endpoint.md) |
| 2286867 | Misconfiguration | medium | $0 | [Subdomain takeover on one of the subdomain under mozaws.net](2286867-subdomain-takeover-on-one-of-the-subdomain-under-mozaws-net.md) |
| 2380084 | Information Disclosure | none | $0 | [paypal client_id And stripe api key indexed on web archive](2380084-paypal-client-id-and-stripe-api-key-indexed-on-web-archive.md) |
| 2193815 | Cleartext Storage of Sensitive Information | critical | $0 | [Mozilla Employee's Token for sql.telemetry.mozilla.org Exposed in Git Commit](2193815-mozilla-employee-s-token-for-sql-telemetry-mozilla-org-expos.md) |
| 2261577 | Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition') | medium | $0 | [MozillaVPN: Elevation of Privilege via a Race Condition Vulnerability](2261577-mozillavpn-elevation-of-privilege-via-a-race-condition-vulne.md) |
| 2209571 | Misconfiguration | medium | $0 | [Subdomain takeover on one of the subdomain under mozaws.net](2209571-subdomain-takeover-on-one-of-the-subdomain-under-mozaws-net.md) |
| 2287098 | Misconfiguration | medium | $0 | [Subdomain takeover on one of the subdomain under mozaws.net](2287098-subdomain-takeover-on-one-of-the-subdomain-under-mozaws-net.md) |
| 2106662 | Cross-Site Request Forgery (CSRF) | low | $0 | [CSRF to Information disclosure on password reset](2106662-csrf-to-information-disclosure-on-password-reset.md) |
| 2140976 | Misconfiguration | medium | $0 | [Subdomain takeover on one of the subdomain under mozgcp.net](2140976-subdomain-takeover-on-one-of-the-subdomain-under-mozgcp-net.md) |
| 3325582 | Improper Access Control - Generic | low | $0 | [User Can Delete Other Users' Personal Access Tokens at /delete-token/{token_id}/ on Mozilla Pontoon](3325582-user-can-delete-other-users-personal-access-tokens-at-delete.md) |
| 2285286 | Misconfiguration | medium | $0 | [Subdomain takeover on one of the subdomain under mozaws.net](2285286-subdomain-takeover-on-one-of-the-subdomain-under-mozaws-net.md) |
| 2398630 | Misconfiguration | medium | $0 | [Subdomain takeover on one of the subdomains under mozaws.net](2398630-subdomain-takeover-on-one-of-the-subdomains-under-mozaws-net.md) |
| 2017323 | Misconfiguration | medium | $0 | [Subdomain takeover on one of the subdomain under mozilla.org](2017323-subdomain-takeover-on-one-of-the-subdomain-under-mozilla-org.md) |
| 2053396 | Information Disclosure | low | $0 | [Possibility of Deface through translation tool - www.mozilla.com](2053396-possibility-of-deface-through-translation-tool-www-mozilla-c.md) |
| 2143408 | Misconfiguration | medium | $0 | [Subdomain takeover on one of the subdomain under mozgcp.net](2143408-subdomain-takeover-on-one-of-the-subdomain-under-mozgcp-net.md) |
| 2037032 | Improper Resource Shutdown or Release | medium | $0 | [Subdomain takeover on one of the subdomain under mozaws.net](2037032-subdomain-takeover-on-one-of-the-subdomain-under-mozaws-net.md) |
| 2860983 | Cache Poisoning | low | $0 | [Denial of Access to Static Resources via Cache Poisoning on addons.allizom.org](2860983-denial-of-access-to-static-resources-via-cache-poisoning-on.md) |
| 1992261 | Information Disclosure | low | $0 | [Flickr API key leaked in GitHub commit](1992261-flickr-api-key-leaked-in-github-commit.md) |
| 2111291 | Cross-site Scripting (XSS) - Stored | low | $0 | [Stored Xss on bugzilla.mozilla.org via comment edit feature from non-admin to admin.](2111291-stored-xss-on-bugzilla-mozilla-org-via-comment-edit-feature.md) |
| 1989901 | Information Disclosure | low | $0 | [If rate limit is hit, IP address is leaked to anyone who tries to login](1989901-if-rate-limit-is-hit-ip-address-is-leaked-to-anyone-who-trie.md) |
| 2190380 | Misconfiguration | medium | $0 | [Subdomain takeover on one of the subdomain under mozgcp.net](2190380-subdomain-takeover-on-one-of-the-subdomain-under-mozgcp-net.md) |
| 2078707 | Improper Access Control - Generic | low | $0 | [Exposing Django Debug Panel and Sensitive Infrastructure Information at https://dev.fxprivaterelay.nonprod.cloudops.mozgcp.net](2078707-exposing-django-debug-panel-and-sensitive-infrastructure-inf.md) |
| 2135054 | Misconfiguration | medium | $0 | [Subdomain takeover on one of the subdomain under mozaws.net](2135054-subdomain-takeover-on-one-of-the-subdomain-under-mozaws-net.md) |
| 2194289 | Misconfiguration | medium | $0 | [Subdomain takeover on one of the subdomain under mozaws.net](2194289-subdomain-takeover-on-one-of-the-subdomain-under-mozaws-net.md) |
| 2171494 | Misconfiguration | medium | $0 | [Subdomain takeover on one of the subdomain under mozaws.net](2171494-subdomain-takeover-on-one-of-the-subdomain-under-mozaws-net.md) |
| 1995595 | Improper Access Control - Generic | n/a | $0 | [Response Manipulation to enable Account recovery key with out current password](1995595-response-manipulation-to-enable-account-recovery-key-with-ou.md) |
| 2123680 | Misconfiguration | medium | $0 | [Subdomain takeover on one of the subdomain under mozgcp.net](2123680-subdomain-takeover-on-one-of-the-subdomain-under-mozgcp-net.md) |
| 1879548 | Uncontrolled Resource Consumption | medium | $0 | [Missing Function Level Access Control in Mozilla formula containsRegular Expression Denial of Service (CVE-2023-25166)](1879548-missing-function-level-access-control-in-mozilla-formula-con.md) |
| 2129791 | Misconfiguration | medium | $0 | [Subdomain takeover on one of the subdomain under mozaws.net](2129791-subdomain-takeover-on-one-of-the-subdomain-under-mozaws-net.md) |
| 2127469 | Misconfiguration | medium | $0 | [Subdomain takeover on one of the subdomain under mozaws.net](2127469-subdomain-takeover-on-one-of-the-subdomain-under-mozaws-net.md) |
| 2134671 | Misconfiguration | medium | $0 | [Subdomain takeover on one of the subdomain under mozaws.net](2134671-subdomain-takeover-on-one-of-the-subdomain-under-mozaws-net.md) |
