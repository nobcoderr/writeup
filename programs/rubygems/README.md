# RubyGems

Disclosed reports: **32**

| ID | Temuan | Severity | Bounty | Writeup |
| --- | --- | --- | ---: | --- |
| 274990 | Deserialization of Untrusted Data | critical | $1500 | [Remote code execution on rubygems.org](274990-remote-code-execution-on-rubygems-org.md) |
| 275269 | Cryptographic Issues - Generic | medium | $1000 | [Gem signature forgery](275269-gem-signature-forgery.md) |
| 243156 | Path Traversal | high | $1000 | [Installing a crafted gem package may create or overwrite files](243156-installing-a-crafted-gem-package-may-create-or-overwrite-fil.md) |
| 317321 | Path Traversal | medium | $500 | [Delete directory using symlink when decompressing tar](317321-delete-directory-using-symlink-when-decompressing-tar.md) |
| 411519 | Path Traversal | high | $500 | [DNS SRV lookup of file:// sources enables local hijacking of gems](411519-dns-srv-lookup-of-file-sources-enables-local-hijacking-of-ge.md) |
| 226335 | Command Injection - Generic | low | $500 | [Escape sequence injection in "summary" field](226335-escape-sequence-injection-in-summary-field.md) |
| 2627221 | Host Header Attac | medium | $0 | [Host Header Attac](2627221-host-header-attac.md) |
| 3097900 | Improper Access Control - Generic | none | $0 | [`/names.nsf` and all `/names*` files route to public API on rubygems.org](3097900-names-nsf-and-all-names-files-route-to-public-api-on-rubygem.md) |
| 3542546 | Uncontrolled Resource Consumption | n/a | $0 | [Server-side ReDoS via user-controlled regex in OIDC Access Policy](3542546-server-side-redos-via-user-controlled-regex-in-oidc-access-p.md) |
| 270072 | Path Traversal | medium | $0 | [Unpacker improperly validates symlinks, allowing gems writes to arbitrary locations](270072-unpacker-improperly-validates-symlinks-allowing-gems-writes.md) |
| 3079931 | Uncontrolled Resource Consumption | medium | $0 | [Memory leak in gem decode logic can allow attacker to take down Rubygems.org application](3079931-memory-leak-in-gem-decode-logic-can-allow-attacker-to-take-d.md) |
| 1119120 | Deserialization of Untrusted Data | n/a | $0 | [Bundler's RCE with response using Marshal](1119120-bundler-s-rce-with-response-using-marshal.md) |
| 3938927 | Improper Access Control - Generic | high | $0 | [An organization admin can create an attacker-controlled organization owner via the gem transfer flow ](3938927-an-organization-admin-can-create-an-attacker-controlled-orga.md) |
| 1536013 | Inadequate Encryption Strength | low | $0 | [Possibility to guess email address from gravatar image URL](1536013-possibility-to-guess-email-address-from-gravatar-image-url.md) |
| 1430405 | Open Redirect | medium | $0 | [Dependency repository hijacking aka Repo Jacking from GitHub repo rubygems/bundler-site & rubygems/bundler.github.io + bundler.io docs](1430405-dependency-repository-hijacking-aka-repo-jacking-from-github.md) |
| 218088 | Code Injection | high | $0 | [Request Hijacking Vulnerability in RubyGems 2.6.11 and earlier](218088-request-hijacking-vulnerability-in-rubygems-2-6-11-and-earli.md) |
| 170301 | Invalid username updating | n/a | $0 | [Invalid username updating](170301-invalid-username-updating.md) |
| 173251 | Improper Authentication - Generic | n/a | $0 | [Password Reset emails missing TLS leads account takeover](173251-password-reset-emails-missing-tls-leads-account-takeover.md) |
| 392311 | Command Injection - Generic | critical | $0 | [Malware in `active-support` gem](392311-malware-in-active-support-gem.md) |
| 270068 | Path Traversal | medium | $0 | [Installer can modify other gems if gem name is specially crafted](270068-installer-can-modify-other-gems-if-gem-name-is-specially-cra.md) |
| 449356 | 65534 times efficient, Brute-force attack for api_key | low | $0 | [65534 times efficient, Brute-force attack for api_key](449356-65534-times-efficient-brute-force-attack-for-api-key.md) |
| 281336 | Uncontrolled Resource Consumption | low | $0 | [Negative size in tar header causes infinite loop](281336-negative-size-in-tar-header-causes-infinite-loop.md) |
| 274267 | Command Injection - Generic | low | $0 | [Request Hijacking Vulnerability in RubyGems 2.6.13 and earlier](274267-request-hijacking-vulnerability-in-rubygems-2-6-13-and-earli.md) |
| 243003 | Uncontrolled Resource Consumption | high | $0 | [No limit of summary length allows Denail of Service](243003-no-limit-of-summary-length-allows-denail-of-service.md) |
| 178409 | Possible Subdomain Takeover at http://production.s3.rubygems.org/ pointing to Fastly  | none | $0 | [Possible Subdomain Takeover at http://production.s3.rubygems.org/ pointing to Fastly ](178409-possible-subdomain-takeover-at-http-production-s3-rubygems-o.md) |
| 289313 | Cross-site Scripting (XSS) - Stored | medium | $0 | [[gem server] Stored XSS via crafted JavaScript URL inclusion in Gemspec](289313-gem-server-stored-xss-via-crafted-javascript-url-inclusion-i.md) |
| 307681 | Cross-site Scripting (XSS) - Generic | low | $0 | [Cross-Domain JavaScript Source File Inclusion ](307681-cross-domain-javascript-source-file-inclusion.md) |
| 180196 | Open Redirect | low | $0 | [Host header Injection rubygems.org](180196-host-header-injection-rubygems-org.md) |
| 173268 | Violation of Secure Design Principles | n/a | $0 | [Login credentials transmitted in cleartext on index.rubygems.org](173268-login-credentials-transmitted-in-cleartext-on-index-rubygems.md) |
| 170333 | Violation of Secure Design Principles | none | $0 | [Host Header Injection/Redirection](170333-host-header-injection-redirection.md) |
| 170748 | Command Injection - Generic | n/a | $0 | [RCE,SQL,Vulnerability + Exploit Method.](170748-rce-sql-vulnerability-exploit-method.md) |
| 103993 | Request Hijacking Vulnerability In RubyGems 2.4.6 And Earlier | n/a | $0 | [Request Hijacking Vulnerability In RubyGems 2.4.6 And Earlier](103993-request-hijacking-vulnerability-in-rubygems-2-4-6-and-earlie.md) |
