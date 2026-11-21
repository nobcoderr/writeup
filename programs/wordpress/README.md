# WordPress

Disclosed reports: **100**

| ID | Temuan | Severity | Bounty | Writeup |
| --- | --- | --- | ---: | --- |
| 643908 | Cross-site Scripting (XSS) - Stored | high | $0 | [Stored XSS Vulnerability](643908-stored-xss-vulnerability.md) |
| 487081 | Cross-site Scripting (XSS) - Stored | critical | $0 | [Stored XSS in Private Message component (BuddyPress)](487081-stored-xss-in-private-message-component-buddypress.md) |
| 436928 | Path Traversal | critical | $0 | [RCE as Admin defeats WordPress hardening and file permissions](436928-rce-as-admin-defeats-wordpress-hardening-and-file-permission.md) |
| 592316 | Cross-site Scripting (XSS) - Stored | low | $0 | [Stored XSS on byddypress Plug-in via groups name](592316-stored-xss-on-byddypress-plug-in-via-groups-name.md) |
| 205481 | Violation of Secure Design Principles | medium | $0 | [Wordpress unzip_file path traversal](205481-wordpress-unzip-file-path-traversal.md) |
| 659419 | Cross-site Scripting (XSS) - Reflected | high | $0 | [Reflected XSS on https://make.wordpress.org via 'channel' parameter](659419-reflected-xss-on-https-make-wordpress-org-via-channel-parame.md) |
| 428019 | Cross-Site Request Forgery (CSRF) | high | $0 | [CSRF to HTML Injection in Comments](428019-csrf-to-html-injection-in-comments.md) |
| 1107282 | Privilege Escalation | high | $0 | [Privilege Escalation via REST API to Administrator leads to RCE](1107282-privilege-escalation-via-rest-api-to-administrator-leads-to.md) |
| 921709 | UI Redressing (Clickjacking) | low | $0 | [Clickjacking on donation page](921709-clickjacking-on-donation-page.md) |
| 509930 | Cross-site Scripting (XSS) - Stored | high | $0 | [Potential unprivileged Stored XSS through wp_targeted_link_rel](509930-potential-unprivileged-stored-xss-through-wp-targeted-link-r.md) |
| 2786591 | Uncontrolled Resource Consumption | high | $0 | [Unauthenticated WordPress Database Repair DoS](2786591-unauthenticated-wordpress-database-repair-dos.md) |
| 490782 | Improper Access Control - Generic | low | $0 | [Mssing Authorization on Private Message replies (BuddyPress)](490782-mssing-authorization-on-private-message-replies-buddypress.md) |
| 2999394 | Privilege Escalation | medium | $0 | [Pivilege escalation of any new user to Keymaster caused by CSRF](2999394-pivilege-escalation-of-any-new-user-to-keymaster-caused-by-c.md) |
| 222692 | Violation of Secure Design Principles | n/a | $0 | [plugins.trac.wordpress.org likely vulnerable to Cross Site Tracing (xst), TRACE HTTP method should be disabled](222692-plugins-trac-wordpress-org-likely-vulnerable-to-cross-site-t.md) |
| 3893632 | Improper Access Control - Generic | medium | $0 | [Unauthenticated disclosure of draft/private/pending post titles & IDs via Secure Custom Fields nopriv AJAX field-query handlers (post_object/relations](3893632-unauthenticated-disclosure-of-draft-private-pending-post-tit.md) |
| 1238528 | Cross-site Scripting (XSS) - DOM | medium | $0 | [wp-embed XSS on Safari](1238528-wp-embed-xss-on-safari.md) |
| 3931777 | Path Traversal | critical | $0 | [Author → arbitrary file deletion anywhere on disk (site takeover) via `POST /wp/v2/media/<id>/finalize` poisoning `_wp_attachment_metadata`](3931777-author-arbitrary-file-deletion-anywhere-on-disk-site-takeove.md) |
| 1095645 | XML External Entities (XXE) | medium | $0 | [Authenticated XXE](1095645-authenticated-xxe.md) |
| 404323 | Business Logic Errors | high | $0 | [Logic flaw in the Post creation process allows creating posts with arbitrary types without needing the corresponding nonce](404323-logic-flaw-in-the-post-creation-process-allows-creating-post.md) |
| 3923967 | Code Injection | high | $0 | [WordPress 7.1 Media Processing Race Enables Persistent PHP File Write and Author-to-RCE](3923967-wordpress-7-1-media-processing-race-enables-persistent-php-f.md) |
| 4043537 | Improper Authentication - Generic | medium | $0 | [CampTix [camptix_private]: the view token is derived from the requester's own IP, so naming any attendee's e-mail unlocks the gated content](4043537-camptix-camptix-private-the-view-token-is-derived-from-the-r.md) |
| 221507 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [Multiple stored XSS in WordPress](221507-multiple-stored-xss-in-wordpress.md) |
| 339483 | Cross-site Scripting (XSS) - Generic | medium | $0 | ["Bad Protocols Validation" Bypass in "wp_kses_bad_protocol_once" using HTML-encoding without trailing semicolons](339483-bad-protocols-validation-bypass-in-wp-kses-bad-protocol-once.md) |
| 3931771 | Cross-site Scripting (XSS) - Stored | critical | $0 | [Author → stored XSS in wp-admin: unescaped sub-size filename from attachment metadata breaks out of the `src` attribute in `get_media_item()`](3931771-author-stored-xss-in-wp-admin-unescaped-sub-size-filename-fr.md) |
| 538008 | Improper Access Control - Generic | high | $0 | [Add users to groups who have restricted group invites](538008-add-users-to-groups-who-have-restricted-group-invites.md) |
| 273726 | Information Disclosure | medium | $0 | [Information / sensitive data disclosure on some endpoints](273726-information-sensitive-data-disclosure-on-some-endpoints.md) |
| 3933198 | Open Redirect | medium | $0 | [wordpress.org/openverse/: unauthenticated open redirect — `str_replace()`'s 4th arg is a count, not a limit; bypasses WordPress.org SSO allow-list](3933198-wordpress-org-openverse-unauthenticated-open-redirect-str-re.md) |
| 3863343 | Cross-site Scripting (XSS) - DOM | low | $0 | [DOM-based XSS in playground.wordpress.net (/scope:*/wp-includes/empty.html) lets any attacker run JavaScript on the origin via a single crafted link](3863343-dom-based-xss-in-playground-wordpress-net-scope-wp-includes.md) |
| 230234 | Cross-site Scripting (XSS) - Reflected | medium | $0 | [[mercantile.wordpress.org] Reflected XSS via AngularJS Template Injection](230234-mercantile-wordpress-org-reflected-xss-via-angularjs-templat.md) |
| 4100259 | Cross-site Scripting (XSS) - Stored | none | $0 | [Stored XSS in the Classic block element path](4100259-stored-xss-in-the-classic-block-element-path.md) |
| 4152553 | Information Disclosure | high | $0 | [Unauthenticated Disclosure of Private, Draft, and Password-Protected Post Content via Core Read-Permission Bypass in SCF Reference Fields](4152553-unauthenticated-disclosure-of-private-draft-and-password-pro.md) |
| 4053546 | Information Disclosure | medium | $0 | [Information Disclosure - Unauthen Leak Private Content](4053546-information-disclosure-unauthen-leak-private-content.md) |
| 385322 | Open API For Username enumeration | low | $0 | [Open API For Username enumeration](385322-open-api-for-username-enumeration.md) |
| 3460138 | Open Email Relay on WordPress Gutenberg Plugin via formAction parameter leads to phishing and spam campaigns | n/a | $0 | [Open Email Relay on WordPress Gutenberg Plugin via formAction parameter leads to phishing and spam campaigns](3460138-open-email-relay-on-wordpress-gutenberg-plugin-via-formactio.md) |
| 3942522 | Improper Access Control - Generic | high | $0 | [wordpress.org Rosetta: invite stores unvalidated role — Editor can assign site Administrator despite editable_roles](3942522-wordpress-org-rosetta-invite-stores-unvalidated-role-editor.md) |
| 881918 | Cross-site Scripting (XSS) - Stored | medium | $0 | [Authenticated Stored Cross-site Scripting in bbPress](881918-authenticated-stored-cross-site-scripting-in-bbpress.md) |
| 4029867 | Improper Access Control - Generic | medium | $0 | [WordCamp Meta gpre: password-protected event RSVP list readable without password via /gpre/v1/.../rsvp-responses](4029867-wordcamp-meta-gpre-password-protected-event-rsvp-list-readab.md) |
| 3801107 | Improper Access Control - Generic | critical | $0 | [Unauthenticated disclosure of private and hidden forum content in bbPress via the WordPress core REST single-item endpoint](3801107-unauthenticated-disclosure-of-private-and-hidden-forum-conte.md) |
| 179695 | Cross-site Scripting (XSS) - Generic | medium | $0 | [XSS via unicode characters in upload filename](179695-xss-via-unicode-characters-in-upload-filename.md) |
| 406289 | Cross-site Scripting (XSS) - Stored | low | $0 | [Stored XSS on Broken Themes via filename](406289-stored-xss-on-broken-themes-via-filename.md) |
| 203515 | Cross-site Scripting (XSS) - Generic | high | $0 | [Wordpress 4.7.2 - Two XSS in Media Upload when file too large.](203515-wordpress-4-7-2-two-xss-in-media-upload-when-file-too-large.md) |
| 278151 | Improper Access Control - Generic | low | $0 | [Content Spoofing @ https://irclogs.wordpress.org/](278151-content-spoofing-https-irclogs-wordpress-org.md) |
| 881855 | Cross-Site Request Forgery (CSRF) | medium | $0 | [Arbitrary change of blog's background image via CSRF](881855-arbitrary-change-of-blog-s-background-image-via-csrf.md) |
| 270060 | Reflected Swf XSS In ( plugins.svn.wordpress.org ) | medium | $0 | [Reflected Swf XSS In ( plugins.svn.wordpress.org )](270060-reflected-swf-xss-in-plugins-svn-wordpress-org.md) |
| 187520 | Cross-Site Request Forgery (CSRF) | high | $0 | [Wordpress 4.7 - CSRF -> HTTP SSRF any private ip:port and basic-auth](187520-wordpress-4-7-csrf-http-ssrf-any-private-ip-port-and-basic-a.md) |
| 204513 | Server-Side Request Forgery (SSRF) | medium | $0 | [Infrastructure - Photon - SSRF](204513-infrastructure-photon-ssrf.md) |
| 230435 | Cross-site Scripting (XSS) - DOM | medium | $0 | [DOM Based XSS In mercantile.wordpress.org](230435-dom-based-xss-in-mercantile-wordpress-org.md) |
| 3878399 | Cross-site Scripting (XSS) - DOM | medium | $0 | [Large-site Quick Edit reparses a Contributor display name into active HTML](3878399-large-site-quick-edit-reparses-a-contributor-display-name-in.md) |
| 460911 | Cross-site Scripting (XSS) - Stored | medium | $0 | [[FG-VD-18-165] Wordpress Cross-Site Scripting Vulnerability Notification II](460911-fg-vd-18-165-wordpress-cross-site-scripting-vulnerability-no.md) |
| 221893 | Cross-site Scripting (XSS) - Reflected | medium | $0 | [XSS in the search bar of mercantile.wordpress.org](221893-xss-in-the-search-bar-of-mercantile-wordpress-org.md) |
| 3941626 | Improper Access Control - Generic | high | $0 | [Instamojo CampTix: fail-open MAC + webhook Credit without binding payment to order](3941626-instamojo-camptix-fail-open-mac-webhook-credit-without-bindi.md) |
| 1172852 | Information Disclosure | medium | $0 | [PII of users can be downloaded from export pages](1172852-pii-of-users-can-be-downloaded-from-export-pages.md) |
| 291878 | Path Traversal | critical | $0 | [Arbitrary file deletion in wp-core - guides towards RCE and information disclosure](291878-arbitrary-file-deletion-in-wp-core-guides-towards-rce-and-in.md) |
| 179920 | SQL Injection | critical | $0 | [WordPress DB Class, bad implementation of prepare method guides to sqli and information disclosure](179920-wordpress-db-class-bad-implementation-of-prepare-method-guid.md) |
| 3871816 | Improper Access Control - Generic | high | $0 | [Unauthenticated private CSV export of Meetup organizer PII via broken authz check in WordCamp Reports](3871816-unauthenticated-private-csv-export-of-meetup-organizer-pii-v.md) |
| 223024 | UI Redressing (Clickjacking) | low | $0 | [Clickjacking In jobs.wordpress.net](223024-clickjacking-in-jobs-wordpress-net.md) |
| 222040 | Cross-site Scripting (XSS) - Reflected | medium | $0 | [Reflected XSS at https://da.wordpress.org/themes/?s= via "s=" parameter ](222040-reflected-xss-at-https-da-wordpress-org-themes-s-via-s-param.md) |
| 495515 | Cross-site Scripting (XSS) - Reflected | medium | $0 | [Reflected XSS: Taxonomy Converter via tax parameter](495515-reflected-xss-taxonomy-converter-via-tax-parameter.md) |
| 220903 | Cross-site Scripting (XSS) - Stored | medium | $0 | [Authenticated Cross-site Scripting in Template Name](220903-authenticated-cross-site-scripting-in-template-name.md) |
| 230232 | Cross-site Scripting (XSS) - Stored | low | $0 | [Stored self-XSS in mercantile.wordpress.org checkout](230232-stored-self-xss-in-mercantile-wordpress-org-checkout.md) |
| 149589 | Cross-Site Request Forgery (CSRF) | n/a | $0 | [CSRF to add admin [wordpress]](149589-csrf-to-add-admin-wordpress.md) |
| 497724 | Cross-site Scripting (XSS) - Stored | medium | $0 | [Stored XSS in Post Preview as Contributor](497724-stored-xss-in-post-preview-as-contributor.md) |
| 309058 | Open Redirect | low | $0 | [Open Redirect on the nl.wordpress.net](309058-open-redirect-on-the-nl-wordpress-net.md) |
| 263109 | Buddypress 2.9.1 - Exceeding the maximum upload size  - XSS leading to potential RCE.  | medium | $0 | [Buddypress 2.9.1 - Exceeding the maximum upload size  - XSS leading to potential RCE. ](263109-buddypress-2-9-1-exceeding-the-maximum-upload-size-xss-leadi.md) |
| 230581 | UI Redressing (Clickjacking) | low | $0 | [Clickjacking wordcamp.org](230581-clickjacking-wordcamp-org.md) |
| 1927360 | Improper Access Control - Generic | low | $0 | [Previously created sessions continue being valid after 2FA activation](1927360-previously-created-sessions-continue-being-valid-after-2fa-a.md) |
| 240256 | Cross-site Scripting (XSS) - Reflected | medium | $0 | [[mercantile.wordpress.org] Reflected XSS](240256-mercantile-wordpress-org-reflected-xss.md) |
| 222036 | Cleartext Transmission of Sensitive Information | low | $0 | [Missing SSL can leak job token ](222036-missing-ssl-can-leak-job-token.md) |
| 633231 | Cross-site Scripting (XSS) - Stored | high | $0 | [pre-auth Stored XSS in comments via javascript: url when administrator edits user supplied comment](633231-pre-auth-stored-xss-in-comments-via-javascript-url-when-admi.md) |
| 837256 | Improper Access Control - Generic | medium | $0 | [Improper Access Control in Buddypress core allows reply,delete any user's activity](837256-improper-access-control-in-buddypress-core-allows-reply-dele.md) |
| 309714 | Improper Access Control - Generic | none | $0 | [[support.wordcamp.org] - publicly accessible .svn repository](309714-support-wordcamp-org-publicly-accessible-svn-repository.md) |
| 250837 | Cross-site Scripting (XSS) - Stored | high | $0 | [Stored xss via template injection](250837-stored-xss-via-template-injection.md) |
| 264125 | UI Redressing (Clickjacking) | low | $0 | [Clickjacking mercantile.wordpress.org](264125-clickjacking-mercantile-wordpress-org.md) |
| 249759 | Cross-site Scripting (XSS) - Stored | medium | $0 | [Lack of Sanitization and Insufficient Authentication](249759-lack-of-sanitization-and-insufficient-authentication.md) |
| 384112 | Cross-site Scripting (XSS) - Reflected | low | $0 | [xss - reflected](384112-xss-reflected.md) |
| 754352 | Cross-site Scripting (XSS) - Stored | high | $0 | [Stored XSS on Wordpress 5.3 via Title Post](754352-stored-xss-on-wordpress-5-3-via-title-post.md) |
| 682344 | Business Logic Errors | n/a | $0 | [Parameter tampering : Price Manipulation of Products](682344-parameter-tampering-price-manipulation-of-products.md) |
| 355773 | Cross-site Scripting (XSS) - Reflected | n/a | $0 | [XSS on support.wordcamp.org in ajax-quote.php](355773-xss-on-support-wordcamp-org-in-ajax-quote-php.md) |
| 295330 | code.wordpress.net subdomain Takeover | medium | $0 | [code.wordpress.net subdomain Takeover](295330-code-wordpress-net-subdomain-takeover.md) |
| 299112 | Cross-site Scripting (XSS) - Reflected | high | $0 | [MediaElements XSS](299112-mediaelements-xss.md) |
| 183568 | [Buddypress] Arbitrary File Deletion through bp_avatar_set | high | $0 | [[Buddypress] Arbitrary File Deletion through bp_avatar_set](183568-buddypress-arbitrary-file-deletion-through-bp-avatar-set.md) |
| 833782 | Privilege Escalation | medium | $0 | [Allow authenticated users can edit, trash,and add new in BuddyPress Emails function](833782-allow-authenticated-users-can-edit-trash-and-add-new-in-budd.md) |
| 388254 | UI Redressing (Clickjacking) | high | $0 | [Account takeover vulnerability by editor role privileged users/attackers via clickjacking](388254-account-takeover-vulnerability-by-editor-role-privileged-use.md) |
| 224556 | Cross-site Scripting (XSS) - Generic | low | $0 | [Self-XSS in WordPress Editor Link Modal](224556-self-xss-in-wordpress-editor-link-modal.md) |
| 258283 | UI Redressing (Clickjacking) | low | $0 | [Clickjacking - https://mercantile.wordpress.org/](258283-clickjacking-https-mercantile-wordpress-org.md) |
| 222224 | Cross-site Scripting (XSS) - Stored | low | $0 | [Stored but [SELF] XSS in mercantile.wordpress.org](222224-stored-but-self-xss-in-mercantile-wordpress-org.md) |
| 277502 | Open Redirect | low | $0 | [[BuddyPress 2.9.1] Open Redirect via "wp_http_referer" parameter on "bp-profile-edit" endpoint](277502-buddypress-2-9-1-open-redirect-via-wp-http-referer-parameter.md) |
| 224214 | Lack of Password Confirmation when Changing Password and Email | n/a | $0 | [Lack of Password Confirmation when Changing Password and Email](224214-lack-of-password-confirmation-when-changing-password-and-ema.md) |
| 837018 | Privilege Escalation in BuddyPress core allows Moderate to Administrator  | medium | $0 | [Privilege Escalation in BuddyPress core allows Moderate to Administrator ](837018-privilege-escalation-in-buddypress-core-allows-moderate-to-a.md) |
| 153093 | Uncontrolled Resource Consumption | n/a | $0 | [WordPress core  - Denial of Service via Cross Site Request Forgery](153093-wordpress-core-denial-of-service-via-cross-site-request-forg.md) |
| 282176 | Improper Access Control - Generic | medium | $0 | [Unauthenticated hidden groups disclosure via Ajax groups search](282176-unauthenticated-hidden-groups-disclosure-via-ajax-groups-sea.md) |
| 914232 | Cross-Site Request Forgery (CSRF) | medium | $0 | [CSRF on comment post](914232-csrf-on-comment-post.md) |
| 836187 | Cross-Site Request Forgery (CSRF) | medium | $0 | [CSRF in Profile Fields allows deleting any field in BuddyPress](836187-csrf-in-profile-fields-allows-deleting-any-field-in-buddypre.md) |
| 263718 | Wordpress 4.8.1 - Rogue editor leads to RCE. And the risks of same origin frame scripting in general | high | $0 | [Wordpress 4.8.1 - Rogue editor leads to RCE. And the risks of same origin frame scripting in general](263718-wordpress-4-8-1-rogue-editor-leads-to-rce-and-the-risks-of-s.md) |
| 221734 | Information Disclosure | medium | $0 | [Administrator(s) Information disclosure via JSON on wordpress.org](221734-administrator-s-information-disclosure-via-json-on-wordpress.md) |
| 298218 | Cross-site Scripting (XSS) - Generic | low | $0 | [antispambot does not always escape <, >, &, " and '](298218-antispambot-does-not-always-escape-and.md) |
| 276105 | Cross-site Scripting (XSS) - Stored | medium | $0 | [Stored XSS in WordPress](276105-stored-xss-in-wordpress.md) |
| 228854 | Cryptographic Issues - Generic | high | $0 | [WordPress Automatic Update Protocol Does Not Authenticate Updates Provided by the Server](228854-wordpress-automatic-update-protocol-does-not-authenticate-up.md) |
| 267075 | UI Redressing (Clickjacking) | n/a | $0 | [Clickjacking irclogs.wordpress.org](267075-clickjacking-irclogs-wordpress-org.md) |
| 282843 | Information Disclosure | none | $0 | [UnResolved ChangeSet are Visible to Public That also Causes Information Disclosure](282843-unresolved-changeset-are-visible-to-public-that-also-causes.md) |
