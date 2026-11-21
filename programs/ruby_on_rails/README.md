# Ruby on Rails

Disclosed reports: **74**

| ID | Temuan | Severity | Bounty | Writeup |
| --- | --- | --- | ---: | --- |
| 473888 | Command Injection - Generic | high | $1500 | [RCE which may occur due to `ActiveSupport::MessageVerifier` or `ActiveSupport::MessageEncryptor` (especially Active storage)](473888-rce-which-may-occur-due-to-activesupport-messageverifier-or.md) |
| 307808 | Path Traversal | medium | $1500 | [Path Traversal on Default Installed Rails Application (Asset Pipeline)](307808-path-traversal-on-default-installed-rails-application-asset.md) |
| 394253 | Validation bypass for queries generated for PostgreSQL | n/a | $1500 | [Validation bypass for queries generated for PostgreSQL](394253-validation-bypass-for-queries-generated-for-postgresql.md) |
| 113928 | Code Injection | n/a | $1500 | [Remote code execution using render :inline](113928-remote-code-execution-using-render-inline.md) |
| 519220 | Path Traversal | high | $1000 | [File writing by Directory traversal at actionpack-page_caching and RCE by it](519220-file-writing-by-directory-traversal-at-actionpack-page-cachi.md) |
| 904059 | Open Redirect | high | $1000 | [Open Redirect (6.0.0 < rails < 6.0.3.2)](904059-open-redirect-6-0-0-rails-6-0-3-2.md) |
| 46019 | Code Injection | high | $500 | [Explicit, dynamic render path: Dir. Trav + RCE](46019-explicit-dynamic-render-path-dir-trav-rce.md) |
| 949513 | Cross-site Scripting (XSS) - Stored | medium | $500 | [XSS by file (Active Storage `Proxying`)](949513-xss-by-file-active-storage-proxying.md) |
| 3008446 | Cross-site Scripting (XSS) - Generic | medium | $0 | [1-Click Cross-Site Scripting via Custom Configuration in SafeListSanitizer](3008446-1-click-cross-site-scripting-via-custom-configuration-in-saf.md) |
| 3580511 | Path Traversal | medium | $0 | [ActiveStorage Disk Service Path Traversal via Custom Blob Key Injection](3580511-activestorage-disk-service-path-traversal-via-custom-blob-ke.md) |
| 2303609 | Cross-site Scripting (XSS) - Generic | low | $0 | [XSS when using `translate` in Action Controller (Rails 7.0, 7.1)](2303609-xss-when-using-translate-in-action-controller-rails-7-0-7-1.md) |
| 895727 | Reliance on Cookies without Validation and Integrity Checking in a Security Decision | low | $0 | [Rack parses encoded cookie names allowing an attacker to send malicious `__Host-` and `__Secure-` prefixed cookies](895727-rack-parses-encoded-cookie-names-allowing-an-attacker-to-sen.md) |
| 1444151 | Cross-site Scripting (XSS) - Generic | medium | $0 | [XSS vulnerabilities due to missing checks in tag helpers](1444151-xss-vulnerabilities-due-to-missing-checks-in-tag-helpers.md) |
| 2334455 | Path Traversal | high | $0 | [Path traversal in AcitveStorage, and lead RCE](2334455-path-traversal-in-acitvestorage-and-lead-rce.md) |
| 2389565 | Cross-site Scripting (XSS) - Stored | medium | $0 | [Action Text XSS (Rails 7.1.x)](2389565-action-text-xss-rails-7-1-x.md) |
| 1023899 | Uncontrolled Resource Consumption | medium | $0 | [Regular expression denial of service in ActiveRecord's PostgreSQL Money type](1023899-regular-expression-denial-of-service-in-activerecord-s-postg.md) |
| 3553340 | Path Traversal | high | $0 | [Active Storage Vips Transformer Missing validate_transformation — CVE-2025-24293 Incomplete Fix](3553340-active-storage-vips-transformer-missing-validate-transformat.md) |
| 2389431 | Uncontrolled Resource Consumption | low | $0 | [Action Text ReDoS (Ruby 3.1  or lower)](2389431-action-text-redos-ruby-3-1-or-lower.md) |
| 1154034 | Code Injection | high | $0 | [Argument/Code Injection via ActiveStorage's image transformation functionality](1154034-argument-code-injection-via-activestorage-s-image-transforma.md) |
| 2307813 | DoS with crafted "Range" header | high | $0 | [DoS with crafted "Range" header](2307813-dos-with-crafted-range-header.md) |
| 1694173 | Cross-site Scripting (XSS) - Generic | medium | $0 | [ActionView sanitize helper bypass leading to XSS using SVG tag.](1694173-actionview-sanitize-helper-bypass-leading-to-xss-using-svg-t.md) |
| 3994016 | Cross-site Scripting (XSS) - Stored | medium | $0 | [Action Text to_markdown: <code>/<pre> content escapes its delimiter, letting a stored body inject arbitrary Markdown](3994016-action-text-to-markdown-code-pre-content-escapes-its-delimit.md) |
| 3601655 | Rails::HTML::Sanitizer.allowed_uri? returns true for entity-encoded control-character-split javascript: URLs | low | $0 | [Rails::HTML::Sanitizer.allowed_uri? returns true for entity-encoded control-character-split javascript: URLs](3601655-rails-html-sanitizer-allowed-uri-returns-true-for-entity-enc.md) |
| 1302395 | Use of Hard-coded Cryptographic Key | medium | $0 | [Sauce Labs API key unencrypted in an old commit](1302395-sauce-labs-api-key-unencrypted-in-an-old-commit.md) |
| 1327196 | Cross-site Scripting (XSS) - Stored | n/a | $0 | [Content Security Policy is only active for HTML responses  but not for image/svg+xml](1327196-content-security-policy-is-only-active-for-html-responses-bu.md) |
| 2814774 | Uncontrolled Resource Consumption | medium | $0 | [Possible DoS in NumberHelpers](2814774-possible-dos-in-numberhelpers.md) |
| 1489141 | ReDoS in Rack::Multipart | high | $0 | [ReDoS in Rack::Multipart](1489141-redos-in-rack-multipart.md) |
| 328270 | Cross-site Scripting (XSS) - Generic | medium | $0 | [XSS vulnerability in sanitize-method when parsing link's href](328270-xss-vulnerability-in-sanitize-method-when-parsing-link-s-hre.md) |
| 1429148 | Privilege Escalation | high | $0 | [Subdomain Takeover at https://new.rubyonrails.org/](1429148-subdomain-takeover-at-https-new-rubyonrails-org.md) |
| 431561 | Specially constructed multi-part requests cause multi-second response times; vulnerable to DoS | medium | $0 | [Specially constructed multi-part requests cause multi-second response times; vulnerable to DoS](431561-specially-constructed-multi-part-requests-cause-multi-second.md) |
| 4082665 | Cross-site Scripting (XSS) - Reflected | medium | $0 | [ActionText `to_markdown` still allows `javascript:` links in kramdown via Rails-generated table cells after PR #58754](4082665-actiontext-to-markdown-still-allows-javascript-links-in-kram.md) |
| 1955370 | Cross-site Scripting (XSS) - Reflected | medium | $0 | [Incorrect handling of certain characters passed to the redirection functionality in Rails can lead to a single-click XSS vulnerability.](1955370-incorrect-handling-of-certain-characters-passed-to-the-redir.md) |
| 3727743 | Cross-site Scripting (XSS) - Reflected | medium | $0 | [URI scheme validation bypass in ActionText `to_markdown` via user-supplied `<action-text-markdown>` marker tag](3727743-uri-scheme-validation-bypass-in-actiontext-to-markdown-via-u.md) |
| 474262 | Cross-site Scripting (XSS) - Generic | low | $0 | [XSS due to incomplete JS escaping](474262-xss-due-to-incomplete-js-escaping.md) |
| 803922 | Information Disclosure | medium | $0 | [Missing resource identifier encoding may lead to security vulnerabilities](803922-missing-resource-identifier-encoding-may-lead-to-security-vu.md) |
| 44513 | Code Injection | n/a | $0 | [RCE due to Web Console IP Whitelist bypass in Rails 4.0 and 4.1](44513-rce-due-to-web-console-ip-whitelist-bypass-in-rails-4-0-and.md) |
| 1702859 | Deserialization of Untrusted Data | high | $0 | [Unexpected deserialization in Kredis](1702859-unexpected-deserialization-in-kredis.md) |
| 1684163 | ReDoS (Rails::Html::PermitScrubber.scrub_attribute) | n/a | $0 | [ReDoS (Rails::Html::PermitScrubber.scrub_attribute)](1684163-redos-rails-html-permitscrubber-scrub-attribute.md) |
| 1106652 | Information Exposure Through an Error Message | low | $0 | [redirect_to(["string"]) remote code execution](1106652-redirect-to-string-remote-code-execution.md) |
| 90457 | Nested attributes reject_if proc can be circumvented by providing "_destroy" parameter | high | $0 | [Nested attributes reject_if proc can be circumvented by providing "_destroy" parameter](90457-nested-attributes-reject-if-proc-can-be-circumvented-by-prov.md) |
| 1656627 | Cross-site Scripting (XSS) - Generic | medium | $0 | [Rails::Html::SafeListSanitizer vulnerable to XSS when certain tags are allowed (math+style \|\| svg+style)](1656627-rails-html-safelistsanitizer-vulnerable-to-xss-when-certain.md) |
| 1530898 | Cross-site Scripting (XSS) - Generic | medium | $0 | [Rails::Html::SafeListSanitizer vulnerable to xss attack in an environment that allows the style tag](1530898-rails-html-safelistsanitizer-vulnerable-to-xss-attack-in-an.md) |
| 407319 | Information Disclosure | high | $0 | [ActiveStorage service's signed URLs can be hijacked via AppCache+Cookie stuffing trick when using GCS or DiskService](407319-activestorage-service-s-signed-urls-can-be-hijacked-via-appc.md) |
| 3370 | Information Disclosure | n/a | $0 | [Directory traversal attack in view resolver](3370-directory-traversal-attack-in-view-resolver.md) |
| 42797 | Uncontrolled Resource Consumption | n/a | $0 | [Denial of Service in Action Pack Exception Handling](42797-denial-of-service-in-action-pack-exception-handling.md) |
| 47280 | Cross-site Scripting (XSS) - Generic | high | $0 | [JSON keys are not properly escaped](47280-json-keys-are-not-properly-escaped.md) |
| 1654310 | Cross-site Scripting (XSS) - Generic | medium | $0 | [Incomplete fix for CVE-2022-32209 (XSS in Rails::Html::Sanitizer under certain configurations)](1654310-incomplete-fix-for-cve-2022-32209-xss-in-rails-html-sanitize.md) |
| 1047447 | Open Redirect | low | $0 | [HostAuthorization middleware does not suitably sanitize the Host / X-Forwarded-For header allowing redirection.](1047447-hostauthorization-middleware-does-not-suitably-sanitize-the.md) |
| 732415 | Cross-Site Request Forgery (CSRF) | medium | $0 | [The authenticity_token can be reversed and used to forge valid per_form_csrf_tokens for arbitrary routes](732415-the-authenticity-token-can-be-reversed-and-used-to-forge-val.md) |
| 139321 | Unsafe Query Generation (CVE-2012-2660, CVE-2012-2694 and CVE-2013-0155) mitigation bypass | n/a | $0 | [Unsafe Query Generation (CVE-2012-2660, CVE-2012-2694 and CVE-2013-0155) mitigation bypass](139321-unsafe-query-generation-cve-2012-2660-cve-2012-2694-and-cve.md) |
| 94568 | Improper Authentication - Generic | n/a | $0 | [http_basic_authenticate_with is suseptible to timing attacks.](94568-http-basic-authenticate-with-is-suseptible-to-timing-attacks.md) |
| 888176 | Improper Neutralization of HTTP Headers for Scripting Syntax | n/a | $0 | [HTTP Host injection in redirect_to function](888176-http-host-injection-in-redirect-to-function.md) |
| 42728 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [Data-Tags and the New HTML Sanitizer Subverts CSRF protection](42728-data-tags-and-the-new-html-sanitizer-subverts-csrf-protectio.md) |
| 113831 | Code Injection | n/a | $0 | [Regarding [CVE-2016-0752] Possible Information Leak Vulnerability in Action View](113831-regarding-cve-2016-0752-possible-information-leak-vulnerabil.md) |
| 429873 | Cross-site Scripting (XSS) - Stored | medium | $0 | [XSS by MathML at Active Storage](429873-xss-by-mathml-at-active-storage.md) |
| 942103 | Command Injection - Generic | none | $0 | [Server-side template injection at ujs test server](942103-server-side-template-injection-at-ujs-test-server.md) |
| 789579 | Client-Side Enforcement of Server-Side Security | medium | $0 | [ActiveStorage direct upload fails to sign content-length header for S3 service](789579-activestorage-direct-upload-fails-to-sign-content-length-hea.md) |
| 81212 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [Potential XSS on sanitize/Rails::Html::WhiteListSanitizer](81212-potential-xss-on-sanitize-rails-html-whitelistsanitizer.md) |
| 108723 | Violation of Secure Design Principles | medium | $0 | [Validation bypass for Active Record and Active Model](108723-validation-bypass-for-active-record-and-active-model.md) |
| 43440 | Arbitrary file existence disclosure in Action Pack | n/a | $0 | [Arbitrary file existence disclosure in Action Pack](43440-arbitrary-file-existence-disclosure-in-action-pack.md) |
| 1057216 | Code Injection | n/a | $0 | [Regex Injection from request header (Rack::Sendfile, send_file)](1057216-regex-injection-from-request-header-rack-sendfile-send-file.md) |
| 292797 | ActionController::Parameters .each returns an unsafe hash | medium | $0 | [ActionController::Parameters .each returns an unsafe hash](292797-actioncontroller-parameters-each-returns-an-unsafe-hash.md) |
| 63131 | Violation of Secure Design Principles | n/a | $0 | [Changeable model ids on vanilla update can lead to severely bad side-effects](63131-changeable-model-ids-on-vanilla-update-can-lead-to-severely.md) |
| 1300802 | Uncontrolled Resource Consumption | medium | $0 | [Possible DOS in app with crashing `exceptions_app`](1300802-possible-dos-in-app-with-crashing-exceptions-app.md) |
| 899069 | Uncontrolled Resource Consumption | medium | $0 | [Untrusted users able to run pending migrations in production](899069-untrusted-users-able-to-run-pending-migrations-in-production.md) |
| 81396 | Cross-site Scripting (XSS) - Generic | n/a | $0 | [[Rails42] We can inject HTML tags when server is using strip_tags method](81396-rails42-we-can-inject-html-tags-when-server-is-using-strip-t.md) |
| 83962 | Uncontrolled Resource Consumption | n/a | $0 | [DoS Attack in Controller Lookup Code](83962-dos-attack-in-controller-lookup-code.md) |
| 49935 | Cross-Site Request Forgery (CSRF) | n/a | $0 | [rails-ujs will send CSRF tokens to other origins](49935-rails-ujs-will-send-csrf-tokens-to-other-origins.md) |
| 1411867 | Escape Sequence Injection vulnerability in Rack | medium | $0 | [Escape Sequence Injection vulnerability in Rack](1411867-escape-sequence-injection-vulnerability-in-rack.md) |
| 189878 | Cross-Site Request Forgery (CSRF) | low | $0 | [CSRF header is sent to external websites when using data-remote forms](189878-csrf-header-is-sent-to-external-websites-when-using-data-rem.md) |
| 413388 | Deserialization of Untrusted Data | high | $0 | [Untrusted strings that are cache fetched with raw option are automatically marshal loaded](413388-untrusted-strings-that-are-cache-fetched-with-raw-option-are.md) |
| 755354 | Cross-site Scripting (XSS) - DOM | low | $0 | [Prevent XSS when passing a parameter directly into link_to ](755354-prevent-xss-when-passing-a-parameter-directly-into-link-to.md) |
| 28450 | Active Record SQL Injection Vulnerability Affecting PostgreSQL | n/a | $0 | [Active Record SQL Injection Vulnerability Affecting PostgreSQL](28450-active-record-sql-injection-vulnerability-affecting-postgres.md) |
| 28449 | Active Record SQL Injection Vulnerability Affecting PostgreSQL | n/a | $0 | [Active Record SQL Injection Vulnerability Affecting PostgreSQL](28449-active-record-sql-injection-vulnerability-affecting-postgres.md) |
