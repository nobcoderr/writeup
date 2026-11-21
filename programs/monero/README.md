# Monero

Disclosed reports: **83**

| ID | Temuan | Severity | Bounty | Writeup |
| --- | --- | --- | ---: | --- |
| 3307874 | Uncontrolled Resource Consumption | critical | $0 | [Critical Deadlock Vulnerability in Monero RPC Leading to Complete Node Paralysis](3307874-critical-deadlock-vulnerability-in-monero-rpc-leading-to-com.md) |
| 2858802 | low-level p2p ping + tcp flooding leads to a remote crash in monerod | critical | $0 | [low-level p2p ping + tcp flooding leads to a remote crash in monerod](2858802-low-level-p2p-ping-tcp-flooding-leads-to-a-remote-crash-in-m.md) |
| 2425873 | Improper Access Control - Generic | n/a | $0 | [[Monero wallet RPC] File precreation to file ownership and credentials leak](2425873-monero-wallet-rpc-file-precreation-to-file-ownership-and-cre.md) |
| 3620006 | Improper Authentication - Generic | high | $0 | [Wallet RPC Restricted-Mode Policy Bypass](3620006-wallet-rpc-restricted-mode-policy-bypass.md) |
| 3738727 | Improper Access Control - Generic | low | $0 | [Restricted RPC leaks alternative block hashes via /get_alt_blocks_hashes](3738727-restricted-rpc-leaks-alternative-block-hashes-via-get-alt-bl.md) |
| 2338094 | Uncontrolled Resource Consumption | medium | $0 | [RPC service DOS](2338094-rpc-service-dos.md) |
| 1981441 | Uncontrolled Resource Consumption | low | $0 | [Dynamic fee algorithm doesn't check for zero fee](1981441-dynamic-fee-algorithm-doesn-t-check-for-zero-fee.md) |
| 3819475 | Monero GUI OpenAlias DNSSEC-invalid resolution still writes spoofable address into recipient field | medium | $0 | [Monero GUI OpenAlias DNSSEC-invalid resolution still writes spoofable address into recipient field](3819475-monero-gui-openalias-dnssec-invalid-resolution-still-writes.md) |
| 3693636 | NULL Pointer Dereference | high | $0 | [wallet-rpc crash via malformed /gettransactions response (empty txs → vector::front() in check_tx_key / check_tx_proof)](3693636-wallet-rpc-crash-via-malformed-gettransactions-response-empt.md) |
| 357858 | Code Injection | high | $0 | [forum.getmonero.org Shell upload](357858-forum-getmonero-org-shell-upload.md) |
| 3699522 | Business Logic Errors | medium | $0 | [`check_reserve_proof` counts duplicate entries: one output can inflate `total`](3699522-check-reserve-proof-counts-duplicate-entries-one-output-can.md) |
| 3619409 | Improper Access Control - Generic | high | $0 | [Windows installer grants low-privileged users write access to executable P2Pool directory, enabling local code execution](3619409-windows-installer-grants-low-privileged-users-write-access-t.md) |
| 3601469 | Improper Authentication - Generic | high | $0 | [Restricted RPC Policy Bypass on ZMQ JSON-RPC Allows Unauthenticated Remote Admin Actions](3601469-restricted-rpc-policy-bypass-on-zmq-json-rpc-allows-unauthen.md) |
| 3185083 | Privacy Violation | n/a | $0 | [Connection Count Bug in Monero Node Enables Outbound Peer Reset Attack](3185083-connection-count-bug-in-monero-node-enables-outbound-peer-re.md) |
| 3698862 | Missing Required Cryptographic Step | medium | $0 | [ `check_reserve_proof` sums RingCT ECDH amounts without checking the output commitment](3698862-check-reserve-proof-sums-ringct-ecdh-amounts-without-checkin.md) |
| 3683934 | sign_multisig crashes monero-wallet-rpc on a malformed but decryptable multisig txset | high | $0 | [sign_multisig crashes monero-wallet-rpc on a malformed but decryptable multisig txset](3683934-sign-multisig-crashes-monero-wallet-rpc-on-a-malformed-but-d.md) |
| 3621588 | Business Logic Errors | high | $0 | [Authenticated `unsigned_txset` change spoof lets a malicious hot wallet steal cold-signer change](3621588-authenticated-unsigned-txset-change-spoof-lets-a-malicious-h.md) |
| 3686283 | Information Disclosure | medium | $0 | [View-only offline transaction creation bypasses the long-payment-ID privacy block](3686283-view-only-offline-transaction-creation-bypasses-the-long-pay.md) |
| 3679471 | Code Injection | medium | $0 | [HTML Injection in Transaction Confirmation Dialog via Address Book Description Enables UI Spoofing Before Fund Transfer](3679471-html-injection-in-transaction-confirmation-dialog-via-addres.md) |
| 3621606 | CRLF Injection | medium | $0 | [ZMQ RPC Log Injection and Untrusted Payload Persistence](3621606-zmq-rpc-log-injection-and-untrusted-payload-persistence.md) |
| 506595 | Uncontrolled Resource Consumption | high | $0 | [CryptoNote: remote node DoS](506595-cryptonote-remote-node-dos.md) |
| 265161 | Business Logic Errors | none | $0 | [Monero Website & Kovri on your policy are returning 404 not found.](265161-monero-website-kovri-on-your-policy-are-returning-404-not-fo.md) |
| 3700036 | Missing Required Cryptographic Step | medium | $0 | [SpendProofV1 txid-substitution: get_spend_proof/check_spend_proof do not verify returned transaction hash](3700036-spendproofv1-txid-substitution-get-spend-proof-check-spend-p.md) |
| 1379707 | Uncontrolled Resource Consumption | high | $0 | [RPC call crashes node](1379707-rpc-call-crashes-node.md) |
| 817245 | Man-in-the-Middle | medium | $0 | [Hardware Wallets Do Not Check Unlock TIme](817245-hardware-wallets-do-not-check-unlock-time.md) |
| 3683886 | Restricted ZMQ RPC bypasses HTTP restricted-mode resource checks | medium | $0 | [Restricted ZMQ RPC bypasses HTTP restricted-mode resource checks](3683886-restricted-zmq-rpc-bypasses-http-restricted-mode-resource-ch.md) |
| 3240792 | Integer Overflow | n/a | $0 | [Reported RPC Overflow](3240792-reported-rpc-overflow.md) |
| 876530 | Uncontrolled Resource Consumption | medium | $0 | [Remote node DOS](876530-remote-node-dos.md) |
| 2912194 | Uncontrolled Resource Consumption | high | $0 | [Remote memory exhaustion in Epee RPC stack under zero Receive Window](2912194-remote-memory-exhaustion-in-epee-rpc-stack-under-zero-receiv.md) |
| 3816330 | Uncontrolled Resource Consumption | high | $0 | [Monero IPv6 /128 tracking bypasses per-IP limit, enables remote OOM](3816330-monero-ipv6-128-tracking-bypasses-per-ip-limit-enables-remot.md) |
| 3241102 | Uncontrolled Resource Consumption | n/a | $0 | [Reported Denial of Service](3241102-reported-denial-of-service.md) |
| 2315026 | Transactions in invalid blocks are kept in tx-pool without undergoing certain checks. | n/a | $0 | [Transactions in invalid blocks are kept in tx-pool without undergoing certain checks.](2315026-transactions-in-invalid-blocks-are-kept-in-tx-pool-without-u.md) |
| 2693786 | A peer can remotely fill the pending block queue to an extremely high size, with blocks that will never leave the queue. | n/a | $0 | [A peer can remotely fill the pending block queue to an extremely high size, with blocks that will never leave the queue.](2693786-a-peer-can-remotely-fill-the-pending-block-queue-to-an-extre.md) |
| 3681690 | ZMQ get_output_distribution duplicate amount DoS | medium | $0 | [ZMQ get_output_distribution duplicate amount DoS](3681690-zmq-get-output-distribution-duplicate-amount-dos.md) |
| 2677306 | Uncontrolled Resource Consumption | n/a | $0 | [Spamming highly nested JSON RPC requests cause node to disconnect from p2p network](2677306-spamming-highly-nested-json-rpc-requests-cause-node-to-disco.md) |
| 3719670 | Information Disclosure | medium | $0 | [`monero-wallet-rpc::rescan_spent` accepts daemon-supplied spent-status from an untrusted daemon, enabling ring-intersection attack on transactions](3719670-monero-wallet-rpc-rescan-spent-accepts-daemon-supplied-spent.md) |
| 3648638 | Business Logic Errors | medium | $0 | [monero:// deeplink parsing accepts tx_amount=(all) and can trigger send-all transaction mode](3648638-monero-deeplink-parsing-accepts-tx-amount-all-and-can-trigge.md) |
| 3687543 | Improper Access Control - Generic | low | $0 | [ `relay_tx` wallet-rpc skips `--restricted-rpc` guard and lets any caller corrupt wallet state via attacker-controlled `pending_tx`](3687543-relay-tx-wallet-rpc-skips-restricted-rpc-guard-and-lets-any.md) |
| 854726 | Business Logic Errors | high | $0 | [Unix time unlock_time values have dangerous validation rules enabling a number of exploits](854726-unix-time-unlock-time-values-have-dangerous-validation-rules.md) |
| 3723315 | Array Index Underflow | medium | $0 | [wallet-rpc describe_transfer uses real_output_in_tx_index instead of real_output: cold-wallet pre-sign review shows wrong ring member](3723315-wallet-rpc-describe-transfer-uses-real-output-in-tx-index-in.md) |
| 3547349 | Inverted ternary in peerlist_manager::filter() allows unlimited whitelist entries per host via different ports | n/a | $0 | [Inverted ternary in peerlist_manager::filter() allows unlimited whitelist entries per host via different ports](3547349-inverted-ternary-in-peerlist-manager-filter-allows-unlimited.md) |
| 379049 | Business Logic Errors | high | $0 | [Attcker can trick monero wallet into reporting it recived twice as much with alternative tx_keypubs](379049-attcker-can-trick-monero-wallet-into-reporting-it-recived-tw.md) |
| 825091 | Array Index Underflow | high | $0 | [Array Index Underflow--http rpc](825091-array-index-underflow-http-rpc.md) |
| 713321 | Exploiting Network and Timing Side-Channels to Break Monero Receiver Anonymity | medium | $0 | [Exploiting Network and Timing Side-Channels to Break Monero Receiver Anonymity](713321-exploiting-network-and-timing-side-channels-to-break-monero.md) |
| 1668258 | Improper Access Control - Generic | n/a | $0 | [Reentrancy attack in eth-monero atomic swap](1668258-reentrancy-attack-in-eth-monero-atomic-swap.md) |
| 291489 | Information Disclosure | high | $0 | [Kovri: potential buffer over-read in garlic clove handling + I2NP message creation](291489-kovri-potential-buffer-over-read-in-garlic-clove-handling-i2.md) |
| 340012 | Buffer Over-read | low | $0 | [Buffer out of bound read in miniupnpc xml parser ](340012-buffer-out-of-bound-read-in-miniupnpc-xml-parser.md) |
| 304770 | Privacy Violation | medium | $0 | [Corrupt RPC responses from remote daemon nodes can lead to transaction tracing](304770-corrupt-rpc-responses-from-remote-daemon-nodes-can-lead-to-t.md) |
| 3515557 | Business Logic Errors | medium | $0 | [Loss of multisig funds through single malicious participant's deliberate deception](3515557-loss-of-multisig-funds-through-single-malicious-participant.md) |
| 391611 | Uncontrolled Resource Consumption | high | $0 | [Malicious get_random_rct_outs.bin rpc can cause a near-infinite loop](391611-malicious-get-random-rct-outs-bin-rpc-can-cause-a-near-infin.md) |
| 265160 | TabNabbing issue (due to taget=_blank) | n/a | $0 | [TabNabbing issue (due to taget=_blank)](265160-tabnabbing-issue-due-to-taget-blank.md) |
| 630903 | Code Injection | high | $0 | [Monero Wallet Gui for Windows (Arbitrary Code Execution)](630903-monero-wallet-gui-for-windows-arbitrary-code-execution.md) |
| 462442 | Improper Access Control - Generic | high | $0 | [Unauthorized access of Monero wallet by an unprivileged process](462442-unauthorized-access-of-monero-wallet-by-an-unprivileged-proc.md) |
| 390499 | Stack Overflow | n/a | $0 | [Stack Overflow in JSON RPC Server](390499-stack-overflow-in-json-rpc-server.md) |
| 543782 | Uncontrolled Resource Consumption | n/a | $0 | [Excessive Resource Usage](543782-excessive-resource-usage.md) |
| 501585 | Resource Injection | critical | $0 | [Zero-amount miner TX + RingCT allows monero wallet to receive arbitrary amount of monero](501585-zero-amount-miner-tx-ringct-allows-monero-wallet-to-receive.md) |
| 511317 | Use After Free | low | $0 | [Potential use-after-free due to struct array_entry_t lacking an explicit copy constructor](511317-potential-use-after-free-due-to-struct-array-entry-t-lacking.md) |
| 506496 | Business Logic Errors | medium | $0 | [RingCT malformed tx prevents target from being able to sweep balance](506496-ringct-malformed-tx-prevents-target-from-being-able-to-sweep.md) |
| 416494 | Uncontrolled Resource Consumption | medium | $0 | [DoS for remote nodes using Slow Loris attack](416494-dos-for-remote-nodes-using-slow-loris-attack.md) |
| 321213 | Monero GUI not linked with /DYNAMICBASE or hardening on windows, no ASLR | n/a | $0 | [Monero GUI not linked with /DYNAMICBASE or hardening on windows, no ASLR](321213-monero-gui-not-linked-with-dynamicbase-or-hardening-on-windo.md) |
| 303390 | Cross-Site Request Forgery (CSRF) | low | $0 | [remote access to localhost daemon, can issue jsonrpc commands](303390-remote-access-to-localhost-daemon-can-issue-jsonrpc-commands.md) |
| 803028 | Unverified Password Change | low | $0 | [Monero wallet password change is confirmed when not matching](803028-monero-wallet-password-change-is-confirmed-when-not-matching.md) |
| 519120 | Uncontrolled Resource Consumption | high | $0 | [Computing hash of crafted block leads to crash in tree_hash()](519120-computing-hash-of-crafted-block-leads-to-crash-in-tree-hash.md) |
| 3686259 | Improper Certificate Validation | high | $0 | [`set_daemon` wallet-rpc silently ignores `ssl_allowed_fingerprints` → pinning bypassed, wallet↔daemon MITM](3686259-set-daemon-wallet-rpc-silently-ignores-ssl-allowed-fingerpri.md) |
| 592200 | Remote P2P DoS | critical | $0 | [Remote P2P DoS](592200-remote-p2p-dos.md) |
| 363680 | Missing Required Cryptographic Step | critical | $0 | [Constant-time comparison is not always implemented; critical areas are vulnerable to key-timing attacks](363680-constant-time-comparison-is-not-always-implemented-critical.md) |
| 361269 | Privacy Violation | low | $0 | [Trusted daemon check fails when proxied through torsocks or proxychains](361269-trusted-daemon-check-fails-when-proxied-through-torsocks-or.md) |
| 284951 | Out-of-bounds Read | low | $0 | [Out-of-bounds read when importing corrupt blockchain with monero-blockchain-import](284951-out-of-bounds-read-when-importing-corrupt-blockchain-with-mo.md) |
| 1511843 | Uncontrolled Resource Consumption | medium | $0 | [monerod JSON RPC server remote DoS](1511843-monerod-json-rpc-server-remote-dos.md) |
| 896338 | Misconfiguration in build environment allows DLL preloading attack | low | $0 | [Misconfiguration in build environment allows DLL preloading attack](896338-misconfiguration-in-build-environment-allows-dll-preloading.md) |
| 417515 | Locked_Transfer functional burning | high | $0 | [Locked_Transfer functional burning](417515-locked-transfer-functional-burning.md) |
| 481164 | Information Disclosure | medium | $0 | [Monero can leak unitialized memory](481164-monero-can-leak-unitialized-memory.md) |
| 377592 | Business Logic Errors | critical | $0 | [A bug in the Monero wallet balance can enable theft from exchanges](377592-a-bug-in-the-monero-wallet-balance-can-enable-theft-from-exc.md) |
| 592094 | Remote Daemon RPC Attack | medium | $0 | [Remote Daemon RPC Attack](592094-remote-daemon-rpc-attack.md) |
| 364904 | Business Logic Errors | high | $0 | [Misreporting of received amount by show_transfers](364904-misreporting-of-received-amount-by-show-transfers.md) |
| 344499 | Uncontrolled Resource Consumption | low | $0 | [epee will accept an arbitrary amount of leading line-breaks in an http request](344499-epee-will-accept-an-arbitrary-amount-of-leading-line-breaks.md) |
| 363714 | Uncontrolled Resource Consumption | medium | $0 | [monerod can be disabled by a well-timed TCP reset packet](363714-monerod-can-be-disabled-by-a-well-timed-tcp-reset-packet.md) |
| 766963 | Information Disclosure | low | $0 | [Potential linkage of public/private (anonymous) node addresses](766963-potential-linkage-of-public-private-anonymous-node-addresses.md) |
| 652911 | Violation of Secure Design Principles | medium | $0 | [CVE-2019-13132 - libzmq 4.1 series is vulnerable](652911-cve-2019-13132-libzmq-4-1-series-is-vulnerable.md) |
| 506498 | Uncontrolled Resource Consumption | high | $0 | [(remote) exabyte allocation via load_from_binary() (DoS)](506498-remote-exabyte-allocation-via-load-from-binary-dos.md) |
| 3749681 | Information Disclosure | low | $0 | [Background sync cache retains outgoing additional transaction secret keys](3749681-background-sync-cache-retains-outgoing-additional-transactio.md) |
| 3960681 | Information Disclosure | medium | $0 | [Monero GUI Automatic Update Check Bypasses Configured SOCKS/Tor Proxy and Leaks User's Real IP Address](3960681-monero-gui-automatic-update-check-bypasses-configured-socks.md) |
| 1437942 | Code Injection | medium | $0 | [DLL hijacking in Monero GUI for Windows 0.17.3.0 would allow an attacker to perform remote command execution](1437942-dll-hijacking-in-monero-gui-for-windows-0-17-3-0-would-allow.md) |
