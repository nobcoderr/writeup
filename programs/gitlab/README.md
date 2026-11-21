# GitLab

Disclosed reports: **258**

| ID | Temuan | Severity | Bounty | Writeup |
| --- | --- | --- | ---: | --- |
| 2293343 | Improper Access Control - Generic | critical | $35000 | [Account Takeover via Password Reset without user interactions](2293343-account-takeover-via-password-reset-without-user-interaction.md) |
| 1679624 | Command Injection - Generic | critical | $33510 | [Remote Command Execution via Github import](1679624-remote-command-execution-via-github-import.md) |
| 1609965 | Command Injection - Generic | critical | $33510 | [RCE via the DecompressedArchiveSizeValidator and Project BulkImports (behind feature flag)](1609965-rce-via-the-decompressedarchivesizevalidator-and-project-bul.md) |
| 1439593 | Path Traversal | critical | $29000 | [Arbitrary file read  via the bulk imports UploadsPipeline](1439593-arbitrary-file-read-via-the-bulk-imports-uploadspipeline.md) |
| 1685822 | Improper Access Control - Generic | medium | $22300 | [RepositoryPipeline allows importing of local git repos](1685822-repositorypipeline-allows-importing-of-local-git-repos.md) |
| 827052 | Path Traversal | critical | $20000 | [Arbitrary file read via the UploadsRewriter when moving and issue](827052-arbitrary-file-read-via-the-uploadsrewriter-when-moving-and.md) |
| 1154542 | Code Injection | critical | $20000 | [RCE when removing metadata with ExifTool](1154542-rce-when-removing-metadata-with-exiftool.md) |
| 1125425 | Code Injection | critical | $20000 | [RCE via unsafe inline Kramdown options when rendering certain Wiki pages](1125425-rce-via-unsafe-inline-kramdown-options-when-rendering-certai.md) |
| 743953 | Insecure Direct Object Reference (IDOR) | critical | $20000 | [Steal private objects of other projects via project import](743953-steal-private-objects-of-other-projects-via-project-import.md) |
| 767770 | Insecure Direct Object Reference (IDOR) | critical | $20000 | [Private objects exposed through project import](767770-private-objects-exposed-through-project-import.md) |
| 1212067 | Cross-site Scripting (XSS) - Stored | critical | $16000 | [Stored XSS in markdown via the DesignReferenceFilter ](1212067-stored-xss-in-markdown-via-the-designreferencefilter.md) |
| 1132378 | Path Traversal | critical | $16000 | [Arbitrary file read during project import](1132378-arbitrary-file-read-during-project-import.md) |
| 1731349 | Cross-site Scripting (XSS) - Stored | high | $13950 | [Stored XSS via Kroki diagram](1731349-stored-xss-via-kroki-diagram.md) |
| 1578400 | Cross-site Scripting (XSS) - Stored | high | $13950 | [New /add_contacts /remove_contacts quick commands susseptible to XSS from Customer Contact firstname/lastname fields](1578400-new-add-contacts-remove-contacts-quick-commands-susseptible.md) |
| 658013 | Command Injection - Generic | critical | $12000 | [Git flag injection - local file overwrite to remote code execution](658013-git-flag-injection-local-file-overwrite-to-remote-code-execu.md) |
| 587854 | Command Injection - Generic | critical | $12000 | [Local files could be overwritten in GitLab, leading to remote command execution](587854-local-files-could-be-overwritten-in-gitlab-leading-to-remote.md) |
| 689314 | Privilege Escalation | critical | $12000 | [Project Template functionality can be used to copy private project data, such as repository, confidential issues, snippets, and merge requests](689314-project-template-functionality-can-be-used-to-copy-private-p.md) |
| 509924 | Information Disclosure | critical | $12000 | [JSON serialization of any Project model results in all Runner tokens being exposed through Quick Actions](509924-json-serialization-of-any-project-model-results-in-all-runne.md) |
| 894569 | Business Logic Errors | critical | $12000 | [An attacker can run pipeline jobs as arbitrary user](894569-an-attacker-can-run-pipeline-jobs-as-arbitrary-user.md) |
| 733072 | Command Injection - Generic | high | $12000 | [Path traversal, to RCE](733072-path-traversal-to-rce.md) |
| 822262 | Path Traversal | high | $12000 | [Path traversal in Nuget Package Registry](822262-path-traversal-in-nuget-package-registry.md) |
| 446585 | Improper Access Control - Generic | critical | $11000 | [Exfiltrate and mutate repository and project data through injected templated service](446585-exfiltrate-and-mutate-repository-and-project-data-through-in.md) |
| 850447 | Information Disclosure | critical | $10000 | [gitlab-workhorse bypass in Gitlab::Middleware::Multipart allowing files in `allowed_paths` to be read](850447-gitlab-workhorse-bypass-in-gitlab-middleware-multipart-allow.md) |
| 826361 | Server-Side Request Forgery (SSRF) | high | $10000 | [SSRF on project import via the remote_attachment_url on a Note](826361-ssrf-on-project-import-via-the-remote-attachment-url-on-a-no.md) |
| 1040786 | Improper Authentication - Generic | high | $10000 | [Exposure of a valid Gitlab-Workhorse JWT leading to various bad things](1040786-exposure-of-a-valid-gitlab-workhorse-jwt-leading-to-various.md) |
| 1543718 | Uncontrolled Resource Consumption | high | $7640 | [DOS via issue preview](1543718-dos-via-issue-preview.md) |
| 682442 | Command Injection - Generic | high | $7000 | [Git flag injection - Search API with scope 'blobs' ](682442-git-flag-injection-search-api-with-scope-blobs.md) |
| 1098793 | Improper Access Control - Generic | high | $5600 | [Kroki Arbitrary File Read/Write ](1098793-kroki-arbitrary-file-read-write.md) |
| 1148364 | Improper Authentication - Generic | high | $5580 | [Mint Oauth2 access token for targeted user](1148364-mint-oauth2-access-token-for-targeted-user.md) |
| 836649 | Cross-site Scripting (XSS) - Stored | high | $5000 | [Stored XSS in markdown when redacting references](836649-stored-xss-in-markdown-when-redacting-references.md) |
| 960244 | Type Confusion | high | $5000 | [Insufficient Type Check leading to Developer ability to delete Project, Repository, Group, ...](960244-insufficient-type-check-leading-to-developer-ability-to-dele.md) |
| 508184 | Cross-site Scripting (XSS) - Stored | high | $4500 | [Persistent XSS in Note objects](508184-persistent-xss-in-note-objects.md) |
| 398799 | Server-Side Request Forgery (SSRF) | high | $4000 | [Unauthenticated blind SSRF in OAuth Jira authorization controller](398799-unauthenticated-blind-ssrf-in-oauth-jira-authorization-contr.md) |
| 946728 | Cross-site Scripting (XSS) - Reflected | high | $4000 | [SafeParamsHelper::safe_params is not so safe](946728-safeparamshelper-safe-params-is-not-so-safe.md) |
| 858671 | Improper Access Control - Generic | high | $4000 | [Insufficient Type Check on GraphQL leading to Maintainer delete repository](858671-insufficient-type-check-on-graphql-leading-to-maintainer-del.md) |
| 662287 | UI Redressing (Clickjacking) | high | $3500 | [Cross-site Scripting (XSS) - Stored in RDoc wiki pages](662287-cross-site-scripting-xss-stored-in-rdoc-wiki-pages.md) |
| 653125 | Command Injection - Generic | critical | $3500 | [Git flag injection leading to file overwrite and potential remote code execution](653125-git-flag-injection-leading-to-file-overwrite-and-potential-r.md) |
| 460545 | Information Exposure Through an Error Message | high | $3500 | [information disclosure of secret_key_base via encoding charcters](460545-information-disclosure-of-secret-key-base-via-encoding-charc.md) |
| 723307 | Cross-site Scripting (XSS) - Stored | high | $3500 | [Stored XSS in merge request pages](723307-stored-xss-in-merge-request-pages.md) |
| 1122408 | Cross-Site Request Forgery (CSRF) | high | $3370 | [CSRF on /api/graphql allows executing mutations through GET requests](1122408-csrf-on-api-graphql-allows-executing-mutations-through-get-r.md) |
| 922456 | Authentication Bypass Using an Alternate Path or Channel | high | $3000 | [Ability to bypass email verification for OAuth grants results in accounts takeovers on 3rd parties](922456-ability-to-bypass-email-verification-for-oauth-grants-result.md) |
| 470067 | Uncontrolled Resource Consumption | medium | $3000 | [DoS on the Issue page by exploiting Mermaid.](470067-dos-on-the-issue-page-by-exploiting-mermaid.md) |
| 1198517 | Cross-site Scripting (XSS) - Stored | high | $3000 | [Stored XSS in custom emoji](1198517-stored-xss-in-custom-emoji.md) |
| 402658 | Cross-site Scripting (XSS) - Stored | medium | $3000 | [XSS in request approvals](402658-xss-in-request-approvals.md) |
| 1106238 | Cross-site Scripting (XSS) - Stored | high | $3000 | [Stored XSS via Mermaid Prototype Pollution vulnerability](1106238-stored-xss-via-mermaid-prototype-pollution-vulnerability.md) |
| 1401444 | OS Command Injection | n/a | $3000 | [RCE via WikiCloth markdown rendering if the `rubyluabridge` gem is installed](1401444-rce-via-wikicloth-markdown-rendering-if-the-rubyluabridge-ge.md) |
| 856554 | Cross-site Scripting (XSS) - Stored | high | $3000 | [Stored XSS on the job page](856554-stored-xss-on-the-job-page.md) |
| 1280002 | Cross-site Scripting (XSS) - Stored | high | $3000 | [Stored XSS via Mermaid Prototype Pollution vulnerability](1280002-stored-xss-via-mermaid-prototype-pollution-vulnerability.md) |
| 1398305 | Cross-site Scripting (XSS) - Stored | high | $3000 | [Stored XSS on issue comments and other pages which contain notes](1398305-stored-xss-on-issue-comments-and-other-pages-which-contain-n.md) |
| 855276 | Server-Side Request Forgery (SSRF) | high | $3000 | [Injection of `http.<url>.*` git config settings leading to SSRF](855276-injection-of-http-url-git-config-settings-leading-to-ssrf.md) |
| 1103258 | Cross-site Scripting (XSS) - Stored | high | $3000 | [Stored DOM XSS via Mermaid chart](1103258-stored-dom-xss-via-mermaid-chart.md) |
| 856836 | Cross-site Scripting (XSS) - Stored | medium | $3000 | [Stored XSS on PyPi simple API endpoint](856836-stored-xss-on-pypi-simple-api-endpoint.md) |
| 819821 | Improper Access Control - Generic | medium | $3000 | [Initial mirror user can be assigned by other user even if the mirror was removed](819821-initial-mirror-user-can-be-assigned-by-other-user-even-if-th.md) |
| 647130 | Cross-site Scripting (XSS) - Stored | high | $2500 | [Stored XSS in "Create Groups"](647130-stored-xss-in-create-groups.md) |
| 1923672 | Cross-Site Request Forgery (CSRF) | medium | $2450 | [Account takeover due to insufficient URL validation on RelayState parameter](1923672-account-takeover-due-to-insufficient-url-validation-on-relay.md) |
| 2499070 | Uncontrolled Resource Consumption | medium | $2300 | [DOS: taking down a 1k users Gitlab EE instance or multiple Sidekiq instances by importing a malicious repo from a Github EE self-hosted server](2499070-dos-taking-down-a-1k-users-gitlab-ee-instance-or-multiple-si.md) |
| 1543584 | Uncontrolled Resource Consumption | medium | $2300 | [DOS via move_issue](1543584-dos-via-move-issue.md) |
| 298873 | Command Injection - Generic | critical | $2000 | [Command injection by overwriting authorized_keys file through GitLab import](298873-command-injection-by-overwriting-authorized-keys-file-throug.md) |
| 301432 | Path Traversal | critical | $2000 | [GitLab CI runner can read and poison cache of all other projects](301432-gitlab-ci-runner-can-read-and-poison-cache-of-all-other-proj.md) |
| 298176 | SQL Injection | critical | $2000 | [SQL injection in MilestoneFinder order method](298176-sql-injection-in-milestonefinder-order-method.md) |
| 790634 | Resource Injection | medium | $2000 | [When you call your branch the same name as a git hash, it could be checked out by dependents](790634-when-you-call-your-branch-the-same-name-as-a-git-hash-it-cou.md) |
| 446593 | Server-Side Request Forgery (SSRF) | medium | $2000 | [GitLab's GitHub integration is vulnerable to SSRF vulnerability](446593-gitlab-s-github-integration-is-vulnerable-to-ssrf-vulnerabil.md) |
| 1072868 | Cross-site Scripting (XSS) - Stored | medium | $2000 | [Stored XSS in repository file viewer](1072868-stored-xss-in-repository-file-viewer.md) |
| 859333 | Cross-site Scripting (XSS) - Stored | medium | $2000 | [Stored XSS in group issue list](859333-stored-xss-in-group-issue-list.md) |
| 1751258 | Insecure Direct Object Reference (IDOR) | medium | $1730 | [Attacker is able to create,Edit & delete notes and leak the title of a victim's private personal snippet](1751258-attacker-is-able-to-create-edit-delete-notes-and-leak-the-ti.md) |
| 1439552 | Improper Authorization | medium | $1680 | [Gitlab Pages token theft using service workers](1439552-gitlab-pages-token-theft-using-service-workers.md) |
| 497047 | Improper Access Control - Generic | medium | $1500 | [Blocked user Git access through CI/CD token](497047-blocked-user-git-access-through-ci-cd-token.md) |
| 962604 | Improper Access Control - Generic | medium | $1500 | [Revoked User can still view  the Merge Request  created by him via API](962604-revoked-user-can-still-view-the-merge-request-created-by-him.md) |
| 1086781 | Violation of Secure Design Principles | medium | $1370 | [Change project visibility to a restricted option](1086781-change-project-visibility-to-a-restricted-option.md) |
| 2528293 | Insecure Direct Object Reference (IDOR) | medium | $1160 | [IDOR Exposes All Machine Learning Models](2528293-idor-exposes-all-machine-learning-models.md) |
| 1892200 | Insecure Direct Object Reference (IDOR) | medium | $1160 | [Attacker can create malicious child epics linked to a victim's epic in an unrelated group](1892200-attacker-can-create-malicious-child-epics-linked-to-a-victim.md) |
| 1194254 | Cross-site Scripting (XSS) - Reflected | medium | $1130 | [XSS by clicking Jira's link](1194254-xss-by-clicking-jira-s-link.md) |
| 1935628 | Resource Injection | low | $1060 | [HTML injection possible with soft email confirmations when Administrator manually confirms attacker email address](1935628-html-injection-possible-with-soft-email-confirmations-when-a.md) |
| 557154 | Uncontrolled Resource Consumption | low | $1000 | [DoS attack via comment on Issue](557154-dos-attack-via-comment-on-issue.md) |
| 511381 | Uncontrolled Resource Consumption | low | $1000 | [All functions that allow users to specify color code are vulnerable to ReDoS](511381-all-functions-that-allow-users-to-specify-color-code-are-vul.md) |
| 462503 | Business Logic Errors | low | $1000 | [Claiming package names in GitLab's automatic package referencer.](462503-claiming-package-names-in-gitlab-s-automatic-package-referen.md) |
| 437142 | Open Redirect | low | $1000 | [Instant open redirect on Live preview WEB Ide opening](437142-instant-open-redirect-on-live-preview-web-ide-opening.md) |
| 312118 | Business Logic Errors | high | $750 | [Using GitLab to monitor and hijack domains in mass quantity.](312118-using-gitlab-to-monitor-and-hijack-domains-in-mass-quantity.md) |
| 299473 | Server-Side Request Forgery (SSRF) | high | $750 | [Evaluating Ruby code by injecting Rescue job on the system_hook_push queue through web hook](299473-evaluating-ruby-code-by-injecting-rescue-job-on-the-system-h.md) |
| 1353103 | Cross-Site Request Forgery (CSRF) | medium | $750 | [Drive-by arbitrary file deletion in the GDK via letter_opener_web gem](1353103-drive-by-arbitrary-file-deletion-in-the-gdk-via-letter-opene.md) |
| 301137 | Improper Access Control - Generic | high | $750 | [GitHub import allows user to create child group under existing namespace](301137-github-import-allows-user-to-create-child-group-under-existi.md) |
| 1113289 | Privilege Escalation | medium | $650 | [Guest users can create new test cases](1113289-guest-users-can-create-new-test-cases.md) |
| 1117768 | Improper Access Control - Generic | low | $610 | [Guest Users can create issues for Sentry errors and track their status](1117768-guest-users-can-create-issues-for-sentry-errors-and-track-th.md) |
| 1112297 | Privilege Escalation | medium | $600 | [Reporters can upload design to issues using the "Move to" feature](1112297-reporters-can-upload-design-to-issues-using-the-move-to-feat.md) |
| 1283484 | Uncontrolled Resource Consumption | medium | $600 | [ReDoS in syntax highlighting due to Rouge](1283484-redos-in-syntax-highlighting-due-to-rouge.md) |
| 446238 | Information Disclosure | low | $500 | [EXIF metadata not stripped from JPG group logos](446238-exif-metadata-not-stripped-from-jpg-group-logos.md) |
| 703894 | Insecure Direct Object Reference (IDOR) | low | $500 | [View the Starred Projects in a Private Profile](703894-view-the-starred-projects-in-a-private-profile.md) |
| 348443 | Information Disclosure | low | $300 | [Snippet JS template allows attacker to read a user's private snippets](348443-snippet-js-template-allows-attacker-to-read-a-user-s-private.md) |
| 475098 | Violation of Secure Design Principles | low | $200 | [A profile page of a user can be denied from loading by appending .html to the username](475098-a-profile-page-of-a-user-can-be-denied-from-loading-by-appen.md) |
| 716677 | Privilege Escalation | low | $200 | [Domain Takeover - gl-canary.freetls.fastly.net](716677-domain-takeover-gl-canary-freetls-fastly-net.md) |
| 762271 | Improper Access Control - Generic | low | $100 | [Guest users can change the confidentiality attribute on those issues that have been assigned to them](762271-guest-users-can-change-the-confidentiality-attribute-on-thos.md) |
| 1417211 | Privilege Escalation | n/a | $100 | [Installing Gitlab runner with Docker-In-Docker allows root access](1417211-installing-gitlab-runner-with-docker-in-docker-allows-root-a.md) |
| 526325 | Cross-site Scripting (XSS) - Stored | high | $0 | [Stored XSS in Wiki pages](526325-stored-xss-in-wiki-pages.md) |
| 409395 | Improper Input Validation | critical | $0 | [Bypass of GitLab CI runner slash fix in YAML validation](409395-bypass-of-gitlab-ci-runner-slash-fix-in-yaml-validation.md) |
| 502593 | Improper Access Control - Generic | high | $0 | [Attacker is able to access commit title and team member comments which are supposed to be private](502593-attacker-is-able-to-access-commit-title-and-team-member-comm.md) |
| 632101 | Server-Side Request Forgery (SSRF) | high | $0 | [Server Side Request Forgery mitigation bypass](632101-server-side-request-forgery-mitigation-bypass.md) |
| 498964 | Incorrect Authorization | critical | $0 | [Full access to internal Gitlab instances at redash.gitlab.com, dashboards.gitlab.com, prometheus.gitlab.com](498964-full-access-to-internal-gitlab-instances-at-redash-gitlab-co.md) |
| 1672388 | OS Command Injection | critical | $0 | [RCE via github import](1672388-rce-via-github-import.md) |
| 493324 | Privilege Escalation | critical | $0 | [Privilege escalation from any user (including external) to gitlab admin when admin impersonates you](493324-privilege-escalation-from-any-user-including-external-to-git.md) |
| 565883 | Reliance on Untrusted Inputs in a Security Decision | medium | $0 | [Bypass Email Verification -- Able to Access Internal Gitlab Services that use Login with Gitlab and Perform Check on email domain](565883-bypass-email-verification-able-to-access-internal-gitlab-ser.md) |
| 878779 | Server-Side Request Forgery (SSRF) | critical | $0 | [Full Read SSRF on Gitlab's Internal Grafana](878779-full-read-ssrf-on-gitlab-s-internal-grafana.md) |
| 928255 | Misconfiguration | high | $0 | [Ability To Delete User(s) Account Without User Interaction](928255-ability-to-delete-user-s-account-without-user-interaction.md) |
| 692252 | Improper Access Control - Generic | high | $0 | [Group search leaks private MRs, code, commits](692252-group-search-leaks-private-mrs-code-commits.md) |
| 1665658 | Cross-site Scripting (XSS) - Stored | high | $0 | [Stored-XSS with CSP-bypass via labels' color](1665658-stored-xss-with-csp-bypass-via-labels-color.md) |
| 1481207 | Cross-site Scripting (XSS) - Stored | high | $0 | [Stored XSS in Notes (with CSP bypass for gitlab.com)](1481207-stored-xss-in-notes-with-csp-bypass-for-gitlab-com.md) |
| 534794 | Insecure Direct Object Reference (IDOR) | high | $0 | [Importing GitLab project archives can replace uploads of other users](534794-importing-gitlab-project-archives-can-replace-uploads-of-oth.md) |
| 824689 | Command Injection - Generic | medium | $0 | [Send arbitrary PUT requests when user clicks on a link](824689-send-arbitrary-put-requests-when-user-clicks-on-a-link.md) |
| 178152 | Information Disclosure | critical | $0 | [Read files on application server, leads to RCE](178152-read-files-on-application-server-leads-to-rce.md) |
| 979787 | Insecure Storage of Sensitive Information | critical | $0 | [Able to view hackerone reports attachments](979787-able-to-view-hackerone-reports-attachments.md) |
| 1588732 | Cross-site Scripting (XSS) - Generic | high | $0 | [CSP-bypass XSS in project settings page](1588732-csp-bypass-xss-in-project-settings-page.md) |
| 708820 | Improper Access Control - Generic | high | $0 | [Group search with Elastic search enable leaks unrelated data](708820-group-search-with-elastic-search-enable-leaks-unrelated-data.md) |
| 1693150 | Cross-site Scripting (XSS) - Stored | high | $0 | [Bypass: Stored-XSS with CSP-bypass via scoped labels' color](1693150-bypass-stored-xss-with-csp-bypass-via-scoped-labels-color.md) |
| 880099 | Cross-site Scripting (XSS) - Stored | medium | $0 | [Unrestricted file upload leads to Stored XSS](880099-unrestricted-file-upload-leads-to-stored-xss.md) |
| 1160407 | Uncontrolled Resource Consumption | high | $0 | [Cache poisoning Denial of Service affecting assets.gitlab-static.net](1160407-cache-poisoning-denial-of-service-affecting-assets-gitlab-st.md) |
| 1542510 | Cross-site Scripting (XSS) - Generic | high | $0 | [XSS in ZenTao integration affecting self hosted instances without strict CSP](1542510-xss-in-zentao-integration-affecting-self-hosted-instances-wi.md) |
| 1256777 | Cross-site Scripting (XSS) - Stored | high | $0 | [Stored XSS in main page of a project caused by arbitrary script payload in group "Default initial branch name"](1256777-stored-xss-in-main-page-of-a-project-caused-by-arbitrary-scr.md) |
| 2523654 | Misconfiguration | low | $0 | [Subdomain takeover in Gitlab pages](2523654-subdomain-takeover-in-gitlab-pages.md) |
| 955016 | OS Command Injection | high | $0 | [GitLab-Runner on Windows `DOCKER_AUTH_CONFIG` container host Command Injection](955016-gitlab-runner-on-windows-docker-auth-config-container-host-c.md) |
| 2599840 | Misconfiguration | low | $0 | [Remove obsolete domain from handbook subdomain](2599840-remove-obsolete-domain-from-handbook-subdomain.md) |
| 541169 | Server-Side Request Forgery (SSRF) | high | $0 | [GitLab::UrlBlocker validation bypass leading to full Server Side Request Forgery](541169-gitlab-urlblocker-validation-bypass-leading-to-full-server-s.md) |
| 369451 | Server-Side Request Forgery (SSRF) | medium | $0 | [SSRF in CI after first run](369451-ssrf-in-ci-after-first-run.md) |
| 2257080 | Cross-site Scripting (XSS) - Stored | high | $0 | [Stored-XSS injected in Wiki page via Banzai pipeline](2257080-stored-xss-injected-in-wiki-page-via-banzai-pipeline.md) |
| 2676025 | Missing Critical Step in Authentication | none | $0 | [Login email verification bypass via `/oauth/token`.](2676025-login-email-verification-bypass-via-oauth-token.md) |
| 1193062 | Privilege Escalation | medium | $0 | [Privilege escalation of "external user" (with maintainer privilege) to internal access  through project token](1193062-privilege-escalation-of-external-user-with-maintainer-privil.md) |
| 614355 | Improper Access Control - Generic | medium | $0 | [GraphQL query "namespace" leaks data](614355-graphql-query-namespace-leaks-data.md) |
| 158330 | Privilege Escalation | critical | $0 | [Ability to access all user authentication tokens, leads to RCE](158330-ability-to-access-all-user-authentication-tokens-leads-to-rc.md) |
| 415238 | Cross-Site Request Forgery (CSRF) | low | $0 | [[Admin Panel] CSRF to resume/pause runner](415238-admin-panel-csrf-to-resume-pause-runner.md) |
| 1087061 | Cross-site Scripting (XSS) - Stored | medium | $0 | [Stored-XSS on wiki pages](1087061-stored-xss-on-wiki-pages.md) |
| 1092230 | Server-Side Request Forgery (SSRF) | high | $0 | [FogBugz import attachment full SSRF requiring vulnerability in *.fogbugz.com](1092230-fogbugz-import-attachment-full-ssrf-requiring-vulnerability.md) |
| 495497 | Information Disclosure | low | $0 | [Know whether private project name exists or not within a group using link comments](495497-know-whether-private-project-name-exists-or-not-within-a-gro.md) |
| 1533976 | Resource Injection | high | $0 | [Content injection in Jira issue title enabling sending arbitrary POST request as victim](1533976-content-injection-in-jira-issue-title-enabling-sending-arbit.md) |
| 617896 | Violation of Secure Design Principles | high | $0 | [Bypass Email Verification using Salesforce -- Reproducible in gitlab.com](617896-bypass-email-verification-using-salesforce-reproducible-in-g.md) |
| 1409788 | Resource Injection | high | $0 | [Arbitrary POST request as victim user from HTML injection in Jupyter notebooks](1409788-arbitrary-post-request-as-victim-user-from-html-injection-in.md) |
| 218230 | Improper Authentication - Generic | critical | $0 | [Access to GitLab's Slack by abusing issue creation from e-mail](218230-access-to-gitlab-s-slack-by-abusing-issue-creation-from-e-ma.md) |
| 549040 | Uncontrolled Resource Consumption | low | $0 | [Clientside resource Exhausting by exploiting gitlab math rendering ](549040-clientside-resource-exhausting-by-exploiting-gitlab-math-ren.md) |
| 1285226 | Improper Access Control - Generic | medium | $0 | [Improper access control for users with expired password, giving the user full access through API and Git](1285226-improper-access-control-for-users-with-expired-password-givi.md) |
| 831962 | Cross-site Scripting (XSS) - DOM | medium | $0 | [XSS on Issue reference numbers](831962-xss-on-issue-reference-numbers.md) |
| 1192460 | Improper Access Control - Generic | medium | $0 | [A deactivated user can access data through GraphQL](1192460-a-deactivated-user-can-access-data-through-graphql.md) |
| 1579645 | Cross-site Scripting (XSS) - Generic | high | $0 | [XSS: `v-safe-html` is not safe enough](1579645-xss-v-safe-html-is-not-safe-enough.md) |
| 460815 | Improper Access Control - Generic | low | $0 | [Milestones leaked via search API](460815-milestones-leaked-via-search-api.md) |
| 1212822 | Cross-site Scripting (XSS) - DOM | high | $0 | [Stored XSS in Mermaid when viewing Markdown files](1212822-stored-xss-in-mermaid-when-viewing-markdown-files.md) |
| 2668302 | Improper Authorization | none | $0 | [Removed Guest role user who dosent have access to private project in members able to view jobs ](2668302-removed-guest-role-user-who-dosent-have-access-to-private-pr.md) |
| 806571 | Cross-site Scripting (XSS) - Stored | medium | $0 | [Stored XSS in blob viewer](806571-stored-xss-in-blob-viewer.md) |
| 526570 | Improper Access Control - Generic | medium | $0 | [Bypassing push rules via MRs created by Email](526570-bypassing-push-rules-via-mrs-created-by-email.md) |
| 1372216 | Insecure Direct Object Reference (IDOR) | medium | $0 | [IDOR in "external status check" API leaks data about any status check on the instance](1372216-idor-in-external-status-check-api-leaks-data-about-any-statu.md) |
| 1196958 | Cross-site Scripting (XSS) - DOM | medium | $0 | [Clipboard DOM-based XSS](1196958-clipboard-dom-based-xss.md) |
| 950190 | Cross-site Scripting (XSS) - Stored | high | $0 | [Store-XSS in error message of build-dependencies ](950190-store-xss-in-error-message-of-build-dependencies.md) |
| 977697 | Cross-site Scripting (XSS) - Stored | high | $0 | [Stored-XSS in merge requests](977697-stored-xss-in-merge-requests.md) |
| 149598 | Violation of Secure Design Principles | n/a | $0 | [Insecure 2FA/authentication implementation creates a brute force vulnerability](149598-insecure-2fa-authentication-implementation-creates-a-brute-f.md) |
| 2104591 | Information Disclosure | medium | $0 | [Maintainer can leak sentry token by changing the configured URL (fix bypass)](2104591-maintainer-can-leak-sentry-token-by-changing-the-configured.md) |
| 1342009 | Cross-site Scripting (XSS) - Stored | high | $0 | [Stored XSS in merge request creation page through payload in approval rule name](1342009-stored-xss-in-merge-request-creation-page-through-payload-in.md) |
| 578119 | Privilege Escalation | low | $0 | [Privilege escalation due to insecure use of logrotate](578119-privilege-escalation-due-to-insecure-use-of-logrotate.md) |
| 378148 | Command Injection - Generic | critical | $0 | [Vulnerability in project import leads to arbitrary command execution](378148-vulnerability-in-project-import-leads-to-arbitrary-command-e.md) |
| 1043480 | Improper Authentication - Generic | medium | $0 | [Remote hacker can download all the files of master branch in public projects where everything is members only.](1043480-remote-hacker-can-download-all-the-files-of-master-branch-in.md) |
| 670572 | Uncontrolled Resource Consumption | medium | $0 | [Uncontrolled Resource Consumption in any Markdown field using Mermaid](670572-uncontrolled-resource-consumption-in-any-markdown-field-usin.md) |
| 174983 | Privilege Escalation | n/a | $0 | [Mailgun misconfiguration leads to email snooping and postmaster@-access on email.mg.gitlab.com](174983-mailgun-misconfiguration-leads-to-email-snooping-and-postmas.md) |
| 972355 | Information Disclosure | medium | $0 | [Able to leak private email of any user given his/her username via graphql](972355-able-to-leak-private-email-of-any-user-given-his-her-usernam.md) |
| 540711 | Improper Access Control - Generic | low | $0 | [Access Projects And create projects in gitlab pre production server](540711-access-projects-and-create-projects-in-gitlab-pre-production.md) |
| 2097377 | Information Disclosure | low | $0 | [Information Disclosure - Pvt Gitlab Issue Disclosing Through GitLab Unfiltered YouTube channel.](2097377-information-disclosure-pvt-gitlab-issue-disclosing-through-g.md) |
| 439729 | Insecure Direct Object Reference (IDOR) | low | $0 | [Add and Access to Labels of any Private Projects/Groups of Gitlab(IDOR)](439729-add-and-access-to-labels-of-any-private-projects-groups-of-g.md) |
| 128085 | Improper Authentication - Generic | n/a | $0 | [Bypassing password authentication of users that have 2FA enabled](128085-bypassing-password-authentication-of-users-that-have-2fa-ena.md) |
| 702987 | Uncontrolled Resource Consumption | low | $0 | [No redirect_uri in the db for web-internal clientKey leads to one-click DoS on gitter.im](702987-no-redirect-uri-in-the-db-for-web-internal-clientkey-leads-t.md) |
| 674195 | Insecure Direct Object Reference (IDOR) | high | $0 | [Stealing data from customers.gitlab.com without user interaction](674195-stealing-data-from-customers-gitlab-com-without-user-interac.md) |
| 853355 | Information Disclosure | medium | $0 | [Unauthorized access to private project security dashboard](853355-unauthorized-access-to-private-project-security-dashboard.md) |
| 477222 | Information Disclosure | low | $0 | [Last build status and coverage leaked to unauthorized users](477222-last-build-status-and-coverage-leaked-to-unauthorized-users.md) |
| 496973 | Cross-site Scripting (XSS) - Generic | low | $0 | [Persistent XSS via e-mail when creating merge requests](496973-persistent-xss-via-e-mail-when-creating-merge-requests.md) |
| 407763 | Information Disclosure | medium | $0 | [Unauthorized users may be able to view almost all informations related to Private projects.](407763-unauthorized-users-may-be-able-to-view-almost-all-informatio.md) |
| 1772063 | Uncontrolled Resource Consumption | medium | $0 | [ReDoS due to device-detector parsing user agents](1772063-redos-due-to-device-detector-parsing-user-agents.md) |
| 882848 | Business Logic Errors | low | $0 | [Possibilty to purchase Ultimate - 1 Year (EDU or OSS)](882848-possibilty-to-purchase-ultimate-1-year-edu-or-oss.md) |
| 441090 | Server-Side Request Forgery (SSRF) | high | $0 | [CRLF injection & SSRF in git:// protocal lead to arbitrary code execution](441090-crlf-injection-ssrf-in-git-protocal-lead-to-arbitrary-code-e.md) |
| 214028 | Information Disclosure | low | $0 | [Race condition in GitLab import, giving access to other people their imports due to filename collision](214028-race-condition-in-gitlab-import-giving-access-to-other-peopl.md) |
| 684268 | Cross-site Scripting (XSS) - Stored | high | $0 | [Stored XSS for Grafana dashboard URL](684268-stored-xss-for-grafana-dashboard-url.md) |
| 265696 | Violation of Secure Design Principles | low | $0 | [Gitlab is vulnerable to impersonation attacks due to broken links](265696-gitlab-is-vulnerable-to-impersonation-attacks-due-to-broken.md) |
| 215105 | Server-Side Request Forgery (SSRF) | medium | $0 | [SSRF vulnerability in gitlab.com via project import.](215105-ssrf-vulnerability-in-gitlab-com-via-project-import.md) |
| 270999 | Cross-site Scripting (XSS) - Stored | medium | $0 | [[Markdown] Stored XSS via character encoding parser bypass](270999-markdown-stored-xss-via-character-encoding-parser-bypass.md) |
| 268794 | Privilege Escalation | critical | $0 | [all private tokens are leaked to an unauthenticated attacker](268794-all-private-tokens-are-leaked-to-an-unauthenticated-attacker.md) |
| 216243 | Command Injection - Generic | medium | $0 | [CSV injection in gitlab.com via issues export feature.](216243-csv-injection-in-gitlab-com-via-issues-export-feature.md) |
| 358001 | Cross-site Scripting (XSS) - Stored | low | $0 | [HTML TAG INJECTION ON PROFILE NAME](358001-html-tag-injection-on-profile-name.md) |
| 1669176 | Improper Access Control - Generic | medium | $0 | [Unauthorized access](1669176-unauthorized-access.md) |
| 409380 | Cross-site Scripting (XSS) - Stored | high | $0 | [Stored XSS in merge request pages](409380-stored-xss-in-merge-request-pages.md) |
| 1591412 | Improper Access Control - Generic | medium | $0 | [Unauthenticated IP allowlist bypass when accessing job artifacts through gitlab pages at `{group_id}.gitlab.io`](1591412-unauthenticated-ip-allowlist-bypass-when-accessing-job-artif.md) |
| 633001 | Information Disclosure | low | $0 | [Private System Note Disclosure using GraphQL](633001-private-system-note-disclosure-using-graphql.md) |
| 218872 | Cross-site Scripting (XSS) - Stored | high | $0 | [Stored XSS on Files overview by abusing git submodule URL](218872-stored-xss-on-files-overview-by-abusing-git-submodule-url.md) |
| 131210 | Privilege Escalation | n/a | $0 | [Privilege escalation to access all private groups and repositories](131210-privilege-escalation-to-access-all-private-groups-and-reposi.md) |
| 384255 | Cross-site Scripting (XSS) - Stored | high | $0 | [Stored XSS on Issue details page](384255-stored-xss-on-issue-details-page.md) |
| 970869 | Command Injection - Generic | medium | $0 | [Sending Arbitrary Requests through Jupyter Notebooks on gitlab.com and Self-Hosted GitLab Instances](970869-sending-arbitrary-requests-through-jupyter-notebooks-on-gitl.md) |
| 709951 | Server-Side Request Forgery (SSRF) | medium | $0 | [Blind SSRF in FogBugz project import](709951-blind-ssrf-in-fogbugz-project-import.md) |
| 605608 | Information Disclosure | low | $0 | [[information disclosure] Validate existence of a private project.](605608-information-disclosure-validate-existence-of-a-private-proje.md) |
| 689245 | Server-Side Request Forgery (SSRF) | medium | $0 | [SSRF In plantuml (on plantuml.pre.gitlab.com)](689245-ssrf-in-plantuml-on-plantuml-pre-gitlab-com.md) |
| 310185 | Improper Access Control - Generic | medium | $0 | [Removing a user from a private group doesn't remove him from group's project, if his project's role was changed](310185-removing-a-user-from-a-private-group-doesn-t-remove-him-from.md) |
| 136333 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [Persistent XSS on public wiki pages](136333-persistent-xss-on-public-wiki-pages.md) |
| 1375393 | Improper Access Control - Generic | medium | $0 | ["External status checks" can be accepted by users below developer access if the user is either author or assignee of the target merge request](1375393-external-status-checks-can-be-accepted-by-users-below-develo.md) |
| 748375 | Improper Access Control - Generic | medium | $0 | [Transferring a public group to a private group doesn't remove code from the Elastichsearch API search result](748375-transferring-a-public-group-to-a-private-group-doesn-t-remov.md) |
| 493791 | Improper Authentication - Generic | none | $0 | [Inadequate cache control in gitter allows to view private chat room](493791-inadequate-cache-control-in-gitter-allows-to-view-private-ch.md) |
| 195134 | Privilege Escalation | medium | $0 | [User with guest access can access private merge requests](195134-user-with-guest-access-can-access-private-merge-requests.md) |
| 1442118 | Improper Access Control - Generic | high | $0 | [Container escape on public GitLab CI runners](1442118-container-escape-on-public-gitlab-ci-runners.md) |
| 985124 | Privacy Violation | medium | $0 | [GraphQL Query leads to sensitive information disclosure](985124-graphql-query-leads-to-sensitive-information-disclosure.md) |
| 809248 | Server-Side Request Forgery (SSRF) | medium | $0 | [SSRF into Shared Runner, by replacing dockerd with malicious server in Executor](809248-ssrf-into-shared-runner-by-replacing-dockerd-with-malicious.md) |
| 135937 | Information Disclosure | n/a | $0 | [SSRF when importing a project from a git repo by URL](135937-ssrf-when-importing-a-project-from-a-git-repo-by-url.md) |
| 266908 | Violation of Secure Design Principles | low | $0 | [Impersonation attack via Broken Link in Resellers Page](266908-impersonation-attack-via-broken-link-in-resellers-page.md) |
| 195088 | Privilege Escalation | medium | $0 | [Every user can delete public deploy keys](195088-every-user-can-delete-public-deploy-keys.md) |
| 667408 | Improper Access Control - Generic | low | $0 | [Head pipeline leaked to unauthorized users via blocking merge request feature](667408-head-pipeline-leaked-to-unauthorized-users-via-blocking-merg.md) |
| 346217 | Cross-site Scripting (XSS) - Stored | medium | $0 | [Persistent XSS - Selecting users as allowed merge request approvers](346217-persistent-xss-selecting-users-as-allowed-merge-request-appr.md) |
| 216453 | Cross-site Scripting (XSS) - DOM | medium | $0 | [Unfiltered `class` attribute in markdown code](216453-unfiltered-class-attribute-in-markdown-code.md) |
| 215384 | Insecure Direct Object Reference (IDOR) | medium | $0 | [[Subgroups] Unprivileged User Can Disclose Private Group Names](215384-subgroups-unprivileged-user-can-disclose-private-group-names.md) |
| 186194 | Privilege Escalation | high | $0 | [State filter in IssuableFinder allows attacker to delete all issues and merge requests](186194-state-filter-in-issuablefinder-allows-attacker-to-delete-all.md) |
| 159984 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [XSS On meta tags in profile page](159984-xss-on-meta-tags-in-profile-page.md) |
| 582349 | Improper Authentication - Generic | low | $0 | [Last pipeline status for MR leaked ](582349-last-pipeline-status-for-mr-leaked.md) |
| 301924 | Server-Side Request Forgery (SSRF) | medium | $0 | [SSRF vulnerability in gitlab.com webhook](301924-ssrf-vulnerability-in-gitlab-com-webhook.md) |
| 195058 | Information Disclosure | medium | $0 | [Users can download old project exports due to unclaimed namespace](195058-users-can-download-old-project-exports-due-to-unclaimed-name.md) |
| 162147 | Information Disclosure | n/a | $0 | [Boards leak private label names and desciptions](162147-boards-leak-private-label-names-and-desciptions.md) |
| 128051 | Information Disclosure | n/a | $0 | [Attacker can extract list of private project's project members](128051-attacker-can-extract-list-of-private-project-s-project-membe.md) |
| 1531958 | Uncontrolled Resource Consumption | medium | $0 | [ReDoS in net/http affects webhooks: Sidekiq job stuck at 100% CPU for a year](1531958-redos-in-net-http-affects-webhooks-sidekiq-job-stuck-at-100.md) |
| 962462 | Information Disclosure | high | $0 | [Unauthorized user is able to access schedule pipeline variables and values](962462-unauthorized-user-is-able-to-access-schedule-pipeline-variab.md) |
| 676976 | Improper Access Control - Generic | medium | $0 | [Container scanning and Dependency scanning report leaked to unauthorized users](676976-container-scanning-and-dependency-scanning-report-leaked-to.md) |
| 118024 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [Markdown based stored XSS (IE only)](118024-markdown-based-stored-xss-ie-only.md) |
| 195140 | Privilege Escalation | medium | $0 | [Users with guest access can post notes to private merge requests, issues, and snippets](195140-users-with-guest-access-can-post-notes-to-private-merge-requ.md) |
| 1643962 | Information Disclosure | low | $0 | [Path paths and file disclosure vulnerabilities at influxdb.quality.gitlab.net](1643962-path-paths-and-file-disclosure-vulnerabilities-at-influxdb-q.md) |
| 710006 | Improper Access Control - Generic | medium | $0 | [Elasticsearch leaks data through the notes scope](710006-elasticsearch-leaks-data-through-the-notes-scope.md) |
| 978768 | Insecure Direct Object Reference (IDOR) | high | $0 | [Adding everyone to the repo due to the lack of rate limit](978768-adding-everyone-to-the-repo-due-to-the-lack-of-rate-limit.md) |
| 346111 | Cross-site Scripting (XSS) - Stored | high | $0 | [XSS (Persistent) - Selecting role(s) for protected branches](346111-xss-persistent-selecting-role-s-for-protected-branches.md) |
| 212629 | UI Redressing (Clickjacking) | medium | $0 | [Gitlab.com is vulnerable to reverse tabnabbing. (#2)](212629-gitlab-com-is-vulnerable-to-reverse-tabnabbing-2.md) |
| 211065 | Open Redirect | low | $0 | [Gitlab.com is vulnerable to reverse tabnabbing.](211065-gitlab-com-is-vulnerable-to-reverse-tabnabbing.md) |
| 200693 | Cross-site Scripting (XSS) - Generic | medium | $0 | [[RDoc] XSS in project README files](200693-rdoc-xss-in-project-readme-files.md) |
| 129736 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [Persistent XSS on public project page](129736-persistent-xss-on-public-project-page.md) |
| 1582160 | Open Redirect | medium | $0 | [Bypass for Domain-level redirects (Unvalidated Redirects and Forwar)](1582160-bypass-for-domain-level-redirects-unvalidated-redirects-and.md) |
| 1089914 | Privacy Violation | high | $0 | [Responsible Disclosure of Privacy Leakage Issue](1089914-responsible-disclosure-of-privacy-leakage-issue.md) |
| 880863 | Information Disclosure | medium | $0 | [Todos are not redacted when membership changes - Access to (confidential) issues and merge requests](880863-todos-are-not-redacted-when-membership-changes-access-to-con.md) |
| 351554 | Cross-site Scripting (XSS) - Stored | medium | $0 | [Persistent XSS - Deleting a project (No Longer Vulnerable in 10.7)](351554-persistent-xss-deleting-a-project-no-longer-vulnerable-in-10.md) |
| 359288 | Server-Side Request Forgery (SSRF) | medium | $0 | [Potensial SSRF via Git repository URL ](359288-potensial-ssrf-via-git-repository-url.md) |
| 182487 | Cross-Site Request Forgery (CSRF) | low | $0 | [CSRF Token Bypass in Account Deletion](182487-csrf-token-bypass-in-account-deletion.md) |
| 205497 | Cross-site Scripting (XSS) - Generic | medium | $0 | [[reStructuredText] XSS in project README files](205497-restructuredtext-xss-in-project-readme-files.md) |
| 132777 | Information Disclosure | n/a | $0 | [Labels created in private projects are leaked](132777-labels-created-in-private-projects-are-leaked.md) |
| 134305 | Information Disclosure | n/a | $0 | [Private snippets in public / internal projects leaked though GitLab API](134305-private-snippets-in-public-internal-projects-leaked-though-g.md) |
| 1681275 | Misconfiguration | n/a | $0 | [Dependecy Confusion via Lookup Request Forwarding to PyPi.org](1681275-dependecy-confusion-via-lookup-request-forwarding-to-pypi-or.md) |
| 1637577 | Improper Access Control - Generic | medium | $0 | [Found Origin IP's lead to access to gitlab](1637577-found-origin-ip-s-lead-to-access-to-gitlab.md) |
| 1261148 | Cross-site Scripting (XSS) - Reflected | none | $0 | [Stored-XSS in merge requests](1261148-stored-xss-in-merge-requests.md) |
| 729341 | Cross-site Scripting (XSS) - DOM | low | $0 | [Double linking cause XSS (but blokeced by CSP in gitlab.com)](729341-double-linking-cause-xss-but-blokeced-by-csp-in-gitlab-com.md) |
| 221041 | Uncontrolled Resource Consumption | medium | $0 | [Cookie bomb](221041-cookie-bomb.md) |
| 221432 | Cross-Site Request Forgery (CSRF) | medium | $0 | [CSRF-Token leak by request forgery](221432-csrf-token-leak-by-request-forgery.md) |
| 133717 | Information Disclosure | n/a | $0 | [GFM renderer leaks external issue tracker URL of private project](133717-gfm-renderer-leaks-external-issue-tracker-url-of-private-pro.md) |
| 134292 | Privilege Escalation | n/a | $0 | [Attacker can delete (and read) private project webhooks](134292-attacker-can-delete-and-read-private-project-webhooks.md) |
| 134299 | Privilege Escalation | n/a | $0 | [Attacker can post notes on private MR, snippets, and issues](134299-attacker-can-post-notes-on-private-mr-snippets-and-issues.md) |
| 1916285 | Command Injection - Generic | low | $0 | [Arbitrary escape sequence injection in docker-machine from worker nodes](1916285-arbitrary-escape-sequence-injection-in-docker-machine-from-w.md) |
| 790786 | Improper Access Control - Generic | high | $0 | [Members from parent group keep their access level on a subgroup transfer and are invisible](790786-members-from-parent-group-keep-their-access-level-on-a-subgr.md) |
| 636560 | Information Disclosure | low | $0 | [Project Milestones Disclosed Via Groups When the Victim disabled milestones access in project settings](636560-project-milestones-disclosed-via-groups-when-the-victim-disa.md) |
| 491319 | Information Disclosure | none | $0 | [Guests Will Disclose the Private Project Full Activity Via Project Activity Feeds](491319-guests-will-disclose-the-private-project-full-activity-via-p.md) |
| 213114 | UI Redressing (Clickjacking) | medium | $0 | [Gitlab.com is vulnerable to reverse tabnabbing via AsciiDoc links. (#3)](213114-gitlab-com-is-vulnerable-to-reverse-tabnabbing-via-asciidoc.md) |
| 205498 | Cross-site Scripting (XSS) - Generic | medium | $0 | [[Textile] XSS in project README files](205498-textile-xss-in-project-readme-files.md) |
| 134300 | Information Disclosure | n/a | $0 | [Confidential issues leaked in public projects when attached to milestone](134300-confidential-issues-leaked-in-public-projects-when-attached.md) |
| 214034 | Open Redirect | medium | $0 | [Open redirect](214034-open-redirect.md) |
| 215970 | Open Redirect | medium | $0 | [[Repository Import] Open Redirect via "continue[to]" parameter ](215970-repository-import-open-redirect-via-continue-to-parameter.md) |
| 801973 | Violation of Secure Design Principles | none | $0 | [Email notification about login email changed is not received when using verified linked email address](801973-email-notification-about-login-email-changed-is-not-received.md) |
| 191216 | Server-Side Request Forgery (SSRF) | medium | $0 | [SSRF via git Repo by URL Abuse](191216-ssrf-via-git-repo-by-url-abuse.md) |
| 1696814 | No Restriction on password | none | $0 | [No Restriction on password](1696814-no-restriction-on-password.md) |
| 874401 | Information Disclosure | medium | $0 | [Use of Ruby Forwardable module and runtime meta-programming may introduce vulnerabilities](874401-use-of-ruby-forwardable-module-and-runtime-meta-programming.md) |
| 296907 | Phishing | medium | $0 | [Lack of validation before assigning custom domain names leading to abuse of GitLab pages service](296907-lack-of-validation-before-assigning-custom-domain-names-lead.md) |
| 224198 | Violation of Secure Design Principles | low | $0 | [Missing/Breach of Internal Security Boundary - Access to Job Queue Results in Remote Code Execution](224198-missing-breach-of-internal-security-boundary-access-to-job-q.md) |
