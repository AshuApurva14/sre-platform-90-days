# Lab 7: Build your own HTTPS server

Create:

```bash
cd ~/tls-lab
nano https_server.py
```

Put:

```python
import http.server
import ssl

server = http.server.HTTPServer(
    ("localhost", 4443),
    http.server.SimpleHTTPRequestHandler
)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain("server.crt", "server.key")

server.socket = context.wrap_socket(
    server.socket,
    server_side=True
)

print("HTTPS server listening on https://localhost:4443")

server.serve_forever()
```

Run:

```bash
python3 https_server.py
```

You should see:

```
HTTPS server listening on https://localhost:4443
```

## Test your HTTPS server

Open another terminal.

First:

```bash
curl -v https://localhost:4443
```
Output:
```
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days$ curl -v https://localhost:4443
* Host localhost:4443 was resolved.
* IPv6: ::1
* IPv4: 127.0.0.1
*   Trying [::1]:4443...
* connect to ::1 port 4443 from ::1 port 35034 failed: Connection refused
*   Trying 127.0.0.1:4443...
* Connected to localhost (127.0.0.1) port 4443
* ALPN: curl offers h2,http/1.1
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
*  CAfile: /etc/ssl/certs/ca-certificates.crt
*  CApath: /etc/ssl/certs
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (OUT), TLS alert, unknown CA (560):
* SSL certificate problem: self-signed certificate
* Closing connection
curl: (60) SSL certificate problem: self-signed certificate
More details here: https://curl.se/docs/sslcerts.html

curl failed to verify the legitimacy of the server and therefore could not
establish a secure connection to it. To learn more about this situation and
how to fix it, please visit the web page mentioned above.

```

You will likely see certificate verification failure because your certificate is self-signed.

Now:

```bash
curl -vk https://localhost:4443
```
Output:

```
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days$ curl -vk https://localhost:4443
* Host localhost:4443 was resolved.
* IPv6: ::1
* IPv4: 127.0.0.1
*   Trying [::1]:4443...
* connect to ::1 port 4443 from ::1 port 51866 failed: Connection refused
*   Trying 127.0.0.1:4443...
* Connected to localhost (127.0.0.1) port 4443
* ALPN: curl offers h2,http/1.1
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384 / X25519 / RSASSA-PSS
* ALPN: server did not agree on a protocol. Uses default.
* Server certificate:
*  subject: CN=localhost
*  start date: Sep 23 02:51:17 2026 GMT
*  expire date: Sep 23 02:51:17 2027 GMT
*  issuer: CN=localhost
*  SSL certificate verify result: self-signed certificate (18), continuing anyway.
*   Certificate level 0: Public key type RSA (2048/112 Bits/secBits), signed using sha256WithRSAEncryption
* using HTTP/1.x
> GET / HTTP/1.1
> Host: localhost:4443
> User-Agent: curl/8.5.0
> Accept: */*
> 
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* old SSL session ID is stale, removing
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Server: SimpleHTTP/0.6 Python/3.12.3
< Date: Wed, 23 Sep 2026 03:13:45 GMT
< Content-type: text/html; charset=utf-8
< Content-Length: 381
< 
<!DOCTYPE HTML>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Directory listing for /</title>
</head>
<body>
<h1>Directory listing for /</h1>
<hr>
<ul>
<li><a href="https_server.py">https_server.py</a></li>
<li><a href="server.crt">server.crt</a></li>
<li><a href="server.key">server.key</a></li>
<li><a href="User-Agent%3A">User-Agent:</a></li>
</ul>
<hr>
</body>
</html>
* Closing connection
* TLSv1.3 (OUT), TLS alert, close notify (256):

```
This should allow the connection despite certificate verification failure.

This is a very important learning moment.

You have demonstrated:

```
TCP works
     ↓
TLS works
     ↓
Certificate verification fails
```

These are three different things.

## Inspect your local TLS server

Run:

```bash
openssl s_client \
  -connect localhost:4443 \
  -servername localhost
```
Output:

