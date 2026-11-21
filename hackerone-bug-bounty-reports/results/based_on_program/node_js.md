## Reports in Node.js program:

| S.No | Title | Bounty |
| ---- | ----- | ------ |
| 1 | [DNS rebinding in --inspect (insufficient fix of CVE-2018-7160)](https://hackerone.com/reports/1069487) | $500.0 |
| 2 | [Potential HTTP Request Smuggling in nodejs](https://hackerone.com/reports/1002188) | $250.0 |
| 3 | [HTTP Request Smuggling due to accepting space before colon](https://hackerone.com/reports/1238709) | $250.0 |
| 4 | [Malformed HTTP/2 SETTINGS frame leads to reachable assert](https://hackerone.com/reports/800140) | $250.0 |
| 5 | [Denial of Service by resource exhaustion CWE-400 due to unfinished HTTP/1.1 requests](https://hackerone.com/reports/868834) | $250.0 |
| 6 | [Slowloris, body parsing](https://hackerone.com/reports/799072) | $250.0 |
| 7 | [napi_get_value_string_X allow various kinds of memory corruption](https://hackerone.com/reports/784186) | $250.0 |
| 8 | [HTTP Request Smuggling due to ignoring chunk extensions](https://hackerone.com/reports/1238099) | $250.0 |
| 9 | [DNS Max Responses for DOS](https://hackerone.com/reports/1033107) | $250.0 |
| 10 | [Built-in TLS module unexpectedly treats "rejectUnauthorized: undefined" as "rejectUnauthorized: false", disabling all certificate validation](https://hackerone.com/reports/1278254) | $150.0 |
| 11 | [HTTP Request Smuggling due to CR-to-Hyphen conversion](https://hackerone.com/reports/922597) | $0 |
| 12 | [Improper HTTP header block termination in llhttp](https://hackerone.com/reports/2054283) | $0 |
| 13 | [HTTP request smuggling using malformed Transfer-Encoding header](https://hackerone.com/reports/735748) | $0 |
| 14 | [TLS PSK/ALPN Callback Exceptions Bypass Error Handlers, Causing DoS and FD Leak](https://hackerone.com/reports/3473882) | $0 |
| 15 | ["Assertion failed" in node::http2::Http2Session::~Http2Session() leads to HTTP/2 server crash](https://hackerone.com/reports/2319584) | $0 |
| 16 | [Path traversal by drive name in Windows environment](https://hackerone.com/reports/2307225) | $0 |
| 17 | [Corrupted pointer in node::fs::ReadFileUtf8(const FunctionCallbackInfo<Value>& args) when args[0] is a string.](https://hackerone.com/reports/3083428) | $0 |
| 18 | [Incomplete fix for CVE-2026-21637: loadSNI() in _tls_wrap.js lacks try/catch leading to Remote DoS](https://hackerone.com/reports/3556769) | $0 |
| 19 | [CWE-195 in ExternalMemoryAccounter::Increase()](https://hackerone.com/reports/3302484) | $0 |
| 20 | [HashDoS in V8](https://hackerone.com/reports/3131758) | $0 |
| 21 | [Node.js permission model bypass via unchecked Unix Domain Socket connections (UDS)](https://hackerone.com/reports/3465156) | $0 |
| 22 | [HTTP Request Smuggling via Connection: close<TAB> in Node.js llhttp parser](https://hackerone.com/reports/3723248) | $0 |
| 23 | [Http request splitting](https://hackerone.com/reports/409943) | $0 |
| 24 | [WASI sandbox escape via symlink](https://hackerone.com/reports/2084280) | $0 |
| 25 | [NULL pointer dereference in node:sqlite DatabaseSync#applyChangeset() via malformed SQLite changeset](https://hackerone.com/reports/3736889) | $0 |
| 26 | [Timeout-based race conditions make Uint8Array/Buffer.alloc non-zerofilled](https://hackerone.com/reports/3405778) | $0 |
| 27 | [Worker permission bypass via InternalWorker leak in diagnostics](https://hackerone.com/reports/2575105) | $0 |
| 28 | [ Incomplete Fix for CVE-2026-21637: OCSPRequest and resumeSession Events Crash Node.js TLS Server via Unhandled Synchronous Exceptions](https://hackerone.com/reports/3781015) | $0 |
| 29 | [Assertion error in node_url.cc via malformed URL format leads to Node.js crash](https://hackerone.com/reports/3546390) | $0 |
| 30 | [Windows Device Names Still Allow Path Traversal in UNC Paths After CVE-2025-27210 Fix](https://hackerone.com/reports/3255707) | $0 |
| 31 | [Improper error handling in async cryptographic operations crashes process](https://hackerone.com/reports/2817648) | $0 |
| 32 | [HTTPS Agent TLS session reuse skips hostname verification across identity policies (incomplete fix of CVE-2026-48934)](https://hackerone.com/reports/3812439) | $0 |
| 33 | [Path traversal by monkey-patching Buffer internals](https://hackerone.com/reports/2218653) | $0 |
| 34 | [registry.nodejs.org Subdomain Takeover](https://hackerone.com/reports/340580) | $0 |
| 35 | [Permission model improperly processes UNC paths](https://hackerone.com/reports/2079103) | $0 |
| 36 | [Windows Device Names (CON, PRN, AUX) Bypass Path Traversal Protection in path.normalize()](https://hackerone.com/reports/3160912) | $0 |
| 37 | [Uncatchable "Maximum call stack size exceeded" error on Node.js via async_hooks leads to process crashes bypassing error handlers](https://hackerone.com/reports/3456295) | $0 |
| 38 | [Permission Model bypass: process.report writes (and overwrites) files outside --allow-fs-write paths](https://hackerone.com/reports/3815767) | $0 |
| 39 | [fs.futimes() Bypasses Read-Only Permission Model](https://hackerone.com/reports/3390084) | $0 |
| 40 | [FS Permissions Bypass](https://hackerone.com/reports/3417819) | $0 |
| 41 | [Memory leak that enables remote Denial of Service against applications processing TLS client certificates](https://hackerone.com/reports/3357723) | $0 |
| 42 | [HTTP/2 sessions never clean up after GOAWAY on invalid protocol errors](https://hackerone.com/reports/3658225) | $0 |
| 43 | [Permission Model: --allow-fs-read/--allow-fs-write radix-tree prefix-boundary over-grant](https://hackerone.com/reports/3761342) | $0 |
| 44 | [Memory Corruption via TOCTOU Race in SharedArrayBuffer UTF-8 Decode (`StringBytes::Encode`)](https://hackerone.com/reports/3752489) | $0 |
| 45 | [Improper Input Validation — HTTP Response Parser Unconditionally Accepts Bare CR in Status Line](https://hackerone.com/reports/3648681) | $0 |
| 46 | [Node.js: TLS session reuse can lead to hostname verification bypass](https://hackerone.com/reports/811502) | $0 |
| 47 | [Permission Model Bypass via `process.report.writeReport()` Path Misvalidation](https://hackerone.com/reports/3692858) | $0 |
| 48 | [TLS certificate hostname bypass when the IP is written fullwidth digits](https://hackerone.com/reports/4038287) | $0 |
| 49 | [HTTP/2 stream teardown can send freed response memory to the peer](https://hackerone.com/reports/4110110) | $0 |
| 50 | [Node.js: use-after-free in TLSWrap](https://hackerone.com/reports/988103) | $0 |
| 51 | [Denial of Service by resource exhaustion in fetch() brotli decoding](https://hackerone.com/reports/2284065) | $0 |
| 52 | [Unbounded decompression chain in HTTP responses on Node.js Fetch API via Content-Encoding leads to resource exhaustion](https://hackerone.com/reports/3456148) | $0 |
| 53 | [HTTPS Agent reuses TLS authentication state across distinct secureContext policies](https://hackerone.com/reports/3908163) | $0 |
| 54 | [setuid() does not drop all privileges due to io_uring](https://hackerone.com/reports/2170226) | $0 |
| 55 | [Usage of unsafe random function in undici for choosing boundary](https://hackerone.com/reports/2913312) | $0 |
| 56 | [Missing AES-GCM Authentication Tag Validation and Improper Deprecation Handling](https://hackerone.com/reports/3463949) | $0 |
| 57 | [HTTPS Agent PFX object-array key collision allows mTLS client identity reuse across different per-request certificates](https://hackerone.com/reports/3816840) | $0 |
| 58 | [TLS certificate hostname bypass when the host loosely resolves to an IP address](https://hackerone.com/reports/4006744) | $0 |
| 59 | [Code injection and privilege escalation through Linux capabilities](https://hackerone.com/reports/2237545) | $0 |
| 60 | [Take over subdomain undici.nodejs.org.cdn.cloudflare.net](https://hackerone.com/reports/1763817) | $0 |
| 61 | [Denial of Service via `__proto__` header name in `req.headersDistinct` (Uncaught `TypeError` crashes Node.js process)](https://hackerone.com/reports/3560402) | $0 |
| 62 | [Null Dereference in X509ToObject](https://hackerone.com/reports/3824331) | $0 |
| 63 | [Permission Model Bypass: `trace_events.createTracing().enable()` Writes Trace Logs Outside `--allow-fs-write`](https://hackerone.com/reports/3838601) | $0 |
| 64 | [Multiple permission model bypasses due to improper path traversal sequence sanitization](https://hackerone.com/reports/2259914) | $0 |
| 65 | [Improper handling of wildcards in --allow-fs-read and --allow-fs-write](https://hackerone.com/reports/2257156) | $0 |
| 66 | [fs.fchown/fchmod bypasses permission model](https://hackerone.com/reports/2472071) | $0 |
| 67 | [Bypass incomplete fix of CVE-2024-27980](https://hackerone.com/reports/2461831) | $0 |
| 68 | [Permissions can be bypassed via arbitrary code execution through abusing libuv signal pipes](https://hackerone.com/reports/2260337) | $0 |
| 69 | [HashDoS in V8](https://hackerone.com/reports/3511792) | $0 |
| 70 | [Proxy-Authorization header is not cleared in cross-domain redirect in undici](https://hackerone.com/reports/2352957) | $0 |
| 71 | [HTTP Request Smuggling via Content Length Obfuscation](https://hackerone.com/reports/2237099) | $0 |
| 72 | [Bypass network import restriction via data URL](https://hackerone.com/reports/2092749) | $0 |
| 73 | [fs.lstat bypasses permission model](https://hackerone.com/reports/2145862) | $0 |
| 74 | [Node.js unicode dot separator handling can lead to tls wildcard-depth authentication bypass due to resolver and verifier hostname normalization mismat](https://hackerone.com/reports/3688064) | $0 |
| 75 | [dns.resolve truncates names containing NUL char](https://hackerone.com/reports/4038342) | $0 |
| 76 | [Re-entrant `nghttp2_session_mem_send()` during `nghttp2_session_mem_recv()` causes heap-use-after-free in Node.js HTTP/2](https://hackerone.com/reports/3833629) | $0 |
| 77 | [Prototype pollution via console.table properties](https://hackerone.com/reports/1431042) | $0 |
| 78 | [DNS rebinding in --inspect (insufficient fix of CVE-2022-32212 affecting macOS devices)](https://hackerone.com/reports/1632921) | $0 |
| 79 | [Node.js is vulnerable to the Marvin Attack (timing variant of the Bleichenbacher attack against PKCS#1 v1.5 padding)](https://hackerone.com/reports/2269177) | $0 |
| 80 | [Timing side-channel in HMAC verification via memcmp() in crypto_hmac.cc leads to potential MAC forgery](https://hackerone.com/reports/3533945) | $0 |
| 81 | [HTTP Request Smuggling via Silent Header Truncation in Node.js HTTP Parser](https://hackerone.com/reports/3564941) | $0 |
| 82 | [Remotely trigger an assertion on a TLS server with a malformed certificate string](https://hackerone.com/reports/746733) | $0 |
| 83 | [Permission Model Bypass in realpathSync.native Allows File Existence Disclosure](https://hackerone.com/reports/3480841) | $0 |
| 84 | [Keep-alive socket process a response that was written before the request was sent](https://hackerone.com/reports/4038361) | $0 |
| 85 | [Permission Model bypass with fs.realpathSync](https://hackerone.com/reports/3838675) | $0 |
| 86 | [http: Reading unprocessed HTTP request with unbounded chunk extension allows DoS attacks](https://hackerone.com/reports/2233486) | $0 |
| 87 | [GOAWAY HTTP/2 frames cause memory leak outside heap](https://hackerone.com/reports/2841362) | $0 |
| 88 | [Node --run POSIX positional argument escaping allows shell command injection](https://hackerone.com/reports/3817602) | $0 |
| 89 | [Node.js WebCrypto AES Integer Overflow Leads to Remote Process Abort (DoS)](https://hackerone.com/reports/3760016) | $0 |
| 90 | [Improper certificate validation for non-canonical IPv4 hostnames allows DNS SANs to authenticate IP endpoints](https://hackerone.com/reports/3962304) | $0 |
| 91 | [Off-by-slash vulnerability in nodejs.org and iojs.org](https://hackerone.com/reports/1631350) | $0 |
| 92 | [HTTP/2 retained header blocks evade maxSessionMemory and enable remote memory exhaustion](https://hackerone.com/reports/3846922) | $0 |
| 93 | [dns.resolveAny() Aborts the Node.js Process When a DNS Response Contains More Than 256 A Records](https://hackerone.com/reports/3795657) | $0 |
| 94 | [Reachable assertion in node:zlib sync API crashes the entire process via spoofed TypedArray byteLength (all 11 *Sync functions affected)](https://hackerone.com/reports/3857258) | $0 |
| 95 | [url.parse() hostname spoofing via javascript: URIs](https://hackerone.com/reports/395845) | $0 |
| 96 | [HTTP header values do not have trailing OWS trimmed](https://hackerone.com/reports/730779) | $0 |
| 97 | [Weak randomness in WebCrypto keygen](https://hackerone.com/reports/1690000) | $0 |
| 98 | [CRLF Injection in Nodejs ‘undici’ via host](https://hackerone.com/reports/1820955) | $0 |
| 99 | [fetch with integrity option is too lax when algorithm is specified but hash value is in incorrect](https://hackerone.com/reports/2377760) | $0 |
| 100 | [HTTP Response Queue Poisoning via TOCTOU Race Condition in `http.Agent`](https://hackerone.com/reports/3582376) | $0 |
| 101 | [node:sqlite SQLTagStore Iterator Replay Lets Attacker Re-Execute Victim-Bound Writes Indefinitely](https://hackerone.com/reports/3795900) | $0 |
| 102 | [Node Installer Local Privilege Escalation ](https://hackerone.com/reports/1211160) | $0 |
| 103 | [Node.js Permission Model bypass: UDS server bind/listen works without `--allow-net`](https://hackerone.com/reports/3559715) | $0 |
| 104 | [Multiple HTTP/2 DOS Issues](https://hackerone.com/reports/589739) | $0 |
| 105 | [HTTP Request Smuggling Due To Improper Delimiting of Header Fields](https://hackerone.com/reports/1524692) | $0 |
| 106 | [DNS rebinding in --inspect (again) via invalid IP addresses ](https://hackerone.com/reports/1574078) | $0 |
| 107 | [Permission model improperly protects against path traversal](https://hackerone.com/reports/2092852) | $0 |
| 108 | [Proxy-Authorization header not cleared on cross-origin redirect in undici.request](https://hackerone.com/reports/2408074) | $0 |
| 109 | [Your page has 2 blocking CSS resources. This causes a delay in rendering your page.](https://hackerone.com/reports/365968) | $0 |
| 110 | [HTTP Request Smuggling via Empty headers separated by CR](https://hackerone.com/reports/2001873) | $0 |
| 111 | [The use of __proto__ in process.mainModule.__proto__.require() bypasses the permission system in Node v19.6.1](https://hackerone.com/reports/1877919) | $0 |
| 112 | [Permissions policies can be bypassed via Module._load.](https://hackerone.com/reports/1960870) | $0 |
| 113 | [fs.statfs bypasses Permission Model](https://hackerone.com/reports/2051224) | $0 |
| 114 | [process.binding() can bypass the permission model through path traversal](https://hackerone.com/reports/2051257) | $0 |
| 115 | [Unix domain socket server bypasses --permission network restrictions (incomplete CVE-2026-21636 fix)](https://hackerone.com/reports/3618831) | $0 |
| 116 | [HTTP Request Smuggling Due to Incorrect Parsing of Multi-line Transfer-Encoding](https://hackerone.com/reports/1501679) | $0 |
| 117 | [HTTP Request Smuggling Due to Flawed Parsing of Transfer-Encoding ](https://hackerone.com/reports/1524555) | $0 |
| 118 | [Permissions policies can be bypassed via process.mainModule](https://hackerone.com/reports/1747642) | $0 |
| 119 | [DiffieHellman doesn't generate keys after setting a key](https://hackerone.com/reports/1927480) | $0 |
| 120 | [Dependency Policy Bypass via process.binding](https://hackerone.com/reports/1946470) | $0 |
| 121 | [Path traversal through path stored in Uint8Array](https://hackerone.com/reports/2199818) | $0 |
| 122 | [Memory leak in Node.js HTTP/2 server via WINDOW_UPDATE on stream 0 leads to resource exhaustion](https://hackerone.com/reports/3531737) | $0 |
| 123 | [CVE-2024-36137 Patch Bypass - FileHandle.chmod/chown](https://hackerone.com/reports/3449392) | $0 |
| 124 | [Uppercase sni context matching can lead to mtls authorization bypass due to case-sensitive hostname matching](https://hackerone.com/reports/3656869) | $0 |
| 125 | [HTTP/2 Denial of Service Vulnerability](https://hackerone.com/reports/335533) | $0 |
| 126 | [HTTP Request Smuggling Due to Incorrect Parsing of Multi-line Transfer-Encoding (improper fix for CVE-2022-32215)](https://hackerone.com/reports/1665156) | $0 |
| 127 | [HTTP Request Smuggling Due to Incorrect Parsing of Header Fields](https://hackerone.com/reports/1675191) | $0 |
| 128 | [fs.openAsBlob() bypasses permission system](https://hackerone.com/reports/1966492) | $0 |
| 129 | [Process-based permissions can be bypassed with the "inspector" module.  ](https://hackerone.com/reports/1962701) | $0 |
| 130 | [Integrity checks according to policies can be circumvented](https://hackerone.com/reports/2094235) | $0 |
| 131 | [Permission Model filesystem over-grant via wildcard radix lookup](https://hackerone.com/reports/3996423) | $0 |
| 132 | [Pull Request #12949 - Security Implications without CVE assignment](https://hackerone.com/reports/415329) | $0 |
| 133 | [OOB read in libuv](https://hackerone.com/reports/1209681) | $0 |
| 134 | [CVE-2022-32213 bypass via obs-fold mechanic](https://hackerone.com/reports/1630336) | $0 |
| 135 | [Multiple OpenSSL error handling issues in nodejs crypto library](https://hackerone.com/reports/1808596) | $0 |
| 136 | [fs module's file watching is not restricted by --allow-fs-read](https://hackerone.com/reports/1966499) | $0 |
| 137 | [Filesystem experimental permissions policy does not handle path traversal cases.](https://hackerone.com/reports/1952978) | $0 |
| 138 | [Renaming/aliasing relative symbolic links potentially redirects them to supposedly inaccessible locations](https://hackerone.com/reports/1961655) | $0 |
| 139 | [TLS host identity verification bypass via session reuse with different servername leads to unauthorized connections](https://hackerone.com/reports/3649802) | $0 |
| 140 | [Node.js Brotli decoder out-of-bounds write permits remote code execution](https://hackerone.com/reports/4107681) | $0 |
| 141 | [Denial of Service: nghttp2 use of uninitialized pointer](https://hackerone.com/reports/335608) | $0 |
| 142 | [`fs.realpath.native` on darwin may cause buffer overflow](https://hackerone.com/reports/965914) | $0 |
| 143 | [Unexpected input validation of octal literals in nodejs v15.12.0 and below returns defined values for all undefined octal literals.](https://hackerone.com/reports/1141623) | $0 |
| 144 | [Improper handling of untypical characters in domain names](https://hackerone.com/reports/1178337) | $0 |
| 145 | [Undici does not use CONNECT or otherwise validate upstream HTTPS certificates when using a proxy](https://hackerone.com/reports/1583680) | $0 |
| 146 | [DNS rebinding in --inspect via invalid octal IP address](https://hackerone.com/reports/1710652) | $0 |
| 147 | [Insecure loading of ICU data through ICU_DATA environment variable](https://hackerone.com/reports/1625036) | $0 |
| 148 | [OpenSSL engines can be used to bypass and/or disable the permission model](https://hackerone.com/reports/1954535) | $0 |
| 149 | [Node 18 reads openssl.cnf from /home/iojs/build/... upon startup.](https://hackerone.com/reports/1623175) | $0 |
| 150 | [Permission model bypass by specifying a path traversal sequence in a buffer, ](https://hackerone.com/reports/2038134) | $0 |
| 151 | [fs.mkdtemp() and fs.mkdtempSync() are missing getValidatedPath() checks.](https://hackerone.com/reports/2037887) | $0 |
| 152 | [Embedded-nul hostnames can lead to silent authority rebinding due to c-string truncation in resolver bindings](https://hackerone.com/reports/3656716) | $0 |
| 153 | [Unbounded memory growth in `node:http2` clients via attacker-controlled ORIGIN frames](https://hackerone.com/reports/3676863) | $0 |
| 154 | [Proxy credentials leaked in ERR_PROXY_TUNNEL error message](https://hackerone.com/reports/3720313) | $0 |
| 155 | [Permission Model bypass via FileHandle.utimes() in the promises API](https://hackerone.com/reports/3625987) | $0 |
| 156 | [Hostname spoofing](https://hackerone.com/reports/678487) | $0 |
| 157 | [Out of order TLS handshake / application data messages lead to segmentation fault](https://hackerone.com/reports/335495) | $0 |
| 158 | [Fix for CVE-2018-12122 can be bypassed via keep-alive requests](https://hackerone.com/reports/453513) | $0 |
| 159 | [loader.js is not secure](https://hackerone.com/reports/629879) | $0 |
| 160 | [Child process environment injection via prototype pollution](https://hackerone.com/reports/878181) | $0 |
| 161 | [HTTP2 'unknownProtocol' cause Denial of Service by resource exhaustion](https://hackerone.com/reports/1043360) | $0 |
| 162 | [Node 18 reads openssl.cnf from /home/iojs/build/... upon startup on MacOS](https://hackerone.com/reports/1695596) | $0 |
| 163 | [Regular Expression Denial of Service in Headers](https://hackerone.com/reports/1784449) | $0 |
| 164 | [CRLF Injection in legacy url API (url.parse().hostname)](https://hackerone.com/reports/771596) | $0 |
| 165 | [Use After Free in crypto.randomFill](https://hackerone.com/reports/340053) | $0 |
| 166 | [Node.js HTTP/2 Large Settings Frame DoS](https://hackerone.com/reports/446662) | $0 |
| 167 | [Node.js Certificate Verification Bypass via String Injection](https://hackerone.com/reports/1429694) | $0 |
| 168 | [node.js process aborts when processing x509 certs with invalid public key information](https://hackerone.com/reports/1884159) | $0 |
| 169 | [Policy-restricted modules can escalate to higher privileges by impersonating other modules in a policy list using module.constructor.createRequire()](https://hackerone.com/reports/2043807) | $0 |
| 170 | [Http response is not ended although underlying socket is already destroyed](https://hackerone.com/reports/676710) | $0 |
| 171 | [Vulnerability in http-parser & embedded NULL header handling](https://hackerone.com/reports/536954) | $0 |
