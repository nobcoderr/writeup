# New Relic

Disclosed reports: **209**

| ID | Temuan | Severity | Bounty | Writeup |
| --- | --- | --- | ---: | --- |
| 498052 | HTTP Request Smuggling | n/a | $3000 | [Password theft login.newrelic.com via Request Smuggling](498052-password-theft-login-newrelic-com-via-request-smuggling.md) |
| 348076 | Cross-site Scripting (XSS) - Stored | n/a | $3000 | [Stored XSS in Brower `name` field reflected in two pages](348076-stored-xss-in-brower-name-field-reflected-in-two-pages.md) |
| 520630 | Cross-site Scripting (XSS) - Stored | n/a | $2500 | [(Prerelease UI) Stored XSS via role name in JSON chart](520630-prerelease-ui-stored-xss-via-role-name-in-json-chart.md) |
| 397137 | Insecure Direct Object Reference (IDOR) | n/a | $2500 | [[NR Insights] Pull any Insights/NRQL data from any NR account](397137-nr-insights-pull-any-insights-nrql-data-from-any-nr-account.md) |
| 459443 | Insecure Direct Object Reference (IDOR) | n/a | $2500 | [[NR Insights] IDOR - Modify the filter settings for any NR Insights dashboard through internal_api endpoint](459443-nr-insights-idor-modify-the-filter-settings-for-any-nr-insig.md) |
| 626082 | Cross-site Scripting (XSS) - Stored | n/a | $2500 | [Stored XSS via "my recent queries" selector in NRQL dashboard builder](626082-stored-xss-via-my-recent-queries-selector-in-nrql-dashboard.md) |
| 634692 | Cross-site Scripting (XSS) - Stored | n/a | $2500 | [Stored XSS Via NRQL chartbuilder JSON view ](634692-stored-xss-via-nrql-chartbuilder-json-view.md) |
| 1067321 | Cross-site Scripting (XSS) - Stored | n/a | $2123 | [Stored XSS via malicious key value of Synthetics monitor tag when visiting an Insights dashboard with filtering enabled](1067321-stored-xss-via-malicious-key-value-of-synthetics-monitor-tag.md) |
| 1089467 | Improper Authentication - Generic | n/a | $2048 | [Account Takeover via Email ID Change and Forgot Password Functionality](1089467-account-takeover-via-email-id-change-and-forgot-password-fun.md) |
| 462321 | Insecure Direct Object Reference (IDOR) | n/a | $2000 | [Ability to view monitor names of other NR accounts through internal API (v3) via "monitor_id" parameter ](462321-ability-to-view-monitor-names-of-other-nr-accounts-through-i.md) |
| 349291 | Insecure Direct Object Reference (IDOR) | n/a | $1500 | [IDOR via internal_api "users" endpoint ](349291-idor-via-internal-api-users-endpoint.md) |
| 332381 | Insecure Direct Object Reference (IDOR) | n/a | $1500 | [Internal API endpoint discloses full account name of email address associated with unconfirmed user](332381-internal-api-endpoint-discloses-full-account-name-of-email-a.md) |
| 320173 | Insecure Direct Object Reference (IDOR) | n/a | $1500 | [Bypass of my three other reports #267636 + #255894 + #271861 - (IDOR) Ability to see full name associated with other New Relic accounts](320173-bypass-of-my-three-other-reports-267636-255894-271861-idor-a.md) |
| 267636 | Insecure Direct Object Reference (IDOR) | n/a | $1500 | [[NR Synthetics] (IDOR) Ability to see full name associated with other New Relic accounts through workaround of #255894](267636-nr-synthetics-idor-ability-to-see-full-name-associated-with.md) |
| 419875 | Insecure Direct Object Reference (IDOR) | n/a | $1500 | [[NR Alerts/Synthetics] IDOR through /policies.json with Synthetics exposes full name of other NR users](419875-nr-alerts-synthetics-idor-through-policies-json-with-synthet.md) |
| 344309 | Insecure Direct Object Reference (IDOR) | n/a | $1500 | [Adding a new user discloses their full name in the "Users" section of NR Alerts notification channels page](344309-adding-a-new-user-discloses-their-full-name-in-the-users-sec.md) |
| 347665 | Insecure Direct Object Reference (IDOR) | n/a | $1500 | [Permissions leaks the full name of other NR accounts - Regression of #267636](347665-permissions-leaks-the-full-name-of-other-nr-accounts-regress.md) |
| 271393 | Insecure Direct Object Reference (IDOR) | n/a | $1000 | [NR Internal_API call allows me to read the events/violations/policies/messages of ANY New Relic account (AND pull data from infrastructure)](271393-nr-internal-api-call-allows-me-to-read-the-events-violations.md) |
| 501672 | Privilege Escalation | n/a | $900 | [Restricted user can view all account invoices, payment method details, PII of account owner through zoura_api endpoints](501672-restricted-user-can-view-all-account-invoices-payment-method.md) |
| 1109620 | Deserialization of Untrusted Data | n/a | $768 | [Untrusted deserialization issue when loading newrelic.yml file in Java agent leads to code execution on host](1109620-untrusted-deserialization-issue-when-loading-newrelic-yml-fi.md) |
| 334143 | Privilege Escalation | n/a | $750 | [[NR Synthetics] Restricted User can add/modify alert conditions on monitors without any synthetics privileges ](334143-nr-synthetics-restricted-user-can-add-modify-alert-condition.md) |
| 520518 | Privilege Escalation | n/a | $750 | [Full name of other accounts exposed through NR API Explorer (another workaround of #476958)](520518-full-name-of-other-accounts-exposed-through-nr-api-explorer.md) |
| 479135 | Information Disclosure | n/a | $750 | [GET request to accounts.json on support site leaks the root account license key and the browser license key to a restricted user](479135-get-request-to-accounts-json-on-support-site-leaks-the-root.md) |
| 447975 | Privilege Escalation | n/a | $750 | [Upgrade menu exposes the mobile application token meant to only be visible to administrators ](447975-upgrade-menu-exposes-the-mobile-application-token-meant-to-o.md) |
| 388743 | Privilege Escalation | n/a | $750 | [[NR Insights] Data app permissions setting does not fully prevent other users from modifying/changing changing data related to your data app ](388743-nr-insights-data-app-permissions-setting-does-not-fully-prev.md) |
| 320689 | Privilege Escalation | n/a | $750 | [[NR Synthetics] Restricted user can view synthetics monitors and user permissions through .json endpoint at /permissions/securablemetadata/{GROUP ID}](320689-nr-synthetics-restricted-user-can-view-synthetics-monitors-a.md) |
| 320200 | Privilege Escalation | n/a | $750 | [[NR Alerts/Synthetics?] User with no Synthetics permissions can view synthetic monitor details through /internal_api/ endpoint](320200-nr-alerts-synthetics-user-with-no-synthetics-permissions-can.md) |
| 476958 | Privilege Escalation | n/a | $750 | [IDOR allows accounts to view full name of other accounts based on email through share notes feature](476958-idor-allows-accounts-to-view-full-name-of-other-accounts-bas.md) |
| 397483 | Privilege Escalation | n/a | $750 | [[NR Infrastructure] Restricted user can update integration provider account name via integrations API](397483-nr-infrastructure-restricted-user-can-update-integration-pro.md) |
| 386556 | Privilege Escalation | n/a | $750 | [[NR Alerts] Internal API exposes Synthetics monitor details to a restricted user without view monitor permissions](386556-nr-alerts-internal-api-exposes-synthetics-monitor-details-to.md) |
| 268541 | Business Logic Errors | n/a | $750 | [[Synthetics/Infrastructure/everything] Individual account permissions are not properly managed and inherited on sub accounts ](268541-synthetics-infrastructure-everything-individual-account-perm.md) |
| 638685 | Privilege Escalation | n/a | $750 | [Restricted user can add and delete tags of APM key transactions ](638685-restricted-user-can-add-and-delete-tags-of-apm-key-transacti.md) |
| 276174 | Privilege Escalation | n/a | $750 | [[NR Infrastructure] Bypass of #200576 through GraphQL query abuse - allows restricted user access to root account license key](276174-nr-infrastructure-bypass-of-200576-through-graphql-query-abu.md) |
| 387290 | Privilege Escalation | n/a | $750 | [NRQL Query allows restricted user to pull all data from Synthetics monitors without having read permissions enabled ](387290-nrql-query-allows-restricted-user-to-pull-all-data-from-synt.md) |
| 255685 | Privilege Escalation | n/a | $750 | [[New Relic Infrastructure] Restricted User can still integrate with AWS via forced browsing (plus, a few other bugs)](255685-new-relic-infrastructure-restricted-user-can-still-integrate.md) |
| 219356 | Business Logic Errors | n/a | $600 | [Manipulation of submit payment request allows me to obtain Infrastructure Pro/Other Services for free or at greatly reduced price](219356-manipulation-of-submit-payment-request-allows-me-to-obtain-i.md) |
| 957829 | Uncontrolled Resource Consumption | n/a | $500 | [Sending thousands of notifications with single request](957829-sending-thousands-of-notifications-with-single-request.md) |
| 347439 | CRLF Injection | n/a | $500 | [[synthetics.newrelic.com] SMTP header injection leads to (mass) arbitrary email sending](347439-synthetics-newrelic-com-smtp-header-injection-leads-to-mass.md) |
| 300879 | Privilege Escalation | n/a | $500 | [User to Admin privilege escalation in Infrastructure Conditions - /v2/accounts/1835740/alerts/conditions](300879-user-to-admin-privilege-escalation-in-infrastructure-conditi.md) |
| 520623 | Client-Side Enforcement of Server-Side Security | n/a | $500 | [Giving myself access to NR1 UI / one.newrelic.com without the proper feature flags on my account](520623-giving-myself-access-to-nr1-ui-one-newrelic-com-without-the.md) |
| 200576 | Privilege Escalation | n/a | $500 | [Logic flaw enables restricted account to access account license key](200576-logic-flaw-enables-restricted-account-to-access-account-lice.md) |
| 380413 | Privilege Escalation | n/a | $500 | [Restricted user can bypass permissions restriction to create NR Alert policies](380413-restricted-user-can-bypass-permissions-restriction-to-create.md) |
| 344468 | Client-Side Enforcement of Server-Side Security | n/a | $500 | [User is able to access and create private synthetics locations without upgrading (regression of #276157) ](344468-user-is-able-to-access-and-create-private-synthetics-locatio.md) |
| 479139 | Privilege Escalation | n/a | $500 | [Bypass of #447975 - view mobile application token though "Application Information" sidebar on Installation page ](479139-bypass-of-447975-view-mobile-application-token-though-applic.md) |
| 1021232 | Improper Authentication - Generic | n/a | $300 | [Account takeover by using  abandoned email id of victim which has already been changed to new  by victim himself on one.newrelic.com](1021232-account-takeover-by-using-abandoned-email-id-of-victim-which.md) |
| 976441 | Business Logic Errors | n/a | $250 | [removed user can still join the organization](976441-removed-user-can-still-join-the-organization.md) |
| 950180 | Code Injection | n/a | $250 | [HTML injection at Alert email](950180-html-injection-at-alert-email.md) |
| 202501 | Improper Authentication - Generic | n/a | $250 | [Restricted user is able to delete filter sets of admin users in https://infrastructure.newrelic.com/accounts/{{ACC#}}/settings/filterSets](202501-restricted-user-is-able-to-delete-filter-sets-of-admin-users.md) |
| 460428 | Information Exposure Through an Error Message | n/a | $200 | [The impossibility of inclusion of the trial (BROWSER)](460428-the-impossibility-of-inclusion-of-the-trial-browser.md) |
| 957874 | Adding your account to victim's app via deeplink | n/a | $100 | [Adding your account to victim's app via deeplink](957874-adding-your-account-to-victim-s-app-via-deeplink.md) |
| 708589 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [Unsafe charts embedding implementation leads to cross-account stored XSS and SSRF](708589-unsafe-charts-embedding-implementation-leads-to-cross-accoun.md) |
| 709883 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [Cross-account stored XSS at embedded charts](709883-cross-account-stored-xss-at-embedded-charts.md) |
| 507132 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [Stored XSS in notes (charts) because of insecure chart data JSON generation](507132-stored-xss-in-notes-charts-because-of-insecure-chart-data-js.md) |
| 1386438 | Cross-site Scripting (XSS) - Reflected | n/a | $0 | [Reflected XSS in VPN Appliance](1386438-reflected-xss-in-vpn-appliance.md) |
| 587829 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [CSTI at Plugin page leading to active stored XSS (Publisher name)](587829-csti-at-plugin-page-leading-to-active-stored-xss-publisher-n.md) |
| 602527 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [Urgent! Stored XSS at plugin's violations leading to account takeover](602527-urgent-stored-xss-at-plugin-s-violations-leading-to-account.md) |
| 698416 | Open Redirect | n/a | $0 | [Host Header Injection](698416-host-header-injection.md) |
| 363971 | Privilege Escalation | n/a | $0 | [Insecure Infrastructure Integrations YML Loading leads to Windows Privilege Escalation](363971-insecure-infrastructure-integrations-yml-loading-leads-to-wi.md) |
| 1367642 | Cross-site Scripting (XSS) - Reflected | n/a | $0 | [ Reflected Cross site Scripting (XSS) on https://one.newrelic.com](1367642-reflected-cross-site-scripting-xss-on-https-one-newrelic-com.md) |
| 681001 | Insecure Direct Object Reference (IDOR) | n/a | $0 | [User can run monitors at private locations, which he has no access to](681001-user-can-run-monitors-at-private-locations-which-he-has-no-a.md) |
| 198690 | Server-Side Request Forgery (SSRF) | n/a | $0 | [SSRF in alerts.newrelic.com exposes entire internal network](198690-ssrf-in-alerts-newrelic-com-exposes-entire-internal-network.md) |
| 267781 | Privilege Escalation | n/a | $0 | [Users can enable API access for free via mass assignment](267781-users-can-enable-api-access-for-free-via-mass-assignment.md) |
| 132835 | Information Disclosure | n/a | $0 | [Cache-Control Misconfiguration Leads to Sensitive Information Leakage](132835-cache-control-misconfiguration-leads-to-sensitive-informatio.md) |
| 207285 | Open Redirect | n/a | $0 | [Open redirection ](207285-open-redirection.md) |
| 566400 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [Stored XSS firing at the "Add chart to note" popup](566400-stored-xss-firing-at-the-add-chart-to-note-popup.md) |
| 549084 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [Stored XSS firing at transaction map (applicationName field)](549084-stored-xss-firing-at-transaction-map-applicationname-field.md) |
| 197059 | Improper Authentication - Generic | n/a | $0 | [A user with restricted privileges is able to view Phone Number + Billing Email of account owner](197059-a-user-with-restricted-privileges-is-able-to-view-phone-numb.md) |
| 154278 | Cache purge requests are not authenticated | n/a | $0 | [Cache purge requests are not authenticated](154278-cache-purge-requests-are-not-authenticated.md) |
| 127202 | Improper Authentication - Generic | n/a | $0 | [Mobile Authentication Endpoint Credentials Brute-Force Vulnerability](127202-mobile-authentication-endpoint-credentials-brute-force-vulne.md) |
| 344032 | Server-Side Request Forgery (SSRF) | n/a | $0 | [Blind SSRF in Ticketing Integrations Jira webhooks leading to internal network enumeration and blind HTTP requests](344032-blind-ssrf-in-ticketing-integrations-jira-webhooks-leading-t.md) |
| 567468 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [Stored XSS at APM key transactions list](567468-stored-xss-at-apm-key-transactions-list.md) |
| 530511 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [Stored XSS at APM applications listing](530511-stored-xss-at-apm-applications-listing.md) |
| 263169 | Information Disclosure | n/a | $0 | [Internal Ports Scanning via Blind SSRF](263169-internal-ports-scanning-via-blind-ssrf.md) |
| 141304 | Information Disclosure | n/a | $0 | [Blind SSRF on synthetics.newrelic.com](141304-blind-ssrf-on-synthetics-newrelic-com.md) |
| 138863 | Improper Authentication - Generic | n/a | $0 | [Missing rate limit on password](138863-missing-rate-limit-on-password.md) |
| 710535 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [Cross-account stored XSS at notes (through "swf" note parameter)](710535-cross-account-stored-xss-at-notes-through-swf-note-parameter.md) |
| 427373 | Swiftype key stored in JavaScript source | n/a | $0 | [Swiftype key stored in JavaScript source](427373-swiftype-key-stored-in-javascript-source.md) |
| 384882 | Remote File Inclusion | n/a | $0 | [stamp2-azure-ext.newrelic.com is vulnerable to MS12-020](384882-stamp2-azure-ext-newrelic-com-is-vulnerable-to-ms12-020.md) |
| 168108 | Improper Authentication - Generic | n/a | $0 | [SSO Authentication Bypass](168108-sso-authentication-bypass.md) |
| 129138 | Cryptographic Issues - Generic | n/a | $0 | [APT repository is signed using weak digest (SHA-1)](129138-apt-repository-is-signed-using-weak-digest-sha-1.md) |
| 277300 | Privacy Violation | n/a | $0 | [Captcha Bypass on SignUp Form](277300-captcha-bypass-on-signup-form.md) |
| 207381 | Privilege Escalation | n/a | $0 | [[docs-ra.newrelic.com] subdomain and Drupal takeover via unconfigured endpoint](207381-docs-ra-newrelic-com-subdomain-and-drupal-takeover-via-uncon.md) |
| 197726 | Improper Authentication - Generic | n/a | $0 | [newrelic.atlassian.net - jira information disclosure](197726-newrelic-atlassian-net-jira-information-disclosure.md) |
| 123095 | Cross-Site Request Forgery (CSRF) | n/a | $0 | [CSRF- delete all empty server policy](123095-csrf-delete-all-empty-server-policy.md) |
| 167460 | Improper Authentication - Generic | n/a | $0 | [Session Hijacking ](167460-session-hijacking.md) |
| 130739 | Information Disclosure | n/a | $0 | [Sensitive information contained with New Relic APM iOS application](130739-sensitive-information-contained-with-new-relic-apm-ios-appli.md) |
| 123089 | Improper Authentication - Generic | n/a | $0 | [Vulnerable Link Leaks the User Names](123089-vulnerable-link-leaks-the-user-names.md) |
| 114796 | Violation of Secure Design Principles | n/a | $0 | [No validation on account names](114796-no-validation-on-account-names.md) |
| 1197160 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [GitHub Integration doesn't sanitize repository URLs which might be attacker-controlled](1197160-github-integration-doesn-t-sanitize-repository-urls-which-mi.md) |
| 680240 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [Stored XSS at Synthetics private locations (planted through location label or description)](680240-stored-xss-at-synthetics-private-locations-planted-through-l.md) |
| 197436 | Improper Authentication - Generic | n/a | $0 | [Restricted User is able to edit Alert Conditions of Synthetics Monitors even if Synthetics Permissions is enabled by an admin](197436-restricted-user-is-able-to-edit-alert-conditions-of-syntheti.md) |
| 941421 | Code Injection | n/a | $0 | [One Click Remote Code Injection - *.blog.newrelic.com](941421-one-click-remote-code-injection-blog-newrelic-com.md) |
| 706533 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [Stored XSS at Mobile (Versions tab)](706533-stored-xss-at-mobile-versions-tab.md) |
| 700091 | Man-in-the-Middle | n/a | $0 | [Mixed content issues on newrelic.com](700091-mixed-content-issues-on-newrelic-com.md) |
| 690536 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [Passive stored XSS at Synthetics job result page (View resource)](690536-passive-stored-xss-at-synthetics-job-result-page-view-resour.md) |
| 329407 | Privilege Escalation | n/a | $0 | [Drupal admin takeover via install.php not being performed prior to install.](329407-drupal-admin-takeover-via-install-php-not-being-performed-pr.md) |
| 271861 | Insecure Direct Object Reference (IDOR) | n/a | $0 | [Bypass of my two other reports #267636 + #255894 - (IDOR) Ability to see full name associated with other New Relic accounts](271861-bypass-of-my-two-other-reports-267636-255894-idor-ability-to.md) |
| 139970 | Information Disclosure | n/a | $0 | [JIRA account misconfig causes internal info leak](139970-jira-account-misconfig-causes-internal-info-leak.md) |
| 123078 | Open Redirect | n/a | $0 | [https://rpm.newrelic.com/login vulnerable to host header attack](123078-https-rpm-newrelic-com-login-vulnerable-to-host-header-attac.md) |
| 1173219 | Code Injection | n/a | $0 | [HTML Injection In Email In one.newrelic.com](1173219-html-injection-in-email-in-one-newrelic-com.md) |
| 727368 | Open Redirect | n/a | $0 | [[Bypass] Code injection to open redirect in https://insights.newrelic.com/accounts/2521182/dashboards/1026927](727368-bypass-code-injection-to-open-redirect-in-https-insights-new.md) |
| 225326 | CSRF For Adding Users | n/a | $0 | [CSRF For Adding Users](225326-csrf-for-adding-users.md) |
| 157270 | Cross-Site Request Forgery (CSRF) | n/a | $0 | [CSRF vulnerability that allows an attacker to purge plugin metric data](157270-csrf-vulnerability-that-allows-an-attacker-to-purge-plugin-m.md) |
| 154855 | Information Disclosure | n/a | $0 | [Leaking license key in source code](154855-leaking-license-key-in-source-code.md) |
| 152944 | Improper Authentication - Generic | n/a | $0 | [Session Management Flaw](152944-session-management-flaw.md) |
| 141682 | Information Disclosure | n/a | $0 | [SSRF on synthetics.newrelic.com permitting access to sensitive data](141682-ssrf-on-synthetics-newrelic-com-permitting-access-to-sensiti.md) |
| 787886 | Insecure Direct Object Reference (IDOR) | n/a | $0 | [Ability to run monitors' jobs of other accounts and to read these jobs content (including the secure credentials values)](787886-ability-to-run-monitors-jobs-of-other-accounts-and-to-read-t.md) |
| 751699 | Improper Access Control - Generic | n/a | $0 | [NR-wide cross account access through misconfigured CORS-policy of multiple endpoints](751699-nr-wide-cross-account-access-through-misconfigured-cors-poli.md) |
| 667770 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [Stored XSS at APM transaction map (transactionName field)](667770-stored-xss-at-apm-transaction-map-transactionname-field.md) |
| 504782 | Cross-Site Request Forgery (CSRF) | n/a | $0 | [CSRF at adding new role (user-management.service.newrelic.com)](504782-csrf-at-adding-new-role-user-management-service-newrelic-com.md) |
| 178537 | Potential sub-domain hijacking | n/a | $0 | [Potential sub-domain hijacking](178537-potential-sub-domain-hijacking.md) |
| 123172 | Open Redirect | n/a | $0 | [Open redirection on login](123172-open-redirection-on-login.md) |
| 123092 | Cross-Site Request Forgery (CSRF) | n/a | $0 | [CSRF - Delete all empty application policy](123092-csrf-delete-all-empty-application-policy.md) |
| 385420 | Violation of Secure Design Principles | n/a | $0 | [ Missing security best practices (leads to further impact) ](385420-missing-security-best-practices-leads-to-further-impact.md) |
| 221250 | Information Disclosure | n/a | $0 | [/accounts/USERID.json file is left open for Restricted User of organization disclosing Owners's Mobile Number and "billing_info, cc_email"](221250-accounts-userid-json-file-is-left-open-for-restricted-user-o.md) |
| 210298 | Privilege Escalation | n/a | $0 | [Privilege Escalation in Default Notification Preferences](210298-privilege-escalation-in-default-notification-preferences.md) |
| 146875 | http://newrelic.com SSRF/XSPA | n/a | $0 | [http://newrelic.com SSRF/XSPA](146875-http-newrelic-com-ssrf-xspa.md) |
| 127032 | Command Injection - Generic | n/a | $0 | [CSV Injection in sub_accounts.csv](127032-csv-injection-in-sub-accounts-csv.md) |
| 123435 | Privilege Escalation | n/a | $0 | [Normal user can set "Job title" of other users by Direct Object Reference](123435-normal-user-can-set-job-title-of-other-users-by-direct-objec.md) |
| 123091 | Memory Corruption - Generic | n/a | $0 | [No Rate Limitation on Promo Code](123091-no-rate-limitation-on-promo-code.md) |
| 119090 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [Reflected XSS on Signup Page](119090-reflected-xss-on-signup-page.md) |
| 969456 | Getting API access key Through  Introspection query Graphql | n/a | $0 | [Getting API access key Through  Introspection query Graphql](969456-getting-api-access-key-through-introspection-query-graphql.md) |
| 789305 | Insufficient Session Expiration | n/a | $0 | [Bypassing Protection Mechanism: Change of Account Name after Session Log out ](789305-bypassing-protection-mechanism-change-of-account-name-after.md) |
| 783688 | Business Logic Errors | n/a | $0 | [Ability to buy PRO subscriptions by arbitrary reduced prices](783688-ability-to-buy-pro-subscriptions-by-arbitrary-reduced-prices.md) |
| 776449 | Improper Access Control - Generic | n/a | $0 | [Restricted user can update Apdex target for applications by leveraging the GraphQL mutation](776449-restricted-user-can-update-apdex-target-for-applications-by.md) |
| 629113 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [CSTI fix (#587829) bypass leading to stored XSS at plugins again](629113-csti-fix-587829-bypass-leading-to-stored-xss-at-plugins-agai.md) |
| 530871 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [Stored XSS firing if the error occurs when trying to delete the APM app](530871-stored-xss-firing-if-the-error-occurs-when-trying-to-delete.md) |
| 512102 | Cross-Site Request Forgery (CSRF) | n/a | $0 | [CSRF at acknowledging an incident](512102-csrf-at-acknowledging-an-incident.md) |
| 216271 | Cryptographic Issues - Generic | n/a | $0 | [SSL Padding Oracle On Downgraded Legacy Encryption (POODLE) Vulnerability](216271-ssl-padding-oracle-on-downgraded-legacy-encryption-poodle-vu.md) |
| 198221 | Improper Authentication - Generic | n/a | $0 | [Restricted User can view multiple account details including customer_root_account_id, payment method, date of first payment, etc.](198221-restricted-user-can-view-multiple-account-details-including.md) |
| 183577 | Sub domain issues. | n/a | $0 | [Sub domain issues.](183577-sub-domain-issues.md) |
| 182414 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [Stored XSS on BillingCountry parameter](182414-stored-xss-on-billingcountry-parameter.md) |
| 181528 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [Cross site scripting in a subdomain of newrelic.com](181528-cross-site-scripting-in-a-subdomain-of-newrelic-com.md) |
| 176494 | Open Redirect | n/a | $0 | [Hyperlink Injection on adding active users](176494-hyperlink-injection-on-adding-active-users.md) |
| 153634 | Privilege Escalation | n/a | $0 | [[alerts.newrelic.com] Scanning local network via notification channel](153634-alerts-newrelic-com-scanning-local-network-via-notification.md) |
| 139502 | Privilege Escalation | n/a | $0 | [Privilege Escalation In Moniter](139502-privilege-escalation-in-moniter.md) |
| 139178 | Improper Session Management | n/a | $0 | [Improper Session Management](139178-improper-session-management.md) |
| 134032 | Code Injection | n/a | $0 | [newrelic.com rails directory traversal vuln](134032-newrelic-com-rails-directory-traversal-vuln.md) |
| 131552 | Open Redirect | n/a | $0 | [Login Open Redirect](131552-login-open-redirect.md) |
| 127741 | Open Redirect | n/a | $0 | [Open redirection bypass](127741-open-redirection-bypass.md) |
| 127026 | User enumeration possible from log-in timing difference | n/a | $0 | [User enumeration possible from log-in timing difference](127026-user-enumeration-possible-from-log-in-timing-difference.md) |
| 123074 | Information Disclosure | n/a | $0 | [https://rpm.newrelic.com/.htaccess file is world readable](123074-https-rpm-newrelic-com-htaccess-file-is-world-readable.md) |
| 1250631 | Insufficient Session Expiration | n/a | $0 | [Verification Link not expiring leading to Account Takeover.](1250631-verification-link-not-expiring-leading-to-account-takeover.md) |
| 975749 | Insecure Direct Object Reference (IDOR) | n/a | $0 | [IDOR - User is able to download charts/dashboards from cross accounts](975749-idor-user-is-able-to-download-charts-dashboards-from-cross-a.md) |
| 786109 | Insecure Direct Object Reference (IDOR) | n/a | $0 | [Attacker can create new account inside any partnership with no approve from the Partnership owner](786109-attacker-can-create-new-account-inside-any-partnership-with.md) |
| 766145 | Improper Access Control - Generic | n/a | $0 | [Restricted user can remove NerdStorage documents/collections scoped to ACCOUNT or ENTITY](766145-restricted-user-can-remove-nerdstorage-documents-collections.md) |
| 765565 | Insecure Direct Object Reference (IDOR) | n/a | $0 | [Cross-account reading of Insights dashboards through GraphQL](765565-cross-account-reading-of-insights-dashboards-through-graphql.md) |
| 757957 | Improper Access Control - Generic | n/a | $0 | [Restricted user can manage the NerdGraph entities' tags](757957-restricted-user-can-manage-the-nerdgraph-entities-tags.md) |
| 605845 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [Stored admin-to-owner XSS at infrastructure alerts runbook URL leading to account takeover by malicious admin](605845-stored-admin-to-owner-xss-at-infrastructure-alerts-runbook-u.md) |
| 534711 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [Stored XSS at APM apps labels autocomplete dropdown (apps listing)](534711-stored-xss-at-apm-apps-labels-autocomplete-dropdown-apps-lis.md) |
| 414427 | Information Disclosure | n/a | $0 | [WordPress username enumeration (/author)](414427-wordpress-username-enumeration-author.md) |
| 390537 | Business Logic Errors | n/a | $0 | [DNS misconfiguration on email.alerts.newrelic.com](390537-dns-misconfiguration-on-email-alerts-newrelic-com.md) |
| 177485 | Open Redirect | n/a | $0 | [Open Redirect ](177485-open-redirect.md) |
| 167809 | Open Redirect | n/a | $0 | [HOST HEADER INJECTION in rpm.newrelic.com ](167809-host-header-injection-in-rpm-newrelic-com.md) |
| 163227 | Improper Authentication - Generic | n/a | $0 | [Cookie Misconfiguration](163227-cookie-misconfiguration.md) |
| 156992 | Cross-Site Request Forgery (CSRF) | n/a | $0 | [Login CSRF vulnerability](156992-login-csrf-vulnerability.md) |
| 152368 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [XSS in a newrelic.com site](152368-xss-in-a-newrelic-com-site.md) |
| 146318 | Open Redirect | n/a | $0 | [Html injection in monitor name textbox](146318-html-injection-in-monitor-name-textbox.md) |
| 144525 | Open Redirect | n/a | $0 | [Open redirection bypass .](144525-open-redirection-bypass.md) |
| 140275 | Cross-Site Request Forgery (CSRF) | n/a | $0 | [No CSRF validation on Account Monitors in Synthetics Block](140275-no-csrf-validation-on-account-monitors-in-synthetics-block.md) |
| 137480 | New Relic - Session Hijacking | n/a | $0 | [New Relic - Session Hijacking](137480-new-relic-session-hijacking.md) |
| 132251 | Open Redirect | n/a | $0 | [Open redirection ](132251-open-redirection.md) |
| 127766 | Information Disclosure | n/a | $0 | [Password disclosure during signup process](127766-password-disclosure-during-signup-process.md) |
| 123513 | Host Header Injection / Cache Poisoning | n/a | $0 | [Host Header Injection / Cache Poisoning](123513-host-header-injection-cache-poisoning.md) |
| 115922 | Privilege Escalation | n/a | $0 | [[download.newrelic.com] Access to private directories](115922-download-newrelic-com-access-to-private-directories.md) |
| 114870 | Improper Authentication - Generic | n/a | $0 | [Basic Authorization over HTTP](114870-basic-authorization-over-http.md) |
| 114807 | Open Redirect | n/a | $0 | [Unsafe HTML in reset password email    and Account verification in email  is missing in Sign up](114807-unsafe-html-in-reset-password-email-and-account-verification.md) |
| 114799 | Cross-Site Request Forgery (CSRF) | n/a | $0 | [A Signup page does not properly validate the authenticity token at the server side.](114799-a-signup-page-does-not-properly-validate-the-authenticity-to.md) |
| 796013 | CRLF Injection | n/a | $0 | [CRLF Injection in email address](796013-crlf-injection-in-email-address.md) |
| 788499 | Improper Access Control - Generic | n/a | $0 | [Secure credentials values disclosure to regular users due to access control issue in monitor creating function](788499-secure-credentials-values-disclosure-to-regular-users-due-to.md) |
| 782703 | Violation of Secure Design Principles | n/a | $0 | [Account owner/admin can't actually delete personal users' API keys](782703-account-owner-admin-can-t-actually-delete-personal-users-api.md) |
| 746786 | Information Disclosure | n/a | $0 | [Disclosure of locally served nerdpacks due to nr-local.net CORS policy misconfiguration](746786-disclosure-of-locally-served-nerdpacks-due-to-nr-local-net-c.md) |
| 614947 | UI Redressing (Clickjacking) | n/a | $0 | [Site-wide clickjacking at IE11](614947-site-wide-clickjacking-at-ie11.md) |
| 210304 | Privilege Escalation | n/a | $0 | [Privilege Escalation in Share Report](210304-privilege-escalation-in-share-report.md) |
| 207505 | Open Redirect | n/a | $0 | [Unvalidated redirect in alerts.newrelic.com/auth/newrelic?origin=](207505-unvalidated-redirect-in-alerts-newrelic-com-auth-newrelic-or.md) |
| 207384 | Information Disclosure | n/a | $0 | [Directory listing - i am able to download all php_agent archive](207384-directory-listing-i-am-able-to-download-all-php-agent-archiv.md) |
| 163547 | Code Injection | n/a | $0 | [Java RMI (Remote Code Execution)](163547-java-rmi-remote-code-execution.md) |
| 132658 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [Stored Cross-Site Scripting via Angular Template Injection](132658-stored-cross-site-scripting-via-angular-template-injection.md) |
| 128645 | Improper Authentication - Generic | n/a | $0 | [Clickjacking on authenticated pages which is inscope for New Relic](128645-clickjacking-on-authenticated-pages-which-is-inscope-for-new.md) |
| 127028 | Old CAPTCHA offers no protection | n/a | $0 | [Old CAPTCHA offers no protection](127028-old-captcha-offers-no-protection.md) |
| 123183 | Improper Authentication - Generic | n/a | $0 | [All the active session should destroy when user change his password](123183-all-the-active-session-should-destroy-when-user-change-his-p.md) |
| 123127 | no email confirmation on signup | n/a | $0 | [no email confirmation on signup](123127-no-email-confirmation-on-signup.md) |
| 123126 | newrelic.com vulnerable to clickjacking ! | n/a | $0 | [newrelic.com vulnerable to clickjacking !](123126-newrelic-com-vulnerable-to-clickjacking.md) |
| 116315 | Open Redirect | n/a | $0 | [open redirection at login](116315-open-redirection-at-login.md) |
| 116243 | Privilege Escalation | n/a | $0 | [Potential Subdomain Takeover - http://storefront.newrelic.com/](116243-potential-subdomain-takeover-http-storefront-newrelic-com.md) |
| 116179 | Improper Authentication - Generic | n/a | $0 | [Unauthorized Access](116179-unauthorized-access.md) |
| 115860 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [[login.newrelic.com] XSS via return_to](115860-login-newrelic-com-xss-via-return-to.md) |
| 115628 | Violation of Secure Design Principles | n/a | $0 | [SUBDOMAIN TAKEOVER(FIXED)](115628-subdomain-takeover-fixed.md) |
| 114797 | Cross-Site Request Forgery (CSRF) | n/a | $0 | [A Log in page does not properly validate the authenticity token at the server side](114797-a-log-in-page-does-not-properly-validate-the-authenticity-to.md) |
| 966531 | Improper Access Control - Generic | n/a | $0 | ["Basic user" which can only access a limited subset of the platform can access certain pages which are restricted to the user by the account owner.](966531-basic-user-which-can-only-access-a-limited-subset-of-the-pla.md) |
| 694943 | Can fake content email of newrelic to any user | n/a | $0 | [Can fake content email of newrelic to any user](694943-can-fake-content-email-of-newrelic-to-any-user.md) |
| 170241 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [Stored Xss in rpm.newrelic.com](170241-stored-xss-in-rpm-newrelic-com.md) |
| 157450 | Improper Authentication - Generic | n/a | $0 | [All Active user sessions should be destroyed when user change his password!](157450-all-active-user-sessions-should-be-destroyed-when-user-chang.md) |
| 140333 | Session takeover | n/a | $0 | [Session takeover](140333-session-takeover.md) |
| 127203 | rpm.newrelic.com - monitor creation to other accounts | n/a | $0 | [rpm.newrelic.com - monitor creation to other accounts](127203-rpm-newrelic-com-monitor-creation-to-other-accounts.md) |
| 125400 | Memory Corruption - Generic | n/a | $0 | [Too many included lookups](125400-too-many-included-lookups.md) |
| 124724 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [Stored XSS through Angular Expression Sandbox Escape](124724-stored-xss-through-angular-expression-sandbox-escape.md) |
| 123649 | Command Injection - Generic | n/a | $0 | [Synthetics Xss](123649-synthetics-xss.md) |
| 123120 | Improper Authentication - Generic | n/a | $0 | [Emails and alert policies can be altered by malicious users.](123120-emails-and-alert-policies-can-be-altered-by-malicious-users.md) |
| 122697 | Information Disclosure | n/a | $0 | [Server Side Browsing - localhost open port enumeration](122697-server-side-browsing-localhost-open-port-enumeration.md) |
| 119148 | Cross-Site Request Forgery (CSRF) | n/a | $0 | [CSRF - Regenerate all admin api keys](119148-csrf-regenerate-all-admin-api-keys.md) |
| 115817 | Information Disclosure | n/a | $0 | [WordPress User Enumeration - blog.newrelic.com](115817-wordpress-user-enumeration-blog-newrelic-com.md) |
| 114852 | Open Redirect | n/a | $0 | [Html injection in monitor name  textbox](114852-html-injection-in-monitor-name-textbox.md) |
| 277262 | Improper Authentication - Generic | n/a | $0 | [Newrelic s3 bucket is writeable and deleteable by authorized AWS users](277262-newrelic-s3-bucket-is-writeable-and-deleteable-by-authorized.md) |
| 207388 | Information Disclosure | n/a | $0 | [Sensitive information disclosure](207388-sensitive-information-disclosure.md) |
| 205309 | Improper Authentication - Generic | n/a | $0 | [Broken Authentication and session management OWASP A2](205309-broken-authentication-and-session-management-owasp-a2.md) |
| 194952 | Moniter Failed Sends too many emails | n/a | $0 | [Moniter Failed Sends too many emails](194952-moniter-failed-sends-too-many-emails.md) |
| 176477 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [XSS (Reflected)](176477-xss-reflected.md) |
| 123915 | Information Disclosure | n/a | $0 | [Insecure transition from HTTP to HTTPS in form post](123915-insecure-transition-from-http-to-https-in-form-post.md) |