```
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days$ openssl s_client \
  -connect localhost:4443 \
  -servername localhost
CONNECTED(00000003)
depth=0 CN = localhost
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
---
Certificate chain
 0 s:CN = localhost
   i:CN = localhost
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA256
   v:NotBefore: Sep 23 02:51:17 2026 GMT; NotAfter: Sep 23 02:51:17 2027 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDCTCCAfGgAwIBAgIUMXBRqRmVvlRnDNH0K5DI3+Jk6E0wDQYJKoZIhvcNAQEL
BQAwFDESMBAGA1UEAwwJbG9jYWxob3N0MB4XDTI2MDkyMzAyNTExN1oXDTI3MDky
MzAyNTExN1owFDESMBAGA1UEAwwJbG9jYWxob3N0MIIBIjANBgkqhkiG9w0BAQEF
AAOCAQ8AMIIBCgKCAQEAxLbTVbUy4JfrhaVO0h/TgbqQFDmM/uNPIE347nscoQR/
8wAy92BsD0Fltk0nlcLZSH8jTI6hNOM9Hk7Hxt0mtfkYGYXTSmMm/qEaszVQRB2t
ba8pyy4tAYmko0kImyVkrSmYqd6rP41Dgg05/3Hvj+CT4L47IxUizT9zNIaqO34l
1LpJnFUimOvwyoaG7Qj9SY5jU762qERZBTQ7aiRsEX/J+xBmT5HUfRUh4uIpET7F
/DAssAEXW5cck4iY4STE77ALJqRYWxAEvn4eOKWH5TEPIojDki1E/ro7tKti0qb/
Umyge/TCOZeARIe/bfmpbJ97s7RAuj6JNvIF2yX+VQIDAQABo1MwUTAdBgNVHQ4E
FgQU7SZmmiBjQHfUmqNPYVE2+HYzze4wHwYDVR0jBBgwFoAU7SZmmiBjQHfUmqNP
YVE2+HYzze4wDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEAXNOe
F38IRpnOp6iKgusLxteJsI03Cnf6UJCigJgIegGo2xP0Fb839VLBd8IN2icBfjCG
cn6NpuIVl79YtpBpFj3nWzSHCq4p8+g6z5KXoW+VmS0FPD+uKPhsKlRbCdbJ0IVT
MTfZ+eDED0dfGVa8on8ozRqnKTXCoeMCoywBBB/BwxAyYTXj2EEVaqn2bNDBVTvM
fZl7uVCjfIN0GxDSGsS62a2cbkyoSzsFhCx/kBZRQWyNk9Q8CUjwM84RjlJMIWCj
EOpLpG0F974HgHY3+447cjlD0esLQMvZfGTNoeEdTjbtJIAH6Om7WWzpiYs0bs9Q
6aRP5xgSxpuZrN2f1A==
-----END CERTIFICATE-----
subject=CN = localhost
issuer=CN = localhost
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1337 bytes and written 391 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 2048 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 4B78F5F0D101C4170A5ED92BB9DFEB0DCE94C0EB1445A49FDE70608B111B49BB
    Session-ID-ctx: 
    Resumption PSK: 1751C5D62EE2B7BA9041C87ABE9FDD36647DF8F352D7D4B71EF63B5AF4E5ADC501405D826D650A47F1A0C61D9FDA0368
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 08 97 f6 d5 0f 69 00 23-e1 b2 05 fb 8c d6 af cd   .....i.#........
    0010 - 90 f4 99 d6 e7 ba 79 b9-31 1d 04 bf 2d f0 d3 37   ......y.1...-..7
    0020 - 6f 6a a3 38 fc 0e cc 34-58 ea 27 bb 99 be af d1   oj.8...4X.'.....
    0030 - 03 0c 63 cf 7f 75 30 3b-0a dd e2 88 3e da df 8d   ..c..u0;....>...
    0040 - ad ad c7 7c 59 70 5a 6a-1b 5f ef a1 f6 e3 3e c4   ...|YpZj._....>.
    0050 - 40 90 2a 3f 49 ee 54 a6-9e 57 e4 f6 36 2b 8a a4   @.*?I.T..W..6+..
    0060 - 8a ef 02 2c ea 49 59 49-9e 93 a6 9f 8a 78 15 ae   ...,.IYI.....x..
    0070 - 96 27 dc a1 07 3f 6e 6c-b8 3a f3 59 9a 60 4e 69   .'...?nl.:.Y.`Ni
    0080 - 01 ae 68 db 49 5a 09 6f-be 31 fb 60 f8 c3 1a 25   ..h.IZ.o.1.`...%
    0090 - 51 6a 22 ea 6a 31 46 c3-1b bd 5f ca 91 80 b6 a0   Qj".j1F..._.....
    00a0 - ad ea 28 7a 6a 2c 4b 87-1d 2c 1d 43 04 bc fb e7   ..(zj,K..,.C....
    00b0 - aa 4c 3b cf 94 ce e3 6c-17 97 be cd 74 80 03 63   .L;....l....t..c
    00c0 - a5 42 02 c4 9d 54 40 72-04 f1 c3 d1 fa df 18 1b   .B...T@r........

    Start Time: 1790133315
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 94D76E2DF08A910C6B9F0143D6D549842340BD05B4BCD29AC8B132538A87600A
    Session-ID-ctx: 
    Resumption PSK: 97AE386D2317B4FE45D505878AC67AF64D16CCD32D5C6A7F8B3C58581EBF3917F3216BC6CBC88394FCA9FE6AD2F442EC
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 08 97 f6 d5 0f 69 00 23-e1 b2 05 fb 8c d6 af cd   .....i.#........
    0010 - 7f ae b8 5b 15 d4 12 87-64 b7 18 9a 0c e7 68 6c   ...[....d.....hl
    0020 - 85 75 03 81 fa d1 ca d3-95 ab 66 87 f6 10 2e 23   .u........f....#
    0030 - d6 a9 3b cb a7 38 9a 31-b6 22 51 cc cd b2 1e a8   ..;..8.1."Q.....
    0040 - 6f f6 77 5e 95 fe 39 bf-8c a8 29 8e 17 97 f2 0e   o.w^..9...).....
    0050 - 8a 73 1c 8a a6 53 96 a2-97 ed 81 c3 e1 09 f3 81   .s...S..........
    0060 - 80 ff c2 a3 9e 19 8e 41-14 4a 86 af ef 50 c1 fc   .......A.J...P..
    0070 - 6c f4 50 03 21 8d 11 2f-51 81 fc db 10 bd 72 a5   l.P.!../Q.....r.
    0080 - 44 88 08 ac 62 4e a2 24-2b f3 fe 41 70 bf 15 69   D...bN.$+..Ap..i
    0090 - 91 52 1a 71 9e 54 6a 82-0b cf 91 bb ea 84 76 c2   .R.q.Tj.......v.
    00a0 - 76 6c 6b ae 8e eb db 54-d0 5e aa e2 7f be 6a 87   vlk....T.^....j.
    00b0 - d2 0c 97 15 24 9f 8a 19-fc bd 92 77 c2 14 2d 5b   ....$......w..-[
    00c0 - 0b d0 6b e5 ca 3b 98 cb-ad db 6d d4 50 e2 47 37   ..k..;....m.P.G7

    Start Time: 1790133315
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
```
You can now see the certificate you created yourself.

This is much more valuable than simply reading about certificates.