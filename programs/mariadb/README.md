# MariaDB

Disclosed reports: **62**

| ID | Temuan | Severity | Bounty | Writeup |
| --- | --- | --- | ---: | --- |
| 1419213 | Remote File Inclusion | medium | $0 | [Grafana LFI on https://grafana.mariadb.org](1419213-grafana-lfi-on-https-grafana-mariadb-org.md) |
| 3788482 | Stack Overflow | critical | $0 | [Stack Buffer Overflow in mariadb-dump quote_name() Allows Malicious Server to Execute Arbitrary Code on Client](3788482-stack-buffer-overflow-in-mariadb-dump-quote-name-allows-mali.md) |
| 3897914 | Out-of-bounds Read | high | $0 | [Out-of-bounds read in MariaDB .frm parsing enables RCE via vtable hijacking](3897914-out-of-bounds-read-in-mariadb-frm-parsing-enables-rce-via-vt.md) |
| 3876430 | Improper Access Control - Generic | high | $0 | [MariaDB GRANT PROXY permits unauthorized authentication changes and administrator account takeover](3876430-mariadb-grant-proxy-permits-unauthorized-authentication-chan.md) |
| 3896671 | Out-of-bounds Read | n/a | $0 | [Connector/C Out-of-bounds read in `unpack_fields()` from short metadata field](3896671-connector-c-out-of-bounds-read-in-unpack-fields-from-short-m.md) |
| 3872239 | Uncontrolled Resource Consumption | medium | $0 | [Connector/J: malicious server crashes client JVM via unbounded result-set field-count allocation in ClientMessage.readPacket](3872239-connector-j-malicious-server-crashes-client-jvm-via-unbounde.md) |
| 3678395 | Path Traversal | high | $0 | [Path Traversal in mbstream Extract](3678395-path-traversal-in-mbstream-extract.md) |
| 3849007 | SQL Injection | n/a | $0 | [MariaDB CLI Utility Issues](3849007-mariadb-cli-utility-issues.md) |
| 3867363 | Uncontrolled Resource Consumption | medium | $0 | [MariaDB HandlerSocket Improper Request Field-Count Validation Causes Server Crash](3867363-mariadb-handlersocket-improper-request-field-count-validatio.md) |
| 3766217 | Stack Overflow | medium | $0 | [libmariadb ( mariadb-connector-c ): stack overflow via server-controlled field->length in prepared-statement codec](3766217-libmariadb-mariadb-connector-c-stack-overflow-via-server-con.md) |
| 3782405 | Stack Overflow | n/a | $0 | [Stack Buffer-Overflow in MariaDB Charset_collation_map_st::insert_or_replace()](3782405-stack-buffer-overflow-in-mariadb-charset-collation-map-st-in.md) |
| 397402 | Server-Side Request Forgery (SSRF) | medium | $0 | [SSRF on jira.mariadb.org](397402-ssrf-on-jira-mariadb-org.md) |
| 690330 | Uncontrolled Resource Consumption | low | $0 | [scripts loader (denial of service) vulnerability](690330-scripts-loader-denial-of-service-vulnerability.md) |
| 3908943 | Improper Access Control - Generic | high | $0 | [DROP PACKAGE leaves PACKAGE BODY grant in mysql.procs_priv causing privilege escalation](3908943-drop-package-leaves-package-body-grant-in-mysql-procs-priv-c.md) |
| 3896507 | Server crash (stack-overflow DoS) via unbounded recursion in MariaDB WKB GEOMETRYCOLLECTION parser | medium | $0 | [Server crash (stack-overflow DoS) via unbounded recursion in MariaDB WKB GEOMETRYCOLLECTION parser](3896507-server-crash-stack-overflow-dos-via-unbounded-recursion-in-m.md) |
| 3769676 | Stack Overflow | medium | $0 | [Stack Overflow DoS in ST_GeomFromGeoJSON Allows Any Authenticated User to Crash the Entire Server](3769676-stack-overflow-dos-in-st-geomfromgeojson-allows-any-authenti.md) |
| 3910393 | Stack Overflow | n/a | $0 | [Stack Buffer Overflow in MariaDB CONNECT storage engine when reading DOUBLE columns from TABLE_TYPE=DOS tables](3910393-stack-buffer-overflow-in-mariadb-connect-storage-engine-when.md) |
| 3867358 | Uncontrolled Resource Consumption | medium | $0 | [MariaDB Low-Privilege User Can Exhaust Memory Through a Formatting Function and Crash the Service](3867358-mariadb-low-privilege-user-can-exhaust-memory-through-a-form.md) |
| 3771139 | Buffer Over-read | n/a | $0 | [Heap Memory Disclosure via Integer Underflow in Item_func_json_arrayagg::cut_max_length in MariaDB Server](3771139-heap-memory-disclosure-via-integer-underflow-in-item-func-js.md) |
| 476257 | CRLF Injection | medium | $0 | [CRLF injection at https://mariadb.org/.](476257-crlf-injection-at-https-mariadb-org.md) |
| 392701 | Cryptographic Issues - Generic | low | $0 | [Vulnerability Report - Missing Certificate Authority Authorization rule](392701-vulnerability-report-missing-certificate-authority-authoriza.md) |
| 3781201 | Integer Underflow | medium | $0 | [Pre-authentication `size_t` integer underflow → out-of-bounds read / server crash in MariaDB `caching_sha2_password` (auth_mysql_sha2) via an RSA-OAEP](3781201-pre-authentication-size-t-integer-underflow-out-of-bounds-re.md) |
| 3836021 | Improper Access Control - Generic | high | $0 | [Missing FILE-privilege enforcement in CONNECT file UDFs allows server-side file read and write](3836021-missing-file-privilege-enforcement-in-connect-file-udfs-allo.md) |
| 3856148 | Use After Free | critical | $0 | [Low-privilege RCE in MariaDB: SYS_REFCURSOR cursor-array use-after-free chained with an ST_Area heap over-read](3856148-low-privilege-rce-in-mariadb-sys-refcursor-cursor-array-use.md) |
| 3896617 | Improper Certificate Validation | n/a | $0 | [Connector/C TLS auth-switch bypass exposes plaintext password on hostname verification failure](3896617-connector-c-tls-auth-switch-bypass-exposes-plaintext-passwor.md) |
| 3771144 | Use After Free | n/a | $0 | [Use-After-Free in BTREE Index Traversal via Stale key_version in heap_update() in MariaDB Server](3771144-use-after-free-in-btree-index-traversal-via-stale-key-versio.md) |
| 3771147 | Classic Buffer Overflow | n/a | $0 | [Stack Buffer Overflow via Crafted keyseg->start/ keyseg->length in .MYI File (MariaDB MyISAM)](3771147-stack-buffer-overflow-via-crafted-keyseg-start-keyseg-length.md) |
| 386160 | Uncontrolled Resource Consumption | low | $0 | [xmlrpc.php on mariadb.org can lead to DDOS and brute force attacks](386160-xmlrpc-php-on-mariadb-org-can-lead-to-ddos-and-brute-force-a.md) |
| 3897588 | Incorrect Calculation of Buffer Size | n/a | $0 | [KILL authorization trusts the presented login name instead of the authenticated anonymous account](3897588-kill-authorization-trusts-the-presented-login-name-instead-o.md) |
| 1019891 | Business Logic Errors | high | $0 | [Named pipe connection inteception](1019891-named-pipe-connection-inteception.md) |
| 639473 | Cryptographic Issues - Generic | medium | $0 | [Ubuntu/Debian installation method allows key poisoning and code execution for network attacker](639473-ubuntu-debian-installation-method-allows-key-poisoning-and-c.md) |
| 457009 | Improper Access Control - Generic | medium | $0 | [Github wiki is editable by anyone](457009-github-wiki-is-editable-by-anyone.md) |
| 392761 | Cross-Site Request Forgery (CSRF) | low | $0 | [vulnerable to Cross-site Request Forgery \| Jira](392761-vulnerable-to-cross-site-request-forgery-jira.md) |
| 3849025 | DATA / INDEX DIRECTORY Abuse | n/a | $0 | [DATA / INDEX DIRECTORY Abuse](3849025-data-index-directory-abuse.md) |
| 3889667 | Improper Authentication - Generic | medium | $0 | [ACL cache collision lets a role inherit privileges from a same-named socket user](3889667-acl-cache-collision-lets-a-role-inherit-privileges-from-a-sa.md) |
| 1176174 | Git Config | medium | $0 | [Git Config](1176174-git-config.md) |
| 514421 | Cryptographic Issues - Generic | low | $0 | [smtp service vulnerable to POODLE SSLv3](514421-smtp-service-vulnerable-to-poodle-sslv3.md) |
| 3920633 | Out-of-bounds Read | medium | $0 | [Connector/ODBC: SqlwcsOctetLen sizes UTF-16 with a byte-oriented helper, reading past the caller's buffer and sending client memory to the server](3920633-connector-odbc-sqlwcsoctetlen-sizes-utf-16-with-a-byte-orien.md) |
| 3871977 | Memory Corruption - Generic | medium | $0 | [Connector/ODBC: malicious server's long version string wraps size_t PrefixLen via negative _snprintf return, causing heap out-of-bounds write](3871977-connector-odbc-malicious-server-s-long-version-string-wraps.md) |
| 481512 | CRLF Injection | medium | $0 | [CRLF injection on https://buildbot.mariadb.org](481512-crlf-injection-on-https-buildbot-mariadb-org.md) |
| 3896684 | Out-of-bounds Read | n/a | $0 | [Connector/C Out-of-bounds read from unterminated GSSAPI SPN in `parse_server_packet()`](3896684-connector-c-out-of-bounds-read-from-unterminated-gssapi-spn.md) |
| 3920647 | Out-of-bounds Read | medium | $0 | [Connector/ODBC: MADB_Stmt::ArrayOffset is not reset when an exception unwinds out of MADB_StmtExecute, so the next paramset reads out of bounds](3920647-connector-odbc-madb-stmt-arrayoffset-is-not-reset-when-an-ex.md) |
| 3872248 | Out-of-bounds Read | medium | $0 | [Connector/C++: heap out-of-bounds read when malicious server field length exceeds declared column length in binary result path](3872248-connector-c-heap-out-of-bounds-read-when-malicious-server-fi.md) |
| 3871740 | Uncontrolled Resource Consumption | medium | $0 | [r2dbc-mariadb Parsec auth: server-controlled PBKDF2 iteration count causes CPU-exhaustion DoS ( regression from b7766de )](3871740-r2dbc-mariadb-parsec-auth-server-controlled-pbkdf2-iteration.md) |
| 3880451 | Privilege escalation via user controlled usernames / roles and views | n/a | $0 | [Privilege escalation via user controlled usernames / roles and views](3880451-privilege-escalation-via-user-controlled-usernames-roles-and.md) |
| 3915935 | Use After Free | high | $0 | [Heap Use-After-Free in Materialized_cursor::open via SYS_REFCURSOR Array Reallocation](3915935-heap-use-after-free-in-materialized-cursor-open-via-sys-refc.md) |
| 3909248 | Heap Overflow | medium | $0 | [MariaDB: heap buffer overflow in ha_tina::chain_append() lets a low-privileged user crash the server via CSV row deletion](3909248-mariadb-heap-buffer-overflow-in-ha-tina-chain-append-lets-a.md) |
| 490997 | CRLF Injection | medium | $0 | [[downloads.mariadb.org] CRLF injection in case of encoded query mark](490997-downloads-mariadb-org-crlf-injection-in-case-of-encoded-quer.md) |
| 394861 | Privilege Escalation | medium | $0 | [Incorrect Permission Assignment for Critical Resource](394861-incorrect-permission-assignment-for-critical-resource.md) |
| 3848978 | SQL Injection | n/a | $0 | [`SHOW [CREATE\|GRANTS] ...` / `mariadb-dump` Unescaped SQL Generation](3848978-show-create-grants-mariadb-dump-unescaped-sql-generation.md) |
| 3849051 | #mysql50# legacy alias / internal table collisions | n/a | $0 | [#mysql50# legacy alias / internal table collisions](3849051-mysql50-legacy-alias-internal-table-collisions.md) |
| 3849040 | #mysql50# legacy alias / stale table cache identity mismatch | n/a | $0 | [#mysql50# legacy alias / stale table cache identity mismatch](3849040-mysql50-legacy-alias-stale-table-cache-identity-mismatch.md) |
| 3890329 | SQL Injection | medium | $0 | [Connector/C++ ignores allowMultiQueries and injects savepoint names into SQL](3890329-connector-c-ignores-allowmultiqueries-and-injects-savepoint.md) |
| 637840 | Path Traversal | medium | $0 | [Path traversal in command line client](637840-path-traversal-in-command-line-client.md) |
| 775504 | Information Disclosure | medium | $0 | [Exposed debug.log file leads to information disclosure](775504-exposed-debug-log-file-leads-to-information-disclosure.md) |
| 3920629 | Information Disclosure | medium | $0 | [r2dbc-mariadb: server message accepted with no command in flight desynchronises the connection and serves one user's rows to another](3920629-r2dbc-mariadb-server-message-accepted-with-no-command-in-fli.md) |
| 3891337 | Type Confusion | medium | $0 | [Connector/ODBC SQLGetDescRec treats descriptor handle as statement handle, heap OOB write on every call](3891337-connector-odbc-sqlgetdescrec-treats-descriptor-handle-as-sta.md) |
| 3891319 | Stack Overflow | medium | $0 | [Stack buffer overflow in 9 of 10 Connector/ODBC catalog functions via unbounded name](3891319-stack-buffer-overflow-in-9-of-10-connector-odbc-catalog-func.md) |
| 3890289 | SQL Injection | medium | $0 | [Connector/C++ string escaper re-escapes its own output, enabling SQL injection](3890289-connector-c-string-escaper-re-escapes-its-own-output-enablin.md) |
| 1369288 | Path Traversal | medium | $0 | [Path Traversal CVE-2021-26086 CVE-2021-26085](1369288-path-traversal-cve-2021-26086-cve-2021-26085.md) |
| 3891779 | SQL Injection | medium | $0 | [Connector/ODBC injects unquoted column names into positioned DELETE and UPDATE via MADB_DynStrGetWhere](3891779-connector-odbc-injects-unquoted-column-names-into-positioned.md) |
| 3890352 | Uncontrolled Resource Consumption | medium | $0 | [Connector/C++ aborts client process on server session-tracking packet via std::stoi](3890352-connector-c-aborts-client-process-on-server-session-tracking.md) |
