# Monero GUI Automatic Update Check Bypasses Configured SOCKS/Tor Proxy and Leaks User's Real IP Address

- Program: Monero
- Weakness / temuan: **Information Disclosure**
- Severity: medium
- State: resolved
- Bounty: $0.00
- Upvotes: 0
- Submitted: 2026-08-22
- Disclosed: 2026-10-08
- Report: https://hackerone.com/reports/3960681

## Writeup

## Summary

monero-gui lets a privacy-conscious user route all of the wallet's network traffic
through a SOCKS5 proxy (e.g. a local Tor daemon) via **Settings → "Connect through a
proxy" / SOCKS address**, or the `--socks5-proxy` CLI flag. Every network client in
the GUI is wired to honor that setting — the fiat-price fetcher, the `WalletManager`,
the wallet↔daemon connection, and even the update-*binary* `Downloader` all bind
`proxyAddress: persistentSettings.getProxyAddress()`.

**One sibling path does not.** The automatic update check (enabled by default; fired
on start-up and hourly) calls `Updater::fetchSignedHash()`, which constructs a bare
`const Network network;` with **no proxy** and fetches
`https://web.getmonero.org/downloads/hashes.txt` and `…/hashes.txt.sig` over a
**direct clear-net connection**. `net::http::client::set_proxy("")` explicitly installs
a `direct_connect{}` connector. When an update is available (i.e. whenever the user is
on a not-quite-latest version — the common case shortly after any release), this
discloses the user's **real public IP address** to `web.getmonero.org` (and to any
on-path network observer), tagged by the Monero-specific request path, **defeating the
app-level proxy/Tor anonymity the user explicitly configured**.

The project treats exactly this as a serious bug: its `NetworkAccessBlockingFactory`
black-holes *all* QML-layer network egress with the comment *"[the] UI does not directly
cause network requests for any reason. These are always a potentially deanonymizing
bug."* The un-proxied epee request in `Updater` slips past both that QML blocker (it is
an epee client, not a `QNetworkAccessManager`) and the user's SOCKS setting.

Confirmed with a local, loopback-only PoC that drives the real `net::http::client`
class (see Steps To Reproduce): an empty proxy connects **directly** to the target,
while a configured SOCKS proxy routes through the proxy.

## Releases Affected

- monero-project/monero-gui, `master` @ `ed9ea9c3c897b0d2bfd9e1b18ffbb2ea15dda41a`
  (current tip, 2026-08-06), all desktop platforms.
