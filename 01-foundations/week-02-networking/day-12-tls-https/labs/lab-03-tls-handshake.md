# Lab 3: Observe TLS handshake

Run:

```bash
openssl s_client \
  -connect example.com:443 \
  -servername example.com
```

Output:
```bash
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https$ openssl s_client \
  -connect example.com:443 \
  -servername example.com
CONNECTED(00000003)
depth=3 C = US, O = SSL Corporation, CN = SSL.com TLS ECC Root CA 2022
verify return:1
depth=2 C = US, O = SSL Corporation, CN = SSL.com TLS Transit ECC CA R2
verify return:1
depth=1 C = US, O = SSL Corporation, CN = Cloudflare TLS Issuing ECC CA 3
verify return:1
depth=0 CN = example.com
verify return:1
---
Certificate chain
 0 s:CN = example.com
   i:C = US, O = SSL Corporation, CN = Cloudflare TLS Issuing ECC CA 3
   a:PKEY: id-ecPublicKey, 256 (bit); sigalg: ecdsa-with-SHA256
   v:NotBefore: Jul 29 22:10:08 2026 GMT; NotAfter: Oct 27 22:17:21 2026 GMT
 1 s:C = US, O = SSL Corporation, CN = Cloudflare TLS Issuing ECC CA 3
   i:C = US, O = SSL Corporation, CN = SSL.com TLS Transit ECC CA R2
   a:PKEY: id-ecPublicKey, 256 (bit); sigalg: ecdsa-with-SHA384
   v:NotBefore: May 29 19:49:45 2025 GMT; NotAfter: May 27 19:49:44 2035 GMT
 2 s:C = US, O = SSL Corporation, CN = SSL.com TLS Transit ECC CA R2
   i:C = US, O = SSL Corporation, CN = SSL.com TLS ECC Root CA 2022
   a:PKEY: id-ecPublicKey, 384 (bit); sigalg: ecdsa-with-SHA384
   v:NotBefore: Oct 21 17:02:23 2022 GMT; NotAfter: Oct 17 17:02:22 2037 GMT
 3 s:C = US, O = SSL Corporation, CN = SSL.com TLS ECC Root CA 2022
   i:C = GB, ST = Greater Manchester, L = Salford, O = Comodo CA Limited, CN = AAA Certificate Services
   a:PKEY: id-ecPublicKey, 384 (bit); sigalg: RSA-SHA256
   v:NotBefore: Aug  1 00:00:00 2025 GMT; NotAfter: Dec 31 23:59:59 2028 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIID5jCCA42gAwIBAgIQBiTQqzEVWHgLfVITuWMYMTAKBggqhkjOPQQDAjBRMQsw
CQYDVQQGEwJVUzEYMBYGA1UECgwPU1NMIENvcnBvcmF0aW9uMSgwJgYDVQQDDB9D
bG91ZGZsYXJlIFRMUyBJc3N1aW5nIEVDQyBDQSAzMB4XDTI2MDcyOTIyMTAwOFoX
DTI2MTAyNzIyMTcyMVowFjEUMBIGA1UEAwwLZXhhbXBsZS5jb20wWTATBgcqhkjO
PQIBBggqhkjOPQMBBwNCAAR2Tgmj3bLPRaVN0Vud8FEAUiMz3Z2Bd5lti39uhuvB
ARyn+R6JJkBCv54dlTizzaUBzLnriaPVW9uysYIJXTVio4ICgDCCAnwwDAYDVR0T
AQH/BAIwADAfBgNVHSMEGDAWgBSDA/3n9vVKTRVB9O0iFtMyCj7KZjBsBggrBgEF
BQcBAQRgMF4wOQYIKwYBBQUHMAKGLWh0dHA6Ly9pLmNmLWkuc3NsLmNvbS9DbG91
ZGZsYXJlLVRMUy1JLUUzLmNlcjAhBggrBgEFBQcwAYYVaHR0cDovL28uY2YtaS5z
c2wuY29tMCUGA1UdEQQeMByCC2V4YW1wbGUuY29tgg0qLmV4YW1wbGUuY29tMCMG
A1UdIAQcMBowCAYGZ4EMAQIBMA4GDCsGAQQBgqkwAQMBATATBgNVHSUEDDAKBggr
BgEFBQcDATBTBgNVHR8ETDBKMEigRqBEhkJodHRwOi8vYy5jZi1pLnNzbC5jb20v
YWU4MDFlZDFjNTViYjU3OWQ3OTIwOGIwZDc3MmFjZmI4Y2MzYTIwOC5jcmwwDgYD
VR0PAQH/BAQDAgeAMA8GCSsGAQQBgtpLLAQCBQAwggEEBgorBgEEAdZ5AgQCBIH1
BIHyAPAAdwCUTkOH+uzB74HzGSQmqBhlAcfTXzgCAT9yZ31VNy4Z2AAAAZ+v9sM2
AAAEAwBIMEYCIQD9WFotRGzWRjLUpKu5UgFVEIW2JB7MtvZe+tocSNgcyQIhAJCF
dDoCWE99JjFKSmzjeRhbiH0M3Aw+h414y9bGxT+PAHUAyKPEf8ezrbk1awE/anoS
beM6TkOlxkb5l605dZkdz5oAAAGfr/bDTAAABAMARjBEAiAKprPtjMQLlLrSks4e
CDoJZ6WqekRLH6AWHSHco9LXtQIgMsRhNtbw0Gp9Q0ItZB5D/0qTzrPKMBDbJZor
+NZkce4wCgYIKoZIzj0EAwIDRwAwRAIgELh9REqDsIBMBAkADWsc3iuhbkwHyfcv
6w+HsjhdPcwCIDzda23fZzKA2+qG5L/k1ti5g4rk3WiJU0UbvpUGLKKv
-----END CERTIFICATE-----
subject=CN = example.com
issuer=C = US, O = SSL Corporation, CN = Cloudflare TLS Issuing ECC CA 3
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: ECDSA
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 3982 bytes and written 393 bytes
Verification: OK
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 256 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 0 (ok)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: AF17C20A899B8D39E189B19B24B963DCA5AFDFB87FB9029288A9D6D79DAB5ECF
    Session-ID-ctx: 
    Resumption PSK: B4B39025EDEFEFB8F1B03277A92783C2516F9D494A30BF20D9D429D4784549EE2BBB900A8DDF1EEA2EDCEFCEA21719D4
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 64800 (seconds)
    TLS session ticket:
    0000 - 08 80 9e 52 7b 40 88 53-16 b9 6a f2 60 7a 16 a1   ...R{@.S..j.`z..
    0010 - 99 c6 73 75 d3 fd 92 11-b7 e2 54 5f c9 e5 e7 b8   ..su......T_....
    0020 - 4f a4 78 b8 8b ac 52 28-6b ce a4 a8 7b ff e5 a2   O.x...R(k...{...
    0030 - 4a 0c c2 5b 83 8c 56 44-3b d3 8a 74 e1 51 be 60   J..[..VD;..t.Q.`
    0040 - 87 82 43 9a 78 be 5a e8-d4 ae 88 58 91 16 96 ee   ..C.x.Z....X....
    0050 - 9d b1 64 25 b6 11 80 1a-bc b5 5f 8d 46 ae a2 f0   ..d%......_.F...
    0060 - 3d 14 e6 b9 2f e1 ab 0d-b9 ff e9 9b ee d2 8e 4a   =.../..........J
    0070 - 12 cf c5 65 e7 d3 4a 68-ea 3d 13 5a d9 c8 c9 75   ...e..Jh.=.Z...u
    0080 - 79 b0 19 89 0e 53 42 00-24 5d b5 cf 08 ad 1b 08   y....SB.$]......
    0090 - 41 47 bf 47 bc 35 6c e4-d4 d6 f5 74 ce df 2e 5e   AG.G.5l....t...^
    00a0 - c4 40 5b 55 90 22 a0 29-bd 5d bb 38 42 0d 09 90   .@[U.".).].8B...
    00b0 - 26 b3 47 1f 39 3a 41 c5-89 59 89 75 1e f7 2a 14   &.G.9:A..Y.u..*.

    Start Time: 1790124103
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 471C69BBC1F061CF2F438F9364AF151CD058085FB200E5688AAA618C0E6B55BE
    Session-ID-ctx: 
    Resumption PSK: B35C8804A02D8543C0C1E06FE2F5A41886CA6FE4955DB1E46EFE25F6F93EC06FF4BABE4824D1D6682AEC36DE3AAB1D8B
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 64800 (seconds)
    TLS session ticket:
    0000 - 08 80 9e 52 7b 40 88 53-16 b9 6a f2 60 7a 16 a1   ...R{@.S..j.`z..
    0010 - 40 fd 9f b6 ed 01 8c 29-e8 18 3d 69 19 4d 9e 6d   @......)..=i.M.m
    0020 - bf 42 d0 77 26 09 ca 21-77 fa 47 5b 56 6c 95 b0   .B.w&..!w.G[Vl..
    0030 - 3b 10 fa 49 b8 2c b3 09-b8 34 28 0d d6 56 4f 90   ;..I.,...4(..VO.
    0040 - 0a dd 9f d9 37 87 f4 79-18 de 00 4b 75 fa 68 01   ....7..y...Ku.h.
    0050 - 87 74 de 58 b8 54 ea a8-9b 47 89 ee 00 4b 8f 2b   .t.X.T...G...K.+
    0060 - 5f e1 d6 1b aa fc ce a8-19 45 88 e3 96 e8 08 56   _........E.....V
    0070 - 90 15 b4 2e c8 0b 69 b9-ce 45 e3 a4 b7 ef 87 70   ......i..E.....p
    0080 - 56 25 d1 c8 65 ee ed 06-e0 8e cf 11 64 56 09 c6   V%..e.......dV..
    0090 - 66 5c 71 e9 40 e6 d1 c4-9a 72 ca 7c 51 05 72 9e   f\q.@....r.|Q.r.
    00a0 - b3 7a eb 3e 4a 2a 7c f9-70 73 74 ed f3 cf 2c 89   .z.>J*|.pst...,.
    00b0 - 00 9e 42 98 76 47 fa 93-29 2a 15 44 2e 17 31 20   ..B.vG..)*.D..1 

    Start Time: 1790124103
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
closed
```


Find:

```bash
Protocol : TLSv1.3
Cipher : TLS_AES_256_GCM_SHA384
Certificate : ok
Verification : ok
```

Then compare:

```bash
curl -v https://example.com
```

Output:

```bash
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https$ curl -v https;//example.com
* Could not resolve host: https
* Closing connection
curl: (6) Could not resolve host: https
-bash: //example.com: No such file or directory
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https$ 
```

Your understanding should be:

```bash
curl
 ↓
DNS
 ↓
TCP
 ↓
TLS
 ↓
HTTP
```