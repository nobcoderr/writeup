# Node.js

Disclosed reports: **171**

| ID | Temuan | Severity | Bounty | Writeup |
| --- | --- | --- | ---: | --- |
| 1069487 | Improper Access Control - Generic | high | $500 | [DNS rebinding in --inspect (insufficient fix of CVE-2018-7160)](1069487-dns-rebinding-in-inspect-insufficient-fix-of-cve-2018-7160.md) |
| 1002188 | HTTP Request Smuggling | low | $250 | [Potential HTTP Request Smuggling in nodejs](1002188-potential-http-request-smuggling-in-nodejs.md) |
| 1238709 | HTTP Request Smuggling | medium | $250 | [HTTP Request Smuggling due to accepting space before colon](1238709-http-request-smuggling-due-to-accepting-space-before-colon.md) |
| 800140 | Uncontrolled Resource Consumption | critical | $250 | [Malformed HTTP/2 SETTINGS frame leads to reachable assert](800140-malformed-http-2-settings-frame-leads-to-reachable-assert.md) |
| 799072 | Uncontrolled Resource Consumption | low | $250 | [Slowloris, body parsing](799072-slowloris-body-parsing.md) |
| 868834 | Uncontrolled Resource Consumption | critical | $250 | [Denial of Service by resource exhaustion CWE-400 due to unfinished HTTP/1.1 requests](868834-denial-of-service-by-resource-exhaustion-cwe-400-due-to-unfi.md) |
| 1238099 | HTTP Request Smuggling | medium | $250 | [HTTP Request Smuggling due to ignoring chunk extensions](1238099-http-request-smuggling-due-to-ignoring-chunk-extensions.md) |
| 784186 | Memory Corruption - Generic | high | $250 | [napi_get_value_string_X allow various kinds of memory corruption](784186-napi-get-value-string-x-allow-various-kinds-of-memory-corrup.md) |
| 1033107 | Uncontrolled Resource Consumption | high | $250 | [DNS Max Responses for DOS](1033107-dns-max-responses-for-dos.md) |
| 1278254 | Improper Certificate Validation | low | $150 | [Built-in TLS module unexpectedly treats "rejectUnauthorized: undefined" as "rejectUnauthorized: false", disabling all certificate validation](1278254-built-in-tls-module-unexpectedly-treats-rejectunauthorized-u.md) |
| 922597 | HTTP Request Smuggling | high | $0 | [HTTP Request Smuggling due to CR-to-Hyphen conversion](922597-http-request-smuggling-due-to-cr-to-hyphen-conversion.md) |
| 2054283 | HTTP Request Smuggling | medium | $0 | [Improper HTTP header block termination in llhttp](2054283-improper-http-header-block-termination-in-llhttp.md) |
| 735748 | HTTP Request Smuggling | critical | $0 | [HTTP request smuggling using malformed Transfer-Encoding header](735748-http-request-smuggling-using-malformed-transfer-encoding-hea.md) |
| 3473882 | Uncontrolled Resource Consumption | medium | $0 | [TLS PSK/ALPN Callback Exceptions Bypass Error Handlers, Causing DoS and FD Leak](3473882-tls-psk-alpn-callback-exceptions-bypass-error-handlers-causi.md) |
| 2319584 | Uncontrolled Resource Consumption | high | $0 | ["Assertion failed" in node::http2::Http2Session::~Http2Session() leads to HTTP/2 server crash](2319584-assertion-failed-in-node-http2-http2session-http2session-lea.md) |
| 3556769 | Incomplete fix for CVE-2026-21637: loadSNI() in _tls_wrap.js lacks try/catch leading to Remote DoS | high | $0 | [Incomplete fix for CVE-2026-21637: loadSNI() in _tls_wrap.js lacks try/catch leading to Remote DoS](3556769-incomplete-fix-for-cve-2026-21637-loadsni-in-tls-wrap-js-lac.md) |
| 3083428 | Memory Corruption - Generic | low | $0 | [Corrupted pointer in node::fs::ReadFileUtf8(const FunctionCallbackInfo<Value>& args) when args[0] is a string.](3083428-corrupted-pointer-in-node-fs-readfileutf8-const-functioncall.md) |
| 2307225 | Path Traversal | medium | $0 | [Path traversal by drive name in Windows environment](2307225-path-traversal-by-drive-name-in-windows-environment.md) |
| 3302484 | CWE-195 in ExternalMemoryAccounter::Increase() | n/a | $0 | [CWE-195 in ExternalMemoryAccounter::Increase()](3302484-cwe-195-in-externalmemoryaccounter-increase.md) |
| 3131758 | Cryptographic Issues - Generic | high | $0 | [HashDoS in V8](3131758-hashdos-in-v8.md) |
| 3465156 | Server-Side Request Forgery (SSRF) | medium | $0 | [Node.js permission model bypass via unchecked Unix Domain Socket connections (UDS)](3465156-node-js-permission-model-bypass-via-unchecked-unix-domain-so.md) |
| 3723248 | HTTP Request Smuggling | medium | $0 | [HTTP Request Smuggling via Connection: close<TAB> in Node.js llhttp parser](3723248-http-request-smuggling-via-connection-close-tab-in-node-js-l.md) |
| 409943 | HTTP Response Splitting | medium | $0 | [Http request splitting](409943-http-request-splitting.md) |
| 3736889 | NULL Pointer Dereference | high | $0 | [NULL pointer dereference in node:sqlite DatabaseSync#applyChangeset() via malformed SQLite changeset](3736889-null-pointer-dereference-in-node-sqlite-databasesync-applych.md) |
| 2084280 | Privilege Escalation | medium | $0 | [WASI sandbox escape via symlink](2084280-wasi-sandbox-escape-via-symlink.md) |
| 3405778 | Improper Initialization | high | $0 | [Timeout-based race conditions make Uint8Array/Buffer.alloc non-zerofilled](3405778-timeout-based-race-conditions-make-uint8array-buffer-alloc-n.md) |
| 2575105 | Improper Access Control - Generic | high | $0 | [Worker permission bypass via InternalWorker leak in diagnostics](2575105-worker-permission-bypass-via-internalworker-leak-in-diagnost.md) |
| 3781015 | Uncontrolled Resource Consumption | high | $0 | [ Incomplete Fix for CVE-2026-21637: OCSPRequest and resumeSession Events Crash Node.js TLS Server via Unhandled Synchronous Exceptions](3781015-incomplete-fix-for-cve-2026-21637-ocsprequest-and-resumesess.md) |
| 3546390 | Reachable Assertion | medium | $0 | [Assertion error in node_url.cc via malformed URL format leads to Node.js crash](3546390-assertion-error-in-node-url-cc-via-malformed-url-format-lead.md) |
| 3255707 | Path Traversal | high | $0 | [Windows Device Names Still Allow Path Traversal in UNC Paths After CVE-2025-27210 Fix](3255707-windows-device-names-still-allow-path-traversal-in-unc-paths.md) |
| 3812439 | Exploiting Incorrectly Configured SSL/TLS | medium | $0 | [HTTPS Agent TLS session reuse skips hostname verification across identity policies (incomplete fix of CVE-2026-48934)](3812439-https-agent-tls-session-reuse-skips-hostname-verification-ac.md) |
| 2817648 | Cryptographic Issues - Generic | high | $0 | [Improper error handling in async cryptographic operations crashes process](2817648-improper-error-handling-in-async-cryptographic-operations-cr.md) |
| 2218653 | Path Traversal | high | $0 | [Path traversal by monkey-patching Buffer internals](2218653-path-traversal-by-monkey-patching-buffer-internals.md) |
| 3815767 | Improper Access Control - Generic | low | $0 | [Permission Model bypass: process.report writes (and overwrites) files outside --allow-fs-write paths](3815767-permission-model-bypass-process-report-writes-and-overwrites.md) |
| 3456295 | Improper Handling of Exceptional Conditions | medium | $0 | [Uncatchable "Maximum call stack size exceeded" error on Node.js via async_hooks leads to process crashes bypassing error handlers](3456295-uncatchable-maximum-call-stack-size-exceeded-error-on-node-j.md) |
| 3160912 | Path Traversal | high | $0 | [Windows Device Names (CON, PRN, AUX) Bypass Path Traversal Protection in path.normalize()](3160912-windows-device-names-con-prn-aux-bypass-path-traversal-prote.md) |
| 2079103 | Privilege Escalation | low | $0 | [Permission model improperly processes UNC paths](2079103-permission-model-improperly-processes-unc-paths.md) |
| 340580 | Man-in-the-Middle | n/a | $0 | [registry.nodejs.org Subdomain Takeover](340580-registry-nodejs-org-subdomain-takeover.md) |
| 3357723 | Uncontrolled Resource Consumption | medium | $0 | [Memory leak that enables remote Denial of Service against applications processing TLS client certificates](3357723-memory-leak-that-enables-remote-denial-of-service-against-ap.md) |
| 3417819 | Violation of Secure Design Principles | high | $0 | [FS Permissions Bypass](3417819-fs-permissions-bypass.md) |
| 3390084 | Improper Access Control - Generic | low | $0 | [fs.futimes() Bypasses Read-Only Permission Model](3390084-fs-futimes-bypasses-read-only-permission-model.md) |
| 3761342 | Improper Access Control - Generic | high | $0 | [Permission Model: --allow-fs-read/--allow-fs-write radix-tree prefix-boundary over-grant](3761342-permission-model-allow-fs-read-allow-fs-write-radix-tree-pre.md) |
| 3658225 | Uncontrolled Resource Consumption | medium | $0 | [HTTP/2 sessions never clean up after GOAWAY on invalid protocol errors](3658225-http-2-sessions-never-clean-up-after-goaway-on-invalid-proto.md) |
| 3752489 | Time-of-check Time-of-use (TOCTOU) Race Condition | high | $0 | [Memory Corruption via TOCTOU Race in SharedArrayBuffer UTF-8 Decode (`StringBytes::Encode`)](3752489-memory-corruption-via-toctou-race-in-sharedarraybuffer-utf-8.md) |
| 3648681 | HTTP Request Smuggling | medium | $0 | [Improper Input Validation — HTTP Response Parser Unconditionally Accepts Bare CR in Status Line](3648681-improper-input-validation-http-response-parser-unconditional.md) |
| 4038287 | Improper Certificate Validation | high | $0 | [TLS certificate hostname bypass when the IP is written fullwidth digits](4038287-tls-certificate-hostname-bypass-when-the-ip-is-written-fullw.md) |
| 3692858 | Improper Access Control - Generic | low | $0 | [Permission Model Bypass via `process.report.writeReport()` Path Misvalidation](3692858-permission-model-bypass-via-process-report-writereport-path.md) |
| 811502 | Man-in-the-Middle | high | $0 | [Node.js: TLS session reuse can lead to hostname verification bypass](811502-node-js-tls-session-reuse-can-lead-to-hostname-verification.md) |
| 4110110 | Use After Free | high | $0 | [HTTP/2 stream teardown can send freed response memory to the peer](4110110-http-2-stream-teardown-can-send-freed-response-memory-to-the.md) |
| 2284065 | Uncontrolled Resource Consumption | medium | $0 | [Denial of Service by resource exhaustion in fetch() brotli decoding](2284065-denial-of-service-by-resource-exhaustion-in-fetch-brotli-dec.md) |
| 988103 | Use After Free | high | $0 | [Node.js: use-after-free in TLSWrap](988103-node-js-use-after-free-in-tlswrap.md) |
| 3908163 | Improper Certificate Validation | medium | $0 | [HTTPS Agent reuses TLS authentication state across distinct secureContext policies](3908163-https-agent-reuses-tls-authentication-state-across-distinct.md) |
| 3456148 | Unbounded decompression chain in HTTP responses on Node.js Fetch API via Content-Encoding leads to resource exhaustion | n/a | $0 | [Unbounded decompression chain in HTTP responses on Node.js Fetch API via Content-Encoding leads to resource exhaustion](3456148-unbounded-decompression-chain-in-http-responses-on-node-js-f.md) |
| 4006744 | Improper Certificate Validation | high | $0 | [TLS certificate hostname bypass when the host loosely resolves to an IP address](4006744-tls-certificate-hostname-bypass-when-the-host-loosely-resolv.md) |
| 3816840 | Improper Authentication - Generic | medium | $0 | [HTTPS Agent PFX object-array key collision allows mTLS client identity reuse across different per-request certificates](3816840-https-agent-pfx-object-array-key-collision-allows-mtls-clien.md) |
| 3463949 | Missing Required Cryptographic Step | high | $0 | [Missing AES-GCM Authentication Tag Validation and Improper Deprecation Handling](3463949-missing-aes-gcm-authentication-tag-validation-and-improper-d.md) |
| 2913312 | Use of Insufficiently Random Values | medium | $0 | [Usage of unsafe random function in undici for choosing boundary](2913312-usage-of-unsafe-random-function-in-undici-for-choosing-bound.md) |
| 2170226 | Privilege Escalation | high | $0 | [setuid() does not drop all privileges due to io_uring](2170226-setuid-does-not-drop-all-privileges-due-to-io-uring.md) |
| 2237545 | Privilege Escalation | high | $0 | [Code injection and privilege escalation through Linux capabilities](2237545-code-injection-and-privilege-escalation-through-linux-capabi.md) |
| 3824331 | NULL Pointer Dereference | medium | $0 | [Null Dereference in X509ToObject](3824331-null-dereference-in-x509toobject.md) |
| 3560402 | Uncontrolled Resource Consumption | high | $0 | [Denial of Service via `__proto__` header name in `req.headersDistinct` (Uncaught `TypeError` crashes Node.js process)](3560402-denial-of-service-via-proto-header-name-in-req-headersdistin.md) |
| 1763817 | Array Index Underflow | medium | $0 | [Take over subdomain undici.nodejs.org.cdn.cloudflare.net](1763817-take-over-subdomain-undici-nodejs-org-cdn-cloudflare-net.md) |
| 3838601 | Improper Access Control - Generic | low | $0 | [Permission Model Bypass: `trace_events.createTracing().enable()` Writes Trace Logs Outside `--allow-fs-write`](3838601-permission-model-bypass-trace-events-createtracing-enable-wr.md) |
| 2260337 | Privilege Escalation | n/a | $0 | [Permissions can be bypassed via arbitrary code execution through abusing libuv signal pipes](2260337-permissions-can-be-bypassed-via-arbitrary-code-execution-thr.md) |
| 2461831 | Command Injection - Generic | high | $0 | [Bypass incomplete fix of CVE-2024-27980](2461831-bypass-incomplete-fix-of-cve-2024-27980.md) |
| 2472071 | Improper Access Control - Generic | low | $0 | [fs.fchown/fchmod bypasses permission model](2472071-fs-fchown-fchmod-bypasses-permission-model.md) |
| 2257156 | Improper Access Control - Generic | medium | $0 | [Improper handling of wildcards in --allow-fs-read and --allow-fs-write](2257156-improper-handling-of-wildcards-in-allow-fs-read-and-allow-fs.md) |
| 2259914 | Path Traversal | high | $0 | [Multiple permission model bypasses due to improper path traversal sequence sanitization](2259914-multiple-permission-model-bypasses-due-to-improper-path-trav.md) |
| 3511792 | Cryptographic Issues - Generic | medium | $0 | [HashDoS in V8](3511792-hashdos-in-v8.md) |
| 4038342 | Improper Access Control - Generic | high | $0 | [dns.resolve truncates names containing NUL char](4038342-dns-resolve-truncates-names-containing-nul-char.md) |
| 3688064 | Improper Handling of Unicode Encoding | high | $0 | [Node.js unicode dot separator handling can lead to tls wildcard-depth authentication bypass due to resolver and verifier hostname normalization mismat](3688064-node-js-unicode-dot-separator-handling-can-lead-to-tls-wildc.md) |
| 2145862 | Privilege Escalation | low | $0 | [fs.lstat bypasses permission model](2145862-fs-lstat-bypasses-permission-model.md) |
| 2092749 | Improper Access Control - Generic | medium | $0 | [Bypass network import restriction via data URL](2092749-bypass-network-import-restriction-via-data-url.md) |
| 2237099 | HTTP Request Smuggling | medium | $0 | [HTTP Request Smuggling via Content Length Obfuscation](2237099-http-request-smuggling-via-content-length-obfuscation.md) |
| 2352957 | Information Disclosure | low | $0 | [Proxy-Authorization header is not cleared in cross-domain redirect in undici](2352957-proxy-authorization-header-is-not-cleared-in-cross-domain-re.md) |
| 3833629 | Use After Free | high | $0 | [Re-entrant `nghttp2_session_mem_send()` during `nghttp2_session_mem_recv()` causes heap-use-after-free in Node.js HTTP/2](3833629-re-entrant-nghttp2-session-mem-send-during-nghttp2-session-m.md) |
| 3564941 | HTTP Request Smuggling | low | $0 | [HTTP Request Smuggling via Silent Header Truncation in Node.js HTTP Parser](3564941-http-request-smuggling-via-silent-header-truncation-in-node.md) |
| 3533945 | Cryptographic Issues - Generic | medium | $0 | [Timing side-channel in HMAC verification via memcmp() in crypto_hmac.cc leads to potential MAC forgery](3533945-timing-side-channel-in-hmac-verification-via-memcmp-in-crypt.md) |
| 2269177 | Use of a Broken or Risky Cryptographic Algorithm | medium | $0 | [Node.js is vulnerable to the Marvin Attack (timing variant of the Bleichenbacher attack against PKCS#1 v1.5 padding)](2269177-node-js-is-vulnerable-to-the-marvin-attack-timing-variant-of.md) |
| 1632921 | Improper Access Control - Generic | high | $0 | [DNS rebinding in --inspect (insufficient fix of CVE-2022-32212 affecting macOS devices)](1632921-dns-rebinding-in-inspect-insufficient-fix-of-cve-2022-32212.md) |
| 1431042 | Modification of Assumed-Immutable Data (MAID) | low | $0 | [Prototype pollution via console.table properties](1431042-prototype-pollution-via-console-table-properties.md) |
| 3838675 | Improper Access Control - Generic | low | $0 | [Permission Model bypass with fs.realpathSync](3838675-permission-model-bypass-with-fs-realpathsync.md) |
| 4038361 | Time-of-check Time-of-use (TOCTOU) Race Condition | medium | $0 | [Keep-alive socket process a response that was written before the request was sent](4038361-keep-alive-socket-process-a-response-that-was-written-before.md) |
| 3480841 | Information Disclosure | low | $0 | [Permission Model Bypass in realpathSync.native Allows File Existence Disclosure](3480841-permission-model-bypass-in-realpathsync-native-allows-file-e.md) |
| 746733 | Improper Certificate Validation | critical | $0 | [Remotely trigger an assertion on a TLS server with a malformed certificate string](746733-remotely-trigger-an-assertion-on-a-tls-server-with-a-malform.md) |
| 3962304 | Improper Certificate Validation | medium | $0 | [Improper certificate validation for non-canonical IPv4 hostnames allows DNS SANs to authenticate IP endpoints](3962304-improper-certificate-validation-for-non-canonical-ipv4-hostn.md) |
| 3760016 | Integer Overflow | high | $0 | [Node.js WebCrypto AES Integer Overflow Leads to Remote Process Abort (DoS)](3760016-node-js-webcrypto-aes-integer-overflow-leads-to-remote-proce.md) |
| 3817602 | OS Command Injection | high | $0 | [Node --run POSIX positional argument escaping allows shell command injection](3817602-node-run-posix-positional-argument-escaping-allows-shell-com.md) |
| 2841362 | Uncontrolled Resource Consumption | medium | $0 | [GOAWAY HTTP/2 frames cause memory leak outside heap](2841362-goaway-http-2-frames-cause-memory-leak-outside-heap.md) |
| 2233486 | Uncontrolled Resource Consumption | high | $0 | [http: Reading unprocessed HTTP request with unbounded chunk extension allows DoS attacks](2233486-http-reading-unprocessed-http-request-with-unbounded-chunk-e.md) |
| 3857258 | Uncontrolled Resource Consumption | medium | $0 | [Reachable assertion in node:zlib sync API crashes the entire process via spoofed TypedArray byteLength (all 11 *Sync functions affected)](3857258-reachable-assertion-in-node-zlib-sync-api-crashes-the-entire.md) |
| 3795657 | Uncontrolled Resource Consumption | medium | $0 | [dns.resolveAny() Aborts the Node.js Process When a DNS Response Contains More Than 256 A Records](3795657-dns-resolveany-aborts-the-node-js-process-when-a-dns-respons.md) |
| 3846922 | Uncontrolled Resource Consumption | high | $0 | [HTTP/2 retained header blocks evade maxSessionMemory and enable remote memory exhaustion](3846922-http-2-retained-header-blocks-evade-maxsessionmemory-and-ena.md) |
| 1631350 | Path Traversal | medium | $0 | [Off-by-slash vulnerability in nodejs.org and iojs.org](1631350-off-by-slash-vulnerability-in-nodejs-org-and-iojs-org.md) |
| 3795900 | Time-of-check Time-of-use (TOCTOU) Race Condition | medium | $0 | [node:sqlite SQLTagStore Iterator Replay Lets Attacker Re-Execute Victim-Bound Writes Indefinitely](3795900-node-sqlite-sqltagstore-iterator-replay-lets-attacker-re-exe.md) |
| 3582376 | Time-of-check Time-of-use (TOCTOU) Race Condition | low | $0 | [HTTP Response Queue Poisoning via TOCTOU Race Condition in `http.Agent`](3582376-http-response-queue-poisoning-via-toctou-race-condition-in-h.md) |
| 2377760 | Violation of Secure Design Principles | n/a | $0 | [fetch with integrity option is too lax when algorithm is specified but hash value is in incorrect](2377760-fetch-with-integrity-option-is-too-lax-when-algorithm-is-spe.md) |
| 1820955 | CRLF Injection | medium | $0 | [CRLF Injection in Nodejs ‘undici’ via host](1820955-crlf-injection-in-nodejs-undici-via-host.md) |
| 1690000 | Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG) | high | $0 | [Weak randomness in WebCrypto keygen](1690000-weak-randomness-in-webcrypto-keygen.md) |
| 730779 | Improper Input Validation | high | $0 | [HTTP header values do not have trailing OWS trimmed](730779-http-header-values-do-not-have-trailing-ows-trimmed.md) |
| 395845 | Cross-site Scripting (XSS) - Generic | medium | $0 | [url.parse() hostname spoofing via javascript: URIs](395845-url-parse-hostname-spoofing-via-javascript-uris.md) |
| 3559715 | Improper Access Control - Generic | medium | $0 | [Node.js Permission Model bypass: UDS server bind/listen works without `--allow-net`](3559715-node-js-permission-model-bypass-uds-server-bind-listen-works.md) |
| 1211160 | Privilege Escalation | medium | $0 | [Node Installer Local Privilege Escalation ](1211160-node-installer-local-privilege-escalation.md) |
| 2408074 | Insufficiently Protected Credentials | low | $0 | [Proxy-Authorization header not cleared on cross-origin redirect in undici.request](2408074-proxy-authorization-header-not-cleared-on-cross-origin-redir.md) |
| 2092852 | Path Traversal | high | $0 | [Permission model improperly protects against path traversal](2092852-permission-model-improperly-protects-against-path-traversal.md) |
| 1574078 | OS Command Injection | high | $0 | [DNS rebinding in --inspect (again) via invalid IP addresses ](1574078-dns-rebinding-in-inspect-again-via-invalid-ip-addresses.md) |
| 1524692 | HTTP Request Smuggling | medium | $0 | [HTTP Request Smuggling Due To Improper Delimiting of Header Fields](1524692-http-request-smuggling-due-to-improper-delimiting-of-header.md) |
| 589739 | Uncontrolled Resource Consumption | high | $0 | [Multiple HTTP/2 DOS Issues](589739-multiple-http-2-dos-issues.md) |
| 3618831 | Improper Access Control - Generic | low | $0 | [Unix domain socket server bypasses --permission network restrictions (incomplete CVE-2026-21636 fix)](3618831-unix-domain-socket-server-bypasses-permission-network-restri.md) |
| 2051257 | Path Traversal | high | $0 | [process.binding() can bypass the permission model through path traversal](2051257-process-binding-can-bypass-the-permission-model-through-path.md) |
| 2051224 | Improper Access Control - Generic | low | $0 | [fs.statfs bypasses Permission Model](2051224-fs-statfs-bypasses-permission-model.md) |
| 1960870 | Privilege Escalation | high | $0 | [Permissions policies can be bypassed via Module._load.](1960870-permissions-policies-can-be-bypassed-via-module-load.md) |
| 1877919 | Privilege Escalation | high | $0 | [The use of __proto__ in process.mainModule.__proto__.require() bypasses the permission system in Node v19.6.1](1877919-the-use-of-proto-in-process-mainmodule-proto-require-bypasse.md) |
| 2001873 | HTTP Request Smuggling | medium | $0 | [HTTP Request Smuggling via Empty headers separated by CR](2001873-http-request-smuggling-via-empty-headers-separated-by-cr.md) |
| 365968 | Array Index Underflow | critical | $0 | [Your page has 2 blocking CSS resources. This causes a delay in rendering your page.](365968-your-page-has-2-blocking-css-resources-this-causes-a-delay-i.md) |
| 3656869 | Improper Access Control - Generic | medium | $0 | [Uppercase sni context matching can lead to mtls authorization bypass due to case-sensitive hostname matching](3656869-uppercase-sni-context-matching-can-lead-to-mtls-authorizatio.md) |
| 3449392 | Improper Access Control - Generic | low | $0 | [CVE-2024-36137 Patch Bypass - FileHandle.chmod/chown](3449392-cve-2024-36137-patch-bypass-filehandle-chmod-chown.md) |
| 3531737 | Missing Release of Memory after Effective Lifetime | medium | $0 | [Memory leak in Node.js HTTP/2 server via WINDOW_UPDATE on stream 0 leads to resource exhaustion](3531737-memory-leak-in-node-js-http-2-server-via-window-update-on-st.md) |
| 2199818 | Path Traversal | high | $0 | [Path traversal through path stored in Uint8Array](2199818-path-traversal-through-path-stored-in-uint8array.md) |
| 1946470 | Privilege Escalation | medium | $0 | [Dependency Policy Bypass via process.binding](1946470-dependency-policy-bypass-via-process-binding.md) |
| 1927480 | Inconsistency Between Implementation and Documented Design | medium | $0 | [DiffieHellman doesn't generate keys after setting a key](1927480-diffiehellman-doesn-t-generate-keys-after-setting-a-key.md) |
| 1747642 | Privilege Escalation | high | $0 | [Permissions policies can be bypassed via process.mainModule](1747642-permissions-policies-can-be-bypassed-via-process-mainmodule.md) |
| 1524555 | HTTP Request Smuggling | medium | $0 | [HTTP Request Smuggling Due to Flawed Parsing of Transfer-Encoding ](1524555-http-request-smuggling-due-to-flawed-parsing-of-transfer-enc.md) |
| 1501679 | HTTP Request Smuggling | medium | $0 | [HTTP Request Smuggling Due to Incorrect Parsing of Multi-line Transfer-Encoding](1501679-http-request-smuggling-due-to-incorrect-parsing-of-multi-lin.md) |
| 3996423 | Improper Access Control - Generic | low | $0 | [Permission Model filesystem over-grant via wildcard radix lookup](3996423-permission-model-filesystem-over-grant-via-wildcard-radix-lo.md) |
| 2094235 | Insufficient Verification of Data Authenticity | medium | $0 | [Integrity checks according to policies can be circumvented](2094235-integrity-checks-according-to-policies-can-be-circumvented.md) |
| 1962701 | Improper Access Control - Generic | high | $0 | [Process-based permissions can be bypassed with the "inspector" module.  ](1962701-process-based-permissions-can-be-bypassed-with-the-inspector.md) |
| 1966492 | Improper Access Control - Generic | medium | $0 | [fs.openAsBlob() bypasses permission system](1966492-fs-openasblob-bypasses-permission-system.md) |
| 1675191 | HTTP Request Smuggling | medium | $0 | [HTTP Request Smuggling Due to Incorrect Parsing of Header Fields](1675191-http-request-smuggling-due-to-incorrect-parsing-of-header-fi.md) |
| 1665156 | HTTP Request Smuggling | medium | $0 | [HTTP Request Smuggling Due to Incorrect Parsing of Multi-line Transfer-Encoding (improper fix for CVE-2022-32215)](1665156-http-request-smuggling-due-to-incorrect-parsing-of-multi-lin.md) |
| 335533 | Memory Corruption - Generic | high | $0 | [HTTP/2 Denial of Service Vulnerability](335533-http-2-denial-of-service-vulnerability.md) |
| 4107681 | Classic Buffer Overflow | high | $0 | [Node.js Brotli decoder out-of-bounds write permits remote code execution](4107681-node-js-brotli-decoder-out-of-bounds-write-permits-remote-co.md) |
| 3649802 | Exploiting Incorrectly Configured SSL/TLS | medium | $0 | [TLS host identity verification bypass via session reuse with different servername leads to unauthorized connections](3649802-tls-host-identity-verification-bypass-via-session-reuse-with.md) |
| 1961655 | Privilege Escalation | medium | $0 | [Renaming/aliasing relative symbolic links potentially redirects them to supposedly inaccessible locations](1961655-renaming-aliasing-relative-symbolic-links-potentially-redire.md) |
| 1952978 | Path Traversal | high | $0 | [Filesystem experimental permissions policy does not handle path traversal cases.](1952978-filesystem-experimental-permissions-policy-does-not-handle-p.md) |
| 1966499 | Improper Access Control - Generic | medium | $0 | [fs module's file watching is not restricted by --allow-fs-read](1966499-fs-module-s-file-watching-is-not-restricted-by-allow-fs-read.md) |
| 1808596 | Cryptographic Issues - Generic | medium | $0 | [Multiple OpenSSL error handling issues in nodejs crypto library](1808596-multiple-openssl-error-handling-issues-in-nodejs-crypto-libr.md) |
| 1630336 | HTTP Request Smuggling | medium | $0 | [CVE-2022-32213 bypass via obs-fold mechanic](1630336-cve-2022-32213-bypass-via-obs-fold-mechanic.md) |
| 1209681 | Buffer Over-read | medium | $0 | [OOB read in libuv](1209681-oob-read-in-libuv.md) |
| 415329 | Command Injection - Generic | medium | $0 | [Pull Request #12949 - Security Implications without CVE assignment](415329-pull-request-12949-security-implications-without-cve-assignm.md) |
| 3625987 | Incorrect Default Permissions | low | $0 | [Permission Model bypass via FileHandle.utimes() in the promises API](3625987-permission-model-bypass-via-filehandle-utimes-in-the-promise.md) |
| 3720313 | Privacy Violation | medium | $0 | [Proxy credentials leaked in ERR_PROXY_TUNNEL error message](3720313-proxy-credentials-leaked-in-err-proxy-tunnel-error-message.md) |
| 3676863 | Uncontrolled Resource Consumption | medium | $0 | [Unbounded memory growth in `node:http2` clients via attacker-controlled ORIGIN frames](3676863-unbounded-memory-growth-in-node-http2-clients-via-attacker-c.md) |
| 3656716 | Improper Access Control - Generic | medium | $0 | [Embedded-nul hostnames can lead to silent authority rebinding due to c-string truncation in resolver bindings](3656716-embedded-nul-hostnames-can-lead-to-silent-authority-rebindin.md) |
| 2037887 | Path Traversal | low | $0 | [fs.mkdtemp() and fs.mkdtempSync() are missing getValidatedPath() checks.](2037887-fs-mkdtemp-and-fs-mkdtempsync-are-missing-getvalidatedpath-c.md) |
| 2038134 | Path Traversal | high | $0 | [Permission model bypass by specifying a path traversal sequence in a buffer, ](2038134-permission-model-bypass-by-specifying-a-path-traversal-seque.md) |
| 1623175 | Cryptographic Issues - Generic | medium | $0 | [Node 18 reads openssl.cnf from /home/iojs/build/... upon startup.](1623175-node-18-reads-openssl-cnf-from-home-iojs-build-upon-startup.md) |
| 1954535 | Privilege Escalation | medium | $0 | [OpenSSL engines can be used to bypass and/or disable the permission model](1954535-openssl-engines-can-be-used-to-bypass-and-or-disable-the-per.md) |
| 1625036 | Insecure loading of ICU data through ICU_DATA environment variable | low | $0 | [Insecure loading of ICU data through ICU_DATA environment variable](1625036-insecure-loading-of-icu-data-through-icu-data-environment-va.md) |
| 1710652 | OS Command Injection | medium | $0 | [DNS rebinding in --inspect via invalid octal IP address](1710652-dns-rebinding-in-inspect-via-invalid-octal-ip-address.md) |
| 1583680 | Improper Certificate Validation | high | $0 | [Undici does not use CONNECT or otherwise validate upstream HTTPS certificates when using a proxy](1583680-undici-does-not-use-connect-or-otherwise-validate-upstream-h.md) |
| 1178337 | Improper Null Termination | high | $0 | [Improper handling of untypical characters in domain names](1178337-improper-handling-of-untypical-characters-in-domain-names.md) |
| 1141623 | Use of Inherently Dangerous Function | critical | $0 | [Unexpected input validation of octal literals in nodejs v15.12.0 and below returns defined values for all undefined octal literals.](1141623-unexpected-input-validation-of-octal-literals-in-nodejs-v15.md) |
| 965914 | Classic Buffer Overflow | medium | $0 | [`fs.realpath.native` on darwin may cause buffer overflow](965914-fs-realpath-native-on-darwin-may-cause-buffer-overflow.md) |
| 335608 | NULL Pointer Dereference | critical | $0 | [Denial of Service: nghttp2 use of uninitialized pointer](335608-denial-of-service-nghttp2-use-of-uninitialized-pointer.md) |
| 1784449 | Uncontrolled Resource Consumption | low | $0 | [Regular Expression Denial of Service in Headers](1784449-regular-expression-denial-of-service-in-headers.md) |
| 1695596 | Cryptographic Issues - Generic | medium | $0 | [Node 18 reads openssl.cnf from /home/iojs/build/... upon startup on MacOS](1695596-node-18-reads-openssl-cnf-from-home-iojs-build-upon-startup.md) |
| 1043360 | Uncontrolled Resource Consumption | critical | $0 | [HTTP2 'unknownProtocol' cause Denial of Service by resource exhaustion](1043360-http2-unknownprotocol-cause-denial-of-service-by-resource-ex.md) |
| 878181 | Code Injection | n/a | $0 | [Child process environment injection via prototype pollution](878181-child-process-environment-injection-via-prototype-pollution.md) |
| 629879 | Code Injection | n/a | $0 | [loader.js is not secure](629879-loader-js-is-not-secure.md) |
| 453513 | Uncontrolled Resource Consumption | medium | $0 | [Fix for CVE-2018-12122 can be bypassed via keep-alive requests](453513-fix-for-cve-2018-12122-can-be-bypassed-via-keep-alive-reques.md) |
| 335495 | Heap Overflow | high | $0 | [Out of order TLS handshake / application data messages lead to segmentation fault](335495-out-of-order-tls-handshake-application-data-messages-lead-to.md) |
| 678487 | Hostname spoofing | n/a | $0 | [Hostname spoofing](678487-hostname-spoofing.md) |
| 2043807 | Privilege Escalation | medium | $0 | [Policy-restricted modules can escalate to higher privileges by impersonating other modules in a policy list using module.constructor.createRequire()](2043807-policy-restricted-modules-can-escalate-to-higher-privileges.md) |
| 1884159 | Uncontrolled Resource Consumption | medium | $0 | [node.js process aborts when processing x509 certs with invalid public key information](1884159-node-js-process-aborts-when-processing-x509-certs-with-inval.md) |
| 1429694 | Improper Following of a Certificate's Chain of Trust | medium | $0 | [Node.js Certificate Verification Bypass via String Injection](1429694-node-js-certificate-verification-bypass-via-string-injection.md) |
| 446662 | Uncontrolled Resource Consumption | low | $0 | [Node.js HTTP/2 Large Settings Frame DoS](446662-node-js-http-2-large-settings-frame-dos.md) |
| 340053 | Use After Free | n/a | $0 | [Use After Free in crypto.randomFill](340053-use-after-free-in-crypto-randomfill.md) |
| 771596 | CRLF Injection | medium | $0 | [CRLF Injection in legacy url API (url.parse().hostname)](771596-crlf-injection-in-legacy-url-api-url-parse-hostname.md) |
| 536954 | Improper Null Termination | high | $0 | [Vulnerability in http-parser & embedded NULL header handling](536954-vulnerability-in-http-parser-embedded-null-header-handling.md) |
| 676710 | Uncontrolled Resource Consumption | n/a | $0 | [Http response is not ended although underlying socket is already destroyed](676710-http-response-is-not-ended-although-underlying-socket-is-alr.md) |
