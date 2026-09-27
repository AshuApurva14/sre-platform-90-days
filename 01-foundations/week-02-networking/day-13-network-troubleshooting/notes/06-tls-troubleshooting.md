# TLS Troubleshooting

You learned TLS yesterday.

Today:

Use TLS knowledge to troubleshoot real failures.

Run:

```bash
openssl s_client \
-connect example.com:443 \
-servername example.com
```

Output:

```
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days$ openssl s_client -connect example.com:443 -servername example.com
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
   v:NotBefore: Sep 26 22:49:11 2026 GMT; NotAfter: Dec 25 22:56:35 2026 GMT
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
MIID5jCCA42gAwIBAgIQAe7mqrtSHV4U/DFf2ZhWkDAKBggqhkjOPQQDAjBRMQsw
CQYDVQQGEwJVUzEYMBYGA1UECgwPU1NMIENvcnBvcmF0aW9uMSgwJgYDVQQDDB9D
bG91ZGZsYXJlIFRMUyBJc3N1aW5nIEVDQyBDQSAzMB4XDTI2MDkyNjIyNDkxMVoX
DTI2MTIyNTIyNTYzNVowFjEUMBIGA1UEAwwLZXhhbXBsZS5jb20wWTATBgcqhkjO
PQIBBggqhkjOPQMBBwNCAARqadExWzxTJ4S3LSzKIzAAeyF09q0Qt0F0XmLiZiaJ
SD0SQPhVK36pUKlM55TUstJnrU7f+7elE0kZESKzzcbto4ICgDCCAnwwDAYDVR0T
AQH/BAIwADAfBgNVHSMEGDAWgBSDA/3n9vVKTRVB9O0iFtMyCj7KZjBsBggrBgEF
BQcBAQRgMF4wOQYIKwYBBQUHMAKGLWh0dHA6Ly9pLmNmLWkuc3NsLmNvbS9DbG91
ZGZsYXJlLVRMUy1JLUUzLmNlcjAhBggrBgEFBQcwAYYVaHR0cDovL28uY2YtaS5z
c2wuY29tMCUGA1UdEQQeMByCC2V4YW1wbGUuY29tgg0qLmV4YW1wbGUuY29tMCMG
A1UdIAQcMBowCAYGZ4EMAQIBMA4GDCsGAQQBgqkwAQMBATATBgNVHSUEDDAKBggr
BgEFBQcDATBTBgNVHR8ETDBKMEigRqBEhkJodHRwOi8vYy5jZi1pLnNzbC5jb20v
YWU4MDFlZDFjNTViYjU3OWQ3OTIwOGIwZDc3MmFjZmI4Y2MzYTIwOC5jcmwwDgYD
VR0PAQH/BAQDAgeAMA8GCSsGAQQBgtpLLAQCBQAwggEEBgorBgEEAdZ5AgQCBIH1
BIHyAPAAdgCUTkOH+uzB74HzGSQmqBhlAcfTXzgCAT9yZ31VNy4Z2AAAAaDf8a1i
AAAEAwBHMEUCIQCuCUahRazwOcqj3A77y8eXdQBpLlGCjv9D/xvXd3X7hAIgbc0K
MS+MsANY5WLGpHgTk3Uxk0g1VWTQB78vYRMga1EAdgDLOPcViXyEoURfW8Hd+8lu
8ppZzUcKaQWFsMsUwxRY5wAAAaDf8a1+AAAEAwBHMEUCIB2YN/lZP6eSBMtV0BTr
GD7KSyKVu/i68Zza97li96FcAiEA1mtvTnM8zbNKj6ArUpWmgTRURDDgOC4R1C2W
5cSK6fIwCgYIKoZIzj0EAwIDRwAwRAIgNGlXxWLTTqn5+XQOkP06fTgaEbjDMAHU
ILmIapx8i5sCIAeTI/xpafGZNB9HwNfEeU05yh+aSv95pD8SNtIAWNr0
-----END CERTIFICATE-----
subject=CN = example.com
issuer=C = US, O = SSL Corporation, CN = Cloudflare TLS Issuing ECC CA 3
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: ECDSA
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 3983 bytes and written 393 bytes
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
    Session-ID: 1ACC9C48E16CF37C0FE5EC1FA6963F596CF36ADF93CAEEDD25141B526F35E864
    Session-ID-ctx: 
    Resumption PSK: 6506D5E30F6577032C0DD539A6EC419307F601EA8214EED1D82A030DFF40629AB0F14892B794AD3437872D8281700955
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 64800 (seconds)
    TLS session ticket:
    0000 - 20 ef 8c d4 21 fd 3a 3b-37 ee 46 c3 a0 05 e9 e7    ...!.:;7.F.....
    0010 - b1 4a 53 db 41 6e 11 b7-c1 ab f0 33 a2 fd cd 17   .JS.An.....3....
    0020 - 05 10 4c ec 82 99 7f 48-6c 71 9d 91 d5 19 14 dc   ..L....Hlq......
    0030 - a7 2d 9a 30 b4 73 20 98-bc 3a f6 89 af cf 03 6c   .-.0.s ..:.....l
    0040 - 59 9f 2b f2 49 cb 8f b1-50 4e a1 5c 5c 79 73 53   Y.+.I...PN.\\ysS
    0050 - fb a3 84 ed 9b da 99 00-56 28 83 bd 4a b6 f7 ea   ........V(..J...
    0060 - d4 f9 b5 f1 d2 25 45 82-87 2c 50 4a 98 d1 93 c5   .....%E..,PJ....
    0070 - 8c 0a 43 2f e4 14 55 2f-ed 9c 66 1e c2 42 c6 23   ..C/..U/..f..B.#
    0080 - 7d 83 1d d9 21 23 2c 4e-5b ae bd 7a 02 c7 e7 80   }...!#,N[..z....
    0090 - 63 d4 44 c1 96 6e b0 cf-4b 3e 87 4c dc 0a 61 a0   c.D..n..K>.L..a.
    00a0 - 7c 9d fa eb d0 7b a8 ec-c1 6e c0 df 46 d2 3d 77   |....{...n..F.=w
    00b0 - b3 c5 90 33 f6 80 95 de-a3 05 03 60 8a 62 2c 49   ...3.......`.b,I

    Start Time: 1790475093
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
    Session-ID: 9772241CD34B4F0365C39AE175A5100035F4C8EE95204289FE0C2C8031106A4A
    Session-ID-ctx: 
    Resumption PSK: CBF959587F07D38E3D3AD2C30B2F8DF1D0866A5C850DF7E7DC54B4E9D0BC5000D1D449A90E13F308988E366B1E9988E0
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 64800 (seconds)
    TLS session ticket:
    0000 - 20 ef 8c d4 21 fd 3a 3b-37 ee 46 c3 a0 05 e9 e7    ...!.:;7.F.....
    0010 - 9d d0 8e 04 dd 1f 4e c6-05 43 6d 5e 74 b1 d0 06   ......N..Cm^t...
    0020 - af b4 8b de ba 91 fb 09-72 32 d0 b9 4b ae ee 52   ........r2..K..R
    0030 - 75 f3 09 a5 6f f7 ac f9-5f ff 2d f6 0c 1e d9 95   u...o..._.-.....
    0040 - 75 4a 95 4e c3 7c af 09-59 b8 a7 e5 0a 1c 75 88   uJ.N.|..Y.....u.
    0050 - 5f d8 43 7c 41 4d 7a 37-65 ce d0 2b a3 9a 7a 96   _.C|AMz7e..+..z.
    0060 - f3 c7 a7 8e 0f af 0e 3e-fe 4d 81 aa 6a c1 6a eb   .......>.M..j.j.
    0070 - 42 dd 07 60 48 86 09 ce-84 51 69 40 0d 36 29 7a   B..`H....Qi@.6)z
    0080 - b4 01 7c 3a c3 66 72 85-71 aa 5f 34 57 ad fb 88   ..|:.fr.q._4W...
    0090 - b4 52 84 92 c0 6e 6f 58-f9 74 b4 80 73 4d 60 5c   .R...noX.t..sM`\
    00a0 - 46 ac 2a af b2 63 20 e1-a7 ed 92 cb 59 e5 ff 1b   F.*..c .....Y...
    00b0 - 08 8e f9 7b 42 31 6f 18-23 57 f6 68 95 39 f2 ed   ...{B1o.#W.h.9..

    Start Time: 1790475093
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
closed


```

Look for:

- `Certificate chain:` Present
- `Subject:` CN = example.com
- `Issuer:` =C = US, O = SSL Corporation, CN = Cloudflare TLS Issuing ECC CA 3
- `Validity:` 
- `TLS version:` v1.3
- `Cipher:` TLS_AES_256_GCM_SHA384
- `Verification:` Ok

Extract certificate information:

```bash
openssl s_client \
-connect example.com:443 \
-servername example.com </dev/null 2>/dev/null |
openssl x509 -noout -subject -issuer -dates
```

Get certifcate details.

Output:

```
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days$ openssl s_client \
-connect example.com:443 \
-servername example.com </dev/null 2>/dev/null |
openssl x509 -noout -subject -issuer -dates
subject=CN = example.com
issuer=C = US, O = SSL Corporation, CN = Cloudflare TLS Issuing ECC CA 3
notBefore=Sep 26 22:49:11 2026 GMT
notAfter=Dec 25 22:56:35 2026 GMT

```

Get SAN details.


Check SAN:

```bash
openssl s_client \
-connect example.com:443 \
-servername example.com </dev/null 2>/dev/null |
openssl x509 -noout -ext subjectAltName
```
Output:

```
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days$ openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null |
> openssl x509 -noout -ext subjectAltName
X509v3 Subject Alternative Name: 
    DNS:example.com, DNS:*.example.com

```

## TLS Troubleshooting Decision Tree

```
TCP 443 works?
       |
       YES
       ↓
TLS handshake works?
       |
       NO
       ↓
```

Check:
- TLS version
- certificate
- SNI
- trust chain
- cipher
- server configuration

If TLS succeeds:

```
TLS works
   ↓
Check HTTP
```
