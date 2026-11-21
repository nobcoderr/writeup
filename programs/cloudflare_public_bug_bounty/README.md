# Cloudflare Public Bug Bounty

Disclosed reports: **48**

| ID | Temuan | Severity | Bounty | Writeup |
| --- | --- | --- | ---: | --- |
| 1785260 | Using special IPv4-mapped IPv6 addresses to bypass local IP ban | critical | $7500 | [Using special IPv4-mapped IPv6 addresses to bypass local IP ban](1785260-using-special-ipv4-mapped-ipv6-addresses-to-bypass-local-ip.md) |
| 1478633 | HTTP Request Smuggling | critical | $6000 | [HTTP Request Smuggling in Transform Rules using hexadecimal escape sequences in the concat() function](1478633-http-request-smuggling-in-transform-rules-using-hexadecimal.md) |
| 1419341 | Improper Authorization | critical | $6000 | [Hijack all emails sent to any domain that uses Cloudflare Email Forwarding](1419341-hijack-all-emails-sent-to-any-domain-that-uses-cloudflare-em.md) |
| 1952124 | Cloudflare CASB Confused Deputy Problem | critical | $3300 | [Cloudflare CASB Confused Deputy Problem](1952124-cloudflare-casb-confused-deputy-problem.md) |
| 1575912 | HTTP Request Smuggling | critical | $3100 | [HTTP request smuggling with Origin Rules using newlines in the host_header action parameter](1575912-http-request-smuggling-with-origin-rules-using-newlines-in-t.md) |
| 3622877 | Improper Access Control - Generic | high | $1500 | [HTTP Request Smuggling via Unsanitized Hop-by-Hop Headers](3622877-http-request-smuggling-via-unsanitized-hop-by-hop-headers.md) |
| 1700276 | Take over subdomains of r2.dev using R2 custom domains | medium | $1125 | [Take over subdomains of r2.dev using R2 custom domains](1700276-take-over-subdomains-of-r2-dev-using-r2-custom-domains.md) |
| 1593404 | Improper Authentication - Generic | high | $1000 | [Sign in with Apple works on existing accounts, bypasses 2FA](1593404-sign-in-with-apple-works-on-existing-accounts-bypasses-2fa.md) |
| 1633231 | Client-Side Enforcement of Server-Side Security | high | $1000 | [Completely remove VPN profile from locked WARP iOS cient.](1633231-completely-remove-vpn-profile-from-locked-warp-ios-cient.md) |
| 1605847 | Client-Side Enforcement of Server-Side Security | high | $1000 | [I found another way to bypass Cloudflare Warp lock!](1605847-i-found-another-way-to-bypass-cloudflare-warp-lock.md) |
| 1635748 | Client-Side Enforcement of Server-Side Security | high | $1000 | [Ability to bypass locked Cloudflare WARP on wifi networks.](1635748-ability-to-bypass-locked-cloudflare-warp-on-wifi-networks.md) |
| 3211031 | Cross-site Scripting (XSS) - Generic | medium | $550 | [`use-mcp`'s oauth2 process uses a window.open call with untrusted mcp server provided data allowing for code execution under the page using it](3211031-use-mcp-s-oauth2-process-uses-a-window-open-call-with-untrus.md) |
| 1507412 | Information Disclosure | high | $500 | [API docs expose an active token for the sample domain theburritobot.com](1507412-api-docs-expose-an-active-token-for-the-sample-domain-thebur.md) |
| 1754811 | Information Disclosure | medium | $500 | [Extraction of Pages build scripts, config values, tokens, etc. via symlinks](1754811-extraction-of-pages-build-scripts-config-values-tokens-etc-v.md) |
| 1542450 | Client-Side Enforcement of Server-Side Security | medium | $500 | [Bypass Cloudflare WARP lock on iOS.](1542450-bypass-cloudflare-warp-lock-on-ios.md) |
| 1636320 | Uncontrolled Resource Consumption | high | $500 | [Lack of Packet Sanitation in Goflow Results in Multiple DoS Attack Vectors and Bugs](1636320-lack-of-packet-sanitation-in-goflow-results-in-multiple-dos.md) |
| 2170559 | Improper Restriction of Authentication Attempts | medium | $350 | [Bypass R2 payment screen](2170559-bypass-r2-payment-screen.md) |
| 1979372 | Privilege Escalation | low | $350 | [Privilege escalation to root in Pages build image v2](1979372-privilege-escalation-to-root-in-pages-build-image-v2.md) |
| 1664974 | Improper Authentication - Generic | low | $250 | [Bypass two-factor authentication](1664974-bypass-two-factor-authentication.md) |
| 1724464 | Business Logic Errors | low | $250 | [cd=false (DNSSEC) not respected in DNS over HTTPS JSON requests](1724464-cd-false-dnssec-not-respected-in-dns-over-https-json-request.md) |
| 1593413 | Improper Authentication - Generic | low | $250 | [Sign in with Apple generates long-life JWTs, seemingly irrevocable, that grant immediate access to accounts](1593413-sign-in-with-apple-generates-long-life-jwts-seemingly-irrevo.md) |
| 1624911 | Misconfigured build on websites "abuse.cloudflare.com" | low | $100 | [Misconfigured build on websites "abuse.cloudflare.com"](1624911-misconfigured-build-on-websites-abuse-cloudflare-com.md) |
| 1615743 | Basic XSS [WAF Bypasses] | n/a | $50 | [Basic XSS [WAF Bypasses]](1615743-basic-xss-waf-bypasses.md) |
| 1805779 | Improper Access Control - Generic | high | $0 | [2FA BYPASS](1805779-2fa-bypass.md) |
| 3027461 | Improper Access Control - Generic | high | $0 | [Bypass of Cloudflare's Cache Keys and WAF via header overflow](3027461-bypass-of-cloudflare-s-cache-keys-and-waf-via-header-overflo.md) |
| 2094346 | Yet Another CASB Integration Takeover of Active Integrations | high | $0 | [Yet Another CASB Integration Takeover of Active Integrations](2094346-yet-another-casb-integration-takeover-of-active-integrations.md) |
| 3423950 | Cross-site Scripting (XSS) - Stored | high | $0 | [[Variation of #3321406] YetAnother 1-Click Chaining of Self-XSS, Cookie Tossing and AntiCSRF Token Prediction leads to auto approval in AccessTempAuth](3423950-variation-of-3321406-yetanother-1-click-chaining-of-self-xss.md) |
| 3424998 | Cross-site Scripting (XSS) - Reflected | low | $0 | [AI Playground XSS to steal user-chat messages and access to connected MCP Server](3424998-ai-playground-xss-to-steal-user-chat-messages-and-access-to.md) |
| 1467044 | Server-Side Request Forgery (SSRF) | low | $0 | [Blind SSRF on platform.dash.cloudflare.com Due to Sentry misconfiguration](1467044-blind-ssrf-on-platform-dash-cloudflare-com-due-to-sentry-mis.md) |
| 1941390 | Cleartext Transmission of Sensitive Information | high | $0 | [Plaintext leakage of DNS requests in Windows 1.1.1.1 WARP client](1941390-plaintext-leakage-of-dns-requests-in-windows-1-1-1-1-warp-cl.md) |
| 3316910 | Cross-site Scripting (XSS) - Stored | low | $0 | [Second-Order XSS via javascript protocol in MCP Server Portal Apps leads to ATO](3316910-second-order-xss-via-javascript-protocol-in-mcp-server-porta.md) |
| 2802817 | Improper Authentication - Generic | none | $0 | [Any WARP User Can Access Organization-Specific Application](2802817-any-warp-user-can-access-organization-specific-application.md) |
| 2122690 | Improper Authentication - Generic | high | $0 | [Accessing apps protected via ZT's Access when user account is deleted/disabled even after clearing user session/seat](2122690-accessing-apps-protected-via-zt-s-access-when-user-account-i.md) |
| 1570874 | Arbitrary file read from Cloudflare Pages build environment | medium | $0 | [Arbitrary file read from Cloudflare Pages build environment](1570874-arbitrary-file-read-from-cloudflare-pages-build-environment.md) |
| 1543259 | Improper Authentication - Generic | medium | $0 | [Signup with any Email and Enable 2-FA without verifying Email](1543259-signup-with-any-email-and-enable-2-fa-without-verifying-emai.md) |
| 1618021 | Improper Access Control - Generic | medium | $0 | [Enable 2Fa verification without verifying email](1618021-enable-2fa-verification-without-verifying-email.md) |
| 3321406 | [Variation of #1554049] 1-Click Chaining of Self-XSS, Cookie Tossing and AntiCSRF Token Prediction leads to auto approval in Access Temp Auth | high | $0 | [[Variation of #1554049] 1-Click Chaining of Self-XSS, Cookie Tossing and AntiCSRF Token Prediction leads to auto approval in Access Temp Auth](3321406-variation-of-1554049-1-click-chaining-of-self-xss-cookie-tos.md) |
| 1391635 | Information Disclosure | medium | $0 | [Bypassing Cache Deception Armor using .avif extension file](1391635-bypassing-cache-deception-armor-using-avif-extension-file.md) |
| 1525309 | Improper Access Control - Generic | high | $0 | [A malicious actor could rotate tokens of a victim, given that he knows the victim's token ID](1525309-a-malicious-actor-could-rotate-tokens-of-a-victim-given-that.md) |
| 1781096 | Memory Corruption - Generic | low | $0 | [💥💥Crash report -Cloudflare WARP doesn't verify text length in "Excluded Host" name input data💥💥](1781096-crash-report-cloudflare-warp-doesn-t-verify-text-length-in-e.md) |
| 2174818 | Resource Injection | low | $0 | [YAML schema injection risk in Swagger UI via schema_url parameter at developers.cloudflare.com](2174818-yaml-schema-injection-risk-in-swagger-ui-via-schema-url-para.md) |
| 1728292 | Business Logic Errors | medium | $0 | [Cloudflare is not properly deleting user's account](1728292-cloudflare-is-not-properly-deleting-user-s-account.md) |
| 1803659 | Information Exposure Through an Error Message | medium | $0 | [Origin IP address disclosure through Pingora response header](1803659-origin-ip-address-disclosure-through-pingora-response-header.md) |
| 1812705 | Improper Authentication - Generic | low | $0 | [Bypassing creation of  API tokens without email verification](1812705-bypassing-creation-of-api-tokens-without-email-verification.md) |
| 1825227 | Insecure Direct Object Reference (IDOR) | medium | $0 | [Session mismatch leading to potential account takeover (local access required)](1825227-session-mismatch-leading-to-potential-account-takeover-local.md) |
| 2086301 | Improper Access Control - Generic | high | $0 | [Permanent CASB Integration Takeover due to Improper Access Controls+Confused Deputy Problem](2086301-permanent-casb-integration-takeover-due-to-improper-access-c.md) |
| 1675730 | Violation of Secure Design Principles | low | $0 | [Password Policy Restriction Bypass](1675730-password-policy-restriction-bypass.md) |
| 2043885 | Client-Side Enforcement of Server-Side Security | high | $0 | [Ability to  bypass Admin override on Cloudflare WARP Android](2043885-ability-to-bypass-admin-override-on-cloudflare-warp-android.md) |