- Present since commit `ea25b71c` ("updater: fetch signed hashes from getmonero.org,
  verify downloads"), which introduced the getmonero.org HTTP hash-fetch. The proxy
  plumbing was subsequently added to the other network paths (fiat, wallet, downloader)
  but never to `Updater`.

## Steps To Reproduce

## A. Confirm the code path (source)

1. `Updater::fetchSignedHash` uses a proxy-less `Network` (`src/qt/updater.cpp:57-59`).
2. An empty proxy string makes the epee client take the `direct_connect{}` branch
   (`monero/src/net/http.cpp:42-45`).
3. Every sibling network client is constructed from a non-empty `getProxyAddress()`
   (see Supporting Material) and therefore takes the `socks::connector` branch.
4. The check runs by default: `checkForUpdates` defaults `true` (`main.qml:1518`);
   `updatesTimer` is `triggeredOnStart` + hourly and its `running` condition never
   consults the proxy setting (`main.qml:2294-2301`).

## B. Dynamic validation (local, loopback only — getmonero.org is never contacted)

`poc_proxy_bypass.cpp` links the **real** `net::http::client` (the exact class the GUI
`Network` uses) and calls `set_proxy()` + `invoke()` against a local target. Two local
listeners stand in for the SOCKS proxy (`127.0.0.1:9999`) and for getmonero.org
(`127.0.0.1:8888`).

Build (against the monero-gui `monero` submodule + Boost/OpenSSL):

```
g++ -std=c++17 poc_proxy_bypass.cpp \
    monero/src/net/{http,socks,socks_connect,parse,error,i2p_address,tor_address}.cpp \
    monero/src/common/error.cpp \
    monero/contrib/epee/src/{net_helper,byte_stream,byte_slice,buffer,portable_storage,\
      parserse_base_utils,abstract_http_client,http_auth,http_base,net_ssl,connection_basic,\
      network_throttle,network_throttle-detail,mlog,string_tools,net_parse_helpers,\
      net_utils_base,wipeable_string,mlocker,misc_language,hex,int-util,file_io_utils}.cpp \
    memwipe.o external/easylogging++/easylogging++.cc \
    -I contrib/epee/include -I src -I external/easylogging++ \
    -lboost_thread -lboost_chrono -lboost_filesystem -lboost_regex -lssl -lcrypto -lpthread -o poc
```

Run (start the two local listeners first):

```
./poc ""                127.0.0.1 8888   # Updater-style: empty proxy
./poc "127.0.0.1:9999"  127.0.0.1 8888   # sibling-style: SOCKS proxy set
```

Observed (from the listeners):

```
### TEST1 empty-proxy (Updater-style) ###
[harness] proxy='' target=127.0.0.1:8888 -> invoking
[TARGET-getmonero-standin] CONNECTION from ('127.0.0.1', 46080) on port 8888   <-- DIRECT to target

### TEST2 socks-proxy 127.0.0.1:9999 (sibling-style) ###
[harness] proxy='127.0.0.1:9999' target=127.0.0.1:8888 -> invoking
[SOCKS-proxy] CONNECTION from ('127.0.0.1', 46092) on port 9999                 <-- routed via SOCKS; never direct to :8888
```

TEST1 (the `Updater` configuration) connects **directly** to the getmonero.org
stand-in, proving the proxy is bypassed; TEST2 (every sibling client's configuration)
connects only to the SOCKS proxy. No traffic was ever sent to a non-loopback host.

## Supporting Material/References

- `src/qt/updater.cpp:49-73` — `Updater::fetchSignedHash`: `const Network network;`
  (empty proxy) fetching `web.getmonero.org/downloads/hashes.txt` and `.sig`.
- `src/qt/network.cpp:97-101,186-194` — `Network` default ctor (empty `m_proxyAddress`)
  and `newClient()` → `set_proxy(m_proxyAddress)`.
- `monero/src/net/http.cpp:40-65` — `net::http::client::set_proxy`: `address.empty()`
  ⇒ `set_connector(epee::net_utils::direct_connect{})` (direct); else `socks::connector`.
- `monero/contrib/epee/include/net/net_helper.h:64-68,107` — `direct_connect` is a plain
  `boost::asio` TCP connect, and is also the default connector.
- `src/qt/updater.h:35-64` — `Updater` has no proxy member.
- `src/libwalletqt/WalletManager.cpp` (checkUpdatesAsync) — `Updater().fetchSignedHash(...)`
  is constructed inline with no proxy.
- Sibling clients that *do* apply the proxy:
  - `main.qml:2497-2500` fiat-price `network` → `proxyAddress: getProxyAddress()`
  - `main.qml:2502-2505` `walletManager` → `proxyAddress: getProxyAddress()`
  - `main.qml:367` wallet daemon conn → `currentWallet.proxyAddress = Qt.binding(getWalletProxyAddress)`
  - `components/UpdateDialog.qml:202` update-binary `downloader` → `proxyAddress: getProxyAddress()`
- `main.qml:1518` `checkForUpdates` defaults `true`; `main.qml:2294-2301` `updatesTimer`
  (hourly, `triggeredOnStart`, independent of proxy).
- `main.qml:1530-1539` `getProxyAddress()` returns the real SOCKS address when enabled;
  `pages/settings/SettingsLayout.qml:272-295` the user-facing proxy toggle/address.
- `src/qt/NetworkAccessBlockingFactory.h:33-58` — project intent: all UI-originated
  network requests are "potentially deanonymizing" and are blocked.
- PoC: `poc_proxy_bypass.cpp`, `validation_output.txt` (attached).

## Root Cause

`Updater::fetchSignedHash` (`src/qt/updater.cpp`):

```cpp
const Network network;                                   // m_proxyAddress == ""  (no proxy)
std::string hashesTxt    = network.get(hashesTxtUrl);    // https://web.getmonero.org/downloads/hashes.txt
std::string hashesTxtSig = network.get(hashesTxtSigUrl); // …/hashes.txt.sig
```

`Network::newClient` (`src/qt/network.cpp`) forwards that empty string:

```cpp
std::shared_ptr<abstract_http_client> Network::newClient() const {
    std::shared_ptr<abstract_http_client> client(new net::http::client());
    if (!client->set_proxy(m_proxyAddress.toStdString()))   // "" here
        throw std::runtime_error("failed to set proxy address");
    return client;
}
```

and `net::http::client::set_proxy` (`monero/src/net/http.cpp`) turns an empty string
into a **direct** connector — this branch is the leak:

```cpp
bool client::set_proxy(const std::string &address) {
    if (address.empty())
        set_connector(epee::net_utils::direct_connect{});   // <-- direct TCP egress of real IP
    else
        set_connector(net::socks::connector{ ... });        // <-- routed via SOCKS
    disconnect();
    return true;
}
```

The deviation: every other GUI network client is created from a non-empty
`getProxyAddress()` (see Supporting Material) and so takes the `socks::connector`
branch; `Updater` alone takes `direct_connect{}`. The update *binary* is downloaded via
the proxy, but the update *hash* that authorizes it is fetched in the clear — an
asymmetry that marks this as an oversight rather than a deliberate policy.

## Suggested remediation / patch

Give `Updater` a proxy and thread the app's `getProxyAddress()` into it, exactly as the
`Downloader` already does:

```diff
--- a/src/qt/updater.h
+++ b/src/qt/updater.h
@@
-    Updater();
+    explicit Updater(QString proxyAddress = {});
@@
 private:
+    QString m_proxyAddress;
     std::vector<openpgp::public_key_block> m_maintainers;
--- a/src/qt/updater.cpp
+++ b/src/qt/updater.cpp
@@ Updater::fetchSignedHash
-    const Network network;
+    Network network;
+    network.setProperty("proxyAddress", m_proxyAddress);   // Network exposes proxyAddress as a Q_PROPERTY
```

and construct it with the live proxy in `WalletManager::checkUpdatesAsync`:

```diff
-    const QString signedHash = Updater().fetchSignedHash(binaryFilename, hashFromDns, signers).toHex();
+    const QString signedHash = Updater(proxyAddress()).fetchSignedHash(binaryFilename, hashFromDns, signers).toHex();
```

Alternatively, skip the entire update check while the proxy is enabled-but-unapplied,
or surface an explicit warning.

## Why this may be downgraded / a false positive

- Users who torify at the OS/network level (Tails uses system Tor; Whonix; a
  transparent-proxy gateway) are **not** affected — the direct socket is still caught by
  system routing. The leak specifically affects users relying on monero-gui's *in-app*
  SOCKS setting without system-level torification.
- The DNS portion of the update check (`Monero::WalletManager::checkUpdates`, in monero
  core, not the GUI) may already leak similar metadata to the resolver; this report is
  scoped to the GUI's clear-net HTTP fetch, which is clearly attributable to monero-gui.
- Should be checked against prior monero-gui privacy reports for duplicates before filing.

## AI assistance disclosure

Found with AI assistance (Claude) for source navigation, analysis, and PoC authoring.
Every file:line claim was verified by reading the source at monero-gui `ed9ea9c3c8`
(and its `monero` submodule), and the leak was **dynamically confirmed locally** by
compiling and running the real `net::http::client` against loopback listeners
(`poc_proxy_bypass.cpp` / `validation_output.txt`); no request was ever sent to
`web.getmonero.org` or any external host.

## Impact

Un-proxied clear-net egress that **defeats the wallet's own app-level anonymity
control**. A user who configures monero-gui's SOCKS/Tor proxy specifically to hide that
they run Monero still has their real IP address disclosed to `web.getmonero.org`
(Monero project infrastructure / CDN) and to any on-path observer, on start-up and
hourly, whenever an update is available. The request path (`/downloads/hashes.txt`) is
Monero-specific, so it doubles as an identifier that the IP runs the Monero GUI. This is
a privacy / deanonymization leak — the class the project's own
`NetworkAccessBlockingFactory` exists to prevent — not a memory-safety or fund-loss bug.
Because the fetched hashes are still PGP-verified (dual maintainer) and DNS-cross-checked
afterward, a network attacker on this connection can only **observe** (leak) or **drop**
(DoS the update check), not forge an update. Realistic severity: **Low–Medium**
(metadata/anonymity), conditioned on update-available + in-app-proxy-enabled + default
update check.
