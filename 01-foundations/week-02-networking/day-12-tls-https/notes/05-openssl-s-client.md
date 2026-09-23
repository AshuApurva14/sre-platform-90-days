# openssl s_client

## Why use it?

`openssl s_client` is one of the most useful TLS troubleshooting tools.

It allows us to inspect:

- TLS handshake
- Certificate
- Certificate chain
- TLS version
- Cipher
- SNI
- Verification errors

---

## Basic command

```
openssl s_client \
  -connect example.com:443
```
Output:

```
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https$ openssl s_client --connect httpbin.org:443
CONNECTED(00000003)
depth=2 C = US, O = Amazon, CN = Amazon Root CA 1
verify return:1
depth=1 C = US, O = Amazon, CN = Amazon RSA 2048 M01
verify return:1
depth=0 CN = httpbin.org
verify return:1
---
Certificate chain
 0 s:CN = httpbin.org
   i:C = US, O = Amazon, CN = Amazon RSA 2048 M01
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA256
   v:NotBefore: Jun 19 00:00:00 2026 GMT; NotAfter: Jan  2 23:59:59 2027 GMT
 1 s:C = US, O = Amazon, CN = Amazon RSA 2048 M01
   i:C = US, O = Amazon, CN = Amazon Root CA 1
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA256
   v:NotBefore: Aug 23 22:21:28 2022 GMT; NotAfter: Aug 23 22:21:28 2030 GMT
 2 s:C = US, O = Amazon, CN = Amazon Root CA 1
   i:C = US, ST = Arizona, L = Scottsdale, O = "Starfield Technologies, Inc.", CN = Starfield Services Root Certificate Authority - G2
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA256
   v:NotBefore: May 25 12:00:00 2015 GMT; NotAfter: Dec 31 01:00:00 2037 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIFzjCCBLagAwIBAgIQBBrcVyTcpg+34EoG2oOJwjANBgkqhkiG9w0BAQsFADA8
MQswCQYDVQQGEwJVUzEPMA0GA1UEChMGQW1hem9uMRwwGgYDVQQDExNBbWF6b24g
UlNBIDIwNDggTTAxMB4XDTI2MDYxOTAwMDAwMFoXDTI3MDEwMjIzNTk1OVowFjEU
MBIGA1UEAxMLaHR0cGJpbi5vcmcwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK
AoIBAQC2wJBc4poyAkDIZ9O1PntUPK0HNgAXiXd9F+OH2iZ00Nr15+Q/1bR1ogSp
iru/31ORyIbgNUE84dqnnaGteys1+QGPii0YIle9qjIKmHT4XIWUnEPir0EUJpqD
71qpP2Jv3VFwJT7lgzq0w7n4GEymRUgsDq559DE6b8eIP6DGK3kWWq61XBDxzNPW
qUqABLo5hx0V2v8tH8UF5INgiOMOLOAy9wCooCI0DsxEm9/3TY2IVFMGmsLINk3n
FftMYfTFFxEZm5nRc/nt0pKgPojEMkLNWqkSLSF2DTrqxst7kErdBvuHzWsyFOfU
ze1LEQRchMrlI1tvVQBboyflMDr7AgMBAAGjggLwMIIC7DAfBgNVHSMEGDAWgBSB
uA5jiokSGOX6OztQlZ/m5ZAThTAdBgNVHQ4EFgQUl8wC1oxpI/x2ATAQn5n6Z8Cy
yWYwJQYDVR0RBB4wHIILaHR0cGJpbi5vcmeCDSouaHR0cGJpbi5vcmcwEwYDVR0g
BAwwCjAIBgZngQwBAgEwDgYDVR0PAQH/BAQDAgWgMBMGA1UdJQQMMAoGCCsGAQUF
BwMBMDsGA1UdHwQ0MDIwMKAuoCyGKmh0dHA6Ly9jcmwucjJtMDEuYW1hem9udHJ1
c3QuY29tL3IybTAxLmNybDB1BggrBgEFBQcBAQRpMGcwLQYIKwYBBQUHMAGGIWh0
dHA6Ly9vY3NwLnIybTAxLmFtYXpvbnRydXN0LmNvbTA2BggrBgEFBQcwAoYqaHR0
cDovL2NydC5yMm0wMS5hbWF6b250cnVzdC5jb20vcjJtMDEuY2VyMAwGA1UdEwEB
/wQCMAAwggGFBgorBgEEAdZ5AgQCBIIBdQSCAXEBbwB1AExj3JjlnB2riPYeij3e
ro+rRKM3e1+blMP7oZz8wb4mAAABnt3x5kEAAAQDAEYwRAIgTJErKt2uQWuOD0/r
62UlnKJLr0SMvwX9E9HLOVPfvbgCIAKGoEyhyorazSm8Di+HFniQD1tI8ml2zZzV
38JK0KcrAHYA1tWNqdAXU/NqSqDHV0kCr+vH3CzTjNn3ZMgMiRkenwIAAAGe3fHm
LAAABAMARzBFAiEA+auX4jUrECZAFKcUpyqJ9kOMtWn92EInPftQC9y20yACIB23
PBP5OeHvzLGYNJ448/Bq6r8JZkcUbFDXBKL/D/6XAH4AjspHC6zeavOiBrCkeoS3
Rv4fxr+VPiXmm07kAkjzxugAAAGe3fHm5gAIAAAFAAQYj8cEAwBHMEUCIEh7kXT9
J+nYGpPc8GXfpuJxGCWbebiOJxIWzMNVXDAuAiEAtUZNLvPpEW70MOxLiLSVkyYi
QqrFmccntZjmim84bFQwDQYJKoZIhvcNAQELBQADggEBADMWuIcsih4oAJP9A5ck
ftPFG7SDHVsYb/oIN9slR4py4RgEqdCzF8lRA549Yna7gBE3v6GRTMSEiUu1pC9v
qG7jwfWQTtI2+VSBvlGr7pC77I9zAsPcvjczjeglf8/ZQyyGs0mnG7obW41j6Nxj
Wh/3Gjztrm82R29KEdRl1YPuF3OsefASOha4QSM0XF7gtbdrLxuoxmo5ATitNkpq
+jQtB2+MbXWLXyVwPvvNJ/hwz4ObiRF/lEapPmDI4l1LEN+EomZ893G1oqEeXTQi
U1h226mUn8Gt1WQnR2KuHhjtWdlyOTNvmac0pCrdOQrTqxyHjpFN/plfdpHVpY/d
Zgo=
-----END CERTIFICATE-----
subject=CN = httpbin.org
issuer=C = US, O = Amazon, CN = Amazon RSA 2048 M01
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA
Server Temp Key: ECDH, prime256v1, 256 bits
---
SSL handshake has read 4462 bytes and written 439 bytes
Verification: OK
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES128-GCM-SHA256
Server public key is 2048 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES128-GCM-SHA256
    Session-ID: 9AA024E1FB6540A8E58DAEA6AC84B43A2833E9DA5C96A8E1C25114FEF1ECC43D
    Session-ID-ctx: 
    Master-Key: 91436933220ABC2CEBA1E2F4CB23372BD6FFDEFDB739633AEE083A4DE87F91425F1BB2B00CD33B214DB9067A8CA5137E
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 85385 (seconds)
    TLS session ticket:
    0000 - 01 8a a4 9f 7b e5 29 f5-7d 00 ca c8 4a 9a e7 29   ....{.).}...J..)
    0010 - 45 df b4 56 e5 d5 e5 02-79 b9 8d f8 db f8 42 a3   E..V....y.....B.
    0020 - 22 79 41 ed 3a 53 38 f6-29 85 e1 6e bb f9 bc fe   "yA.:S8.)..n....
    0030 - cb 8b c4 c4 c9 89 c3 96-d4 a4 bb 50 64 eb 1e eb   ...........Pd...
    0040 - 3a bb d9 e9 98 08 93 3f-4f 7d 9c 31 18 10 6a ac   :......?O}.1..j.
    0050 - ab e0 f9 bc 64 62 d9 f1-ea 55 72 bd fd ee 1f 9d   ....db...Ur.....
    0060 - 7f 2d 2f 7f 50 9e 36 c2-68 b6 46 3b d0 3d a2 a7   .-/.P.6.h.F;.=..
    0070 - 15 fc f8 74 0e 3c 57 44-5b 5c 91 62 77 f1 8a 1f   ...t.<WD[\.bw...
    0080 - 09 2b cf 83 33 84 7b 51-65 8d                     .+..3.{Qe.

    Start Time: 1790129814
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: yes
---
```
---

## With SNI

```
openssl s_client \
  -connect example.com:443 \
  -servername example.com
```
Output:

```
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https$ openssl s_client --connect httpbin.org:443 --servername httpbin.org
CONNECTED(00000003)
depth=2 C = US, O = Amazon, CN = Amazon Root CA 1
verify return:1
depth=1 C = US, O = Amazon, CN = Amazon RSA 2048 M01
verify return:1
depth=0 CN = httpbin.org
verify return:1
---
Certificate chain
 0 s:CN = httpbin.org
   i:C = US, O = Amazon, CN = Amazon RSA 2048 M01
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA256
   v:NotBefore: Jun 19 00:00:00 2026 GMT; NotAfter: Jan  2 23:59:59 2027 GMT
 1 s:C = US, O = Amazon, CN = Amazon RSA 2048 M01
   i:C = US, O = Amazon, CN = Amazon Root CA 1
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA256
   v:NotBefore: Aug 23 22:21:28 2022 GMT; NotAfter: Aug 23 22:21:28 2030 GMT
 2 s:C = US, O = Amazon, CN = Amazon Root CA 1
   i:C = US, ST = Arizona, L = Scottsdale, O = "Starfield Technologies, Inc.", CN = Starfield Services Root Certificate Authority - G2
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA256
   v:NotBefore: May 25 12:00:00 2015 GMT; NotAfter: Dec 31 01:00:00 2037 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIFzjCCBLagAwIBAgIQBBrcVyTcpg+34EoG2oOJwjANBgkqhkiG9w0BAQsFADA8
MQswCQYDVQQGEwJVUzEPMA0GA1UEChMGQW1hem9uMRwwGgYDVQQDExNBbWF6b24g
UlNBIDIwNDggTTAxMB4XDTI2MDYxOTAwMDAwMFoXDTI3MDEwMjIzNTk1OVowFjEU
MBIGA1UEAxMLaHR0cGJpbi5vcmcwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK
AoIBAQC2wJBc4poyAkDIZ9O1PntUPK0HNgAXiXd9F+OH2iZ00Nr15+Q/1bR1ogSp
iru/31ORyIbgNUE84dqnnaGteys1+QGPii0YIle9qjIKmHT4XIWUnEPir0EUJpqD
71qpP2Jv3VFwJT7lgzq0w7n4GEymRUgsDq559DE6b8eIP6DGK3kWWq61XBDxzNPW
qUqABLo5hx0V2v8tH8UF5INgiOMOLOAy9wCooCI0DsxEm9/3TY2IVFMGmsLINk3n
FftMYfTFFxEZm5nRc/nt0pKgPojEMkLNWqkSLSF2DTrqxst7kErdBvuHzWsyFOfU
ze1LEQRchMrlI1tvVQBboyflMDr7AgMBAAGjggLwMIIC7DAfBgNVHSMEGDAWgBSB
uA5jiokSGOX6OztQlZ/m5ZAThTAdBgNVHQ4EFgQUl8wC1oxpI/x2ATAQn5n6Z8Cy
yWYwJQYDVR0RBB4wHIILaHR0cGJpbi5vcmeCDSouaHR0cGJpbi5vcmcwEwYDVR0g
BAwwCjAIBgZngQwBAgEwDgYDVR0PAQH/BAQDAgWgMBMGA1UdJQQMMAoGCCsGAQUF
BwMBMDsGA1UdHwQ0MDIwMKAuoCyGKmh0dHA6Ly9jcmwucjJtMDEuYW1hem9udHJ1
c3QuY29tL3IybTAxLmNybDB1BggrBgEFBQcBAQRpMGcwLQYIKwYBBQUHMAGGIWh0
dHA6Ly9vY3NwLnIybTAxLmFtYXpvbnRydXN0LmNvbTA2BggrBgEFBQcwAoYqaHR0
cDovL2NydC5yMm0wMS5hbWF6b250cnVzdC5jb20vcjJtMDEuY2VyMAwGA1UdEwEB
/wQCMAAwggGFBgorBgEEAdZ5AgQCBIIBdQSCAXEBbwB1AExj3JjlnB2riPYeij3e
ro+rRKM3e1+blMP7oZz8wb4mAAABnt3x5kEAAAQDAEYwRAIgTJErKt2uQWuOD0/r
62UlnKJLr0SMvwX9E9HLOVPfvbgCIAKGoEyhyorazSm8Di+HFniQD1tI8ml2zZzV
38JK0KcrAHYA1tWNqdAXU/NqSqDHV0kCr+vH3CzTjNn3ZMgMiRkenwIAAAGe3fHm
LAAABAMARzBFAiEA+auX4jUrECZAFKcUpyqJ9kOMtWn92EInPftQC9y20yACIB23
PBP5OeHvzLGYNJ448/Bq6r8JZkcUbFDXBKL/D/6XAH4AjspHC6zeavOiBrCkeoS3
Rv4fxr+VPiXmm07kAkjzxugAAAGe3fHm5gAIAAAFAAQYj8cEAwBHMEUCIEh7kXT9
J+nYGpPc8GXfpuJxGCWbebiOJxIWzMNVXDAuAiEAtUZNLvPpEW70MOxLiLSVkyYi
QqrFmccntZjmim84bFQwDQYJKoZIhvcNAQELBQADggEBADMWuIcsih4oAJP9A5ck
ftPFG7SDHVsYb/oIN9slR4py4RgEqdCzF8lRA549Yna7gBE3v6GRTMSEiUu1pC9v
qG7jwfWQTtI2+VSBvlGr7pC77I9zAsPcvjczjeglf8/ZQyyGs0mnG7obW41j6Nxj
Wh/3Gjztrm82R29KEdRl1YPuF3OsefASOha4QSM0XF7gtbdrLxuoxmo5ATitNkpq
+jQtB2+MbXWLXyVwPvvNJ/hwz4ObiRF/lEapPmDI4l1LEN+EomZ893G1oqEeXTQi
U1h226mUn8Gt1WQnR2KuHhjtWdlyOTNvmac0pCrdOQrTqxyHjpFN/plfdpHVpY/d
Zgo=
-----END CERTIFICATE-----
subject=CN = httpbin.org
issuer=C = US, O = Amazon, CN = Amazon RSA 2048 M01
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA
Server Temp Key: ECDH, prime256v1, 256 bits
---
SSL handshake has read 4462 bytes and written 439 bytes
Verification: OK
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES128-GCM-SHA256
Server public key is 2048 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES128-GCM-SHA256
    Session-ID: D1F2AA087AE295EAF0B5055DFB4570D575B0EB77947AD1C300DE640E3A2A4628
    Session-ID-ctx: 
    Master-Key: CEDC62065AD51D7C47A2584D473DC1840DA885F82FE43F04C52D1ACDAA7B763C4FD0FA89BAAA536B22B1CEF1DA7ACC51
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 85278 (seconds)
    TLS session ticket:
    0000 - 01 47 f4 bb 5c 19 94 f5-cb 2c 9f f4 5e 1e 89 20   .G..\....,..^.. 
    0010 - 32 9a a7 81 3a 9d 7e 64-5a d8 46 c6 a5 3a d7 8c   2...:.~dZ.F..:..
    0020 - 53 39 05 10 0d f0 48 e5-b1 be 1d 17 5c be 49 74   S9....H.....\.It
    0030 - e7 8d b3 fa 24 5a 25 15-91 18 6d ad 59 41 ab ed   ....$Z%...m.YA..
    0040 - 3a ae 4a e5 c5 89 7c e1-35 a2 73 b6 60 f0 ba b6   :.J...|.5.s.`...
    0050 - 8b 5c 47 50 c9 ed 91 48-bf c2 a0 68 63 9c 68 68   .\GP...H...hc.hh
    0060 - db 2c 2e be 4c 6f 83 a9-e6 f2 bc 43 48 ea 3b d0   .,..Lo.....CH.;.
    0070 - 1a 85 82 3b 77 1a 41 e7-4b 49 c1 be 70 88 7b 56   ...;w.A.KI..p.{V
    0080 - 0b 1a b1 a5 5a 00 bf db-4a a3                     ....Z...J.

    Start Time: 1790129921
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: yes
---
```
---

## Show certificates

```
openssl s_client \
  -connect example.com:443 \
  -servername example.com \
  -showcerts
```

Output:

```bash
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https$ openssl s_client --connect httpbin.org:443 --servername httpbin.org -showcerts
CONNECTED(00000003)
depth=2 C = US, O = Amazon, CN = Amazon Root CA 1
verify return:1
depth=1 C = US, O = Amazon, CN = Amazon RSA 2048 M01
verify return:1
depth=0 CN = httpbin.org
verify return:1
---
Certificate chain
 0 s:CN = httpbin.org
   i:C = US, O = Amazon, CN = Amazon RSA 2048 M01
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA256
   v:NotBefore: Jun 19 00:00:00 2026 GMT; NotAfter: Jan  2 23:59:59 2027 GMT
-----BEGIN CERTIFICATE-----
MIIFzjCCBLagAwIBAgIQBBrcVyTcpg+34EoG2oOJwjANBgkqhkiG9w0BAQsFADA8
MQswCQYDVQQGEwJVUzEPMA0GA1UEChMGQW1hem9uMRwwGgYDVQQDExNBbWF6b24g
UlNBIDIwNDggTTAxMB4XDTI2MDYxOTAwMDAwMFoXDTI3MDEwMjIzNTk1OVowFjEU
MBIGA1UEAxMLaHR0cGJpbi5vcmcwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK
AoIBAQC2wJBc4poyAkDIZ9O1PntUPK0HNgAXiXd9F+OH2iZ00Nr15+Q/1bR1ogSp
iru/31ORyIbgNUE84dqnnaGteys1+QGPii0YIle9qjIKmHT4XIWUnEPir0EUJpqD
71qpP2Jv3VFwJT7lgzq0w7n4GEymRUgsDq559DE6b8eIP6DGK3kWWq61XBDxzNPW
qUqABLo5hx0V2v8tH8UF5INgiOMOLOAy9wCooCI0DsxEm9/3TY2IVFMGmsLINk3n
FftMYfTFFxEZm5nRc/nt0pKgPojEMkLNWqkSLSF2DTrqxst7kErdBvuHzWsyFOfU
ze1LEQRchMrlI1tvVQBboyflMDr7AgMBAAGjggLwMIIC7DAfBgNVHSMEGDAWgBSB
uA5jiokSGOX6OztQlZ/m5ZAThTAdBgNVHQ4EFgQUl8wC1oxpI/x2ATAQn5n6Z8Cy
yWYwJQYDVR0RBB4wHIILaHR0cGJpbi5vcmeCDSouaHR0cGJpbi5vcmcwEwYDVR0g
BAwwCjAIBgZngQwBAgEwDgYDVR0PAQH/BAQDAgWgMBMGA1UdJQQMMAoGCCsGAQUF
BwMBMDsGA1UdHwQ0MDIwMKAuoCyGKmh0dHA6Ly9jcmwucjJtMDEuYW1hem9udHJ1
c3QuY29tL3IybTAxLmNybDB1BggrBgEFBQcBAQRpMGcwLQYIKwYBBQUHMAGGIWh0
dHA6Ly9vY3NwLnIybTAxLmFtYXpvbnRydXN0LmNvbTA2BggrBgEFBQcwAoYqaHR0
cDovL2NydC5yMm0wMS5hbWF6b250cnVzdC5jb20vcjJtMDEuY2VyMAwGA1UdEwEB
/wQCMAAwggGFBgorBgEEAdZ5AgQCBIIBdQSCAXEBbwB1AExj3JjlnB2riPYeij3e
ro+rRKM3e1+blMP7oZz8wb4mAAABnt3x5kEAAAQDAEYwRAIgTJErKt2uQWuOD0/r
62UlnKJLr0SMvwX9E9HLOVPfvbgCIAKGoEyhyorazSm8Di+HFniQD1tI8ml2zZzV
38JK0KcrAHYA1tWNqdAXU/NqSqDHV0kCr+vH3CzTjNn3ZMgMiRkenwIAAAGe3fHm
LAAABAMARzBFAiEA+auX4jUrECZAFKcUpyqJ9kOMtWn92EInPftQC9y20yACIB23
PBP5OeHvzLGYNJ448/Bq6r8JZkcUbFDXBKL/D/6XAH4AjspHC6zeavOiBrCkeoS3
Rv4fxr+VPiXmm07kAkjzxugAAAGe3fHm5gAIAAAFAAQYj8cEAwBHMEUCIEh7kXT9
J+nYGpPc8GXfpuJxGCWbebiOJxIWzMNVXDAuAiEAtUZNLvPpEW70MOxLiLSVkyYi
QqrFmccntZjmim84bFQwDQYJKoZIhvcNAQELBQADggEBADMWuIcsih4oAJP9A5ck
ftPFG7SDHVsYb/oIN9slR4py4RgEqdCzF8lRA549Yna7gBE3v6GRTMSEiUu1pC9v
qG7jwfWQTtI2+VSBvlGr7pC77I9zAsPcvjczjeglf8/ZQyyGs0mnG7obW41j6Nxj
Wh/3Gjztrm82R29KEdRl1YPuF3OsefASOha4QSM0XF7gtbdrLxuoxmo5ATitNkpq
+jQtB2+MbXWLXyVwPvvNJ/hwz4ObiRF/lEapPmDI4l1LEN+EomZ893G1oqEeXTQi
U1h226mUn8Gt1WQnR2KuHhjtWdlyOTNvmac0pCrdOQrTqxyHjpFN/plfdpHVpY/d
Zgo=
-----END CERTIFICATE-----
 1 s:C = US, O = Amazon, CN = Amazon RSA 2048 M01
   i:C = US, O = Amazon, CN = Amazon Root CA 1
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA256
   v:NotBefore: Aug 23 22:21:28 2022 GMT; NotAfter: Aug 23 22:21:28 2030 GMT
-----BEGIN CERTIFICATE-----
MIIEXjCCA0agAwIBAgITB3MSOAudZoijOx7Zv5zNpo4ODzANBgkqhkiG9w0BAQsF
ADA5MQswCQYDVQQGEwJVUzEPMA0GA1UEChMGQW1hem9uMRkwFwYDVQQDExBBbWF6
b24gUm9vdCBDQSAxMB4XDTIyMDgyMzIyMjEyOFoXDTMwMDgyMzIyMjEyOFowPDEL
MAkGA1UEBhMCVVMxDzANBgNVBAoTBkFtYXpvbjEcMBoGA1UEAxMTQW1hem9uIFJT
QSAyMDQ4IE0wMTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAOtxLKnL
H4gokjIwr4pXD3i3NyWVVYesZ1yX0yLI2qIUZ2t88Gfa4gMqs1YSXca1R/lnCKeT
epWSGA+0+fkQNpp/L4C2T7oTTsddUx7g3ZYzByDTlrwS5HRQQqEFE3O1T5tEJP4t
f+28IoXsNiEzl3UGzicYgtzj2cWCB41eJgEmJmcf2T8TzzK6a614ZPyq/w4CPAff
nAV4coz96nW3AyiE2uhuB4zQUIXvgVSycW7sbWLvj5TDXunEpNCRwC4kkZjK7rol
jtT2cbb7W2s4Bkg3R42G3PLqBvt2N32e/0JOTViCk8/iccJ4sXqrS1uUN4iB5Nmv
JK74csVl+0u0UecCAwEAAaOCAVowggFWMBIGA1UdEwEB/wQIMAYBAf8CAQAwDgYD
VR0PAQH/BAQDAgGGMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjAdBgNV
HQ4EFgQUgbgOY4qJEhjl+js7UJWf5uWQE4UwHwYDVR0jBBgwFoAUhBjMhTTsvAyU
lC4IWZzHshBOCggwewYIKwYBBQUHAQEEbzBtMC8GCCsGAQUFBzABhiNodHRwOi8v
b2NzcC5yb290Y2ExLmFtYXpvbnRydXN0LmNvbTA6BggrBgEFBQcwAoYuaHR0cDov
L2NydC5yb290Y2ExLmFtYXpvbnRydXN0LmNvbS9yb290Y2ExLmNlcjA/BgNVHR8E
ODA2MDSgMqAwhi5odHRwOi8vY3JsLnJvb3RjYTEuYW1hem9udHJ1c3QuY29tL3Jv
b3RjYTEuY3JsMBMGA1UdIAQMMAowCAYGZ4EMAQIBMA0GCSqGSIb3DQEBCwUAA4IB
AQCtAN4CBSMuBjJitGuxlBbkEUDeK/pZwTXv4KqPK0G50fOHOQAd8j21p0cMBgbG
kfMHVwLU7b0XwZCav0h1ogdPMN1KakK1DT0VwA/+hFvGPJnMV1Kx2G4S1ZaSk0uU
5QfoiYIIano01J5k4T2HapKQmmOhS/iPtuo00wW+IMLeBuKMn3OLn005hcrOGTad
hcmeyfhQP7Z+iKHvyoQGi1C0ClymHETx/chhQGDyYSWqB/THwnN15AwLQo0E5V9E
SJlbe4mBlqeInUsNYugExNf+tOiybcrswBy8OFsd34XOW3rjSUtsuafd9AWySa3h
xRRrwszrzX/WWGm6wyB+f7C4
-----END CERTIFICATE-----
 2 s:C = US, O = Amazon, CN = Amazon Root CA 1
   i:C = US, ST = Arizona, L = Scottsdale, O = "Starfield Technologies, Inc.", CN = Starfield Services Root Certificate Authority - G2
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA256
   v:NotBefore: May 25 12:00:00 2015 GMT; NotAfter: Dec 31 01:00:00 2037 GMT
-----BEGIN CERTIFICATE-----
MIIEkjCCA3qgAwIBAgITBn+USionzfP6wq4rAfkI7rnExjANBgkqhkiG9w0BAQsF
ADCBmDELMAkGA1UEBhMCVVMxEDAOBgNVBAgTB0FyaXpvbmExEzARBgNVBAcTClNj
b3R0c2RhbGUxJTAjBgNVBAoTHFN0YXJmaWVsZCBUZWNobm9sb2dpZXMsIEluYy4x
OzA5BgNVBAMTMlN0YXJmaWVsZCBTZXJ2aWNlcyBSb290IENlcnRpZmljYXRlIEF1
dGhvcml0eSAtIEcyMB4XDTE1MDUyNTEyMDAwMFoXDTM3MTIzMTAxMDAwMFowOTEL
MAkGA1UEBhMCVVMxDzANBgNVBAoTBkFtYXpvbjEZMBcGA1UEAxMQQW1hem9uIFJv
b3QgQ0EgMTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALJ4gHHKeNXj
ca9HgFB0fW7Y14h29Jlo91ghYPl0hAEvrAIthtOgQ3pOsqTQNroBvo3bSMgHFzZM
9O6II8c+6zf1tRn4SWiw3te5djgdYZ6k/oI2peVKVuRF4fn9tBb6dNqcmzU5L/qw
IFAGbHrQgLKm+a/sRxmPUDgH3KKHOVj4utWp+UhnMJbulHheb4mjUcAwhmahRWa6
VOujw5H5SNz/0egwLX0tdHA114gk957EWW67c4cX8jJGKLhD+rcdqsq08p8kDi1L
93FcXmn/6pUCyziKrlA4b9v7LWIbxcceVOF34GfID5yHI9Y/QCB/IIDEgEw+OyQm
jgSubJrIqg0CAwEAAaOCATEwggEtMA8GA1UdEwEB/wQFMAMBAf8wDgYDVR0PAQH/
BAQDAgGGMB0GA1UdDgQWBBSEGMyFNOy8DJSULghZnMeyEE4KCDAfBgNVHSMEGDAW
gBScXwDfqgHXMCs4iKK4bUqc8hGRgzB4BggrBgEFBQcBAQRsMGowLgYIKwYBBQUH
MAGGImh0dHA6Ly9vY3NwLnJvb3RnMi5hbWF6b250cnVzdC5jb20wOAYIKwYBBQUH
MAKGLGh0dHA6Ly9jcnQucm9vdGcyLmFtYXpvbnRydXN0LmNvbS9yb290ZzIuY2Vy
MD0GA1UdHwQ2MDQwMqAwoC6GLGh0dHA6Ly9jcmwucm9vdGcyLmFtYXpvbnRydXN0
LmNvbS9yb290ZzIuY3JsMBEGA1UdIAQKMAgwBgYEVR0gADANBgkqhkiG9w0BAQsF
AAOCAQEAYjdCXLwQtT6LLOkMm2xF4gcAevnFWAu5CIw+7bMlPLVvUOTNNWqnkzSW
MiGpSESrnO09tKpzbeR/FoCJbM8oAxiDR3mjEH4wW6w7sGDgd9QIpuEdfF7Au/ma
eyKdpwAJfqxGF4PcnCZXmTA5YpaP7dreqsXMGz7KQ2hsVxa81Q4gLv7/wmpdLqBK
bRRYh5TmOTFffHPLkIhqhBGWJ6bt2YFGpn6jcgAKUj6DiAdjd4lpFw85hdKrCEVN
0FE6/V1dN2RMfjCyVSRCnTawXZwXgWHxyvkQAiSr6w10kY17RSlQOYiypok1JR4U
akcjMS9cmvqtmg5iUaQqqcT5NJ0hGA==
-----END CERTIFICATE-----
---
Server certificate
subject=CN = httpbin.org
issuer=C = US, O = Amazon, CN = Amazon RSA 2048 M01
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA
Server Temp Key: ECDH, prime256v1, 256 bits
---
SSL handshake has read 4462 bytes and written 439 bytes
Verification: OK
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES128-GCM-SHA256
Server public key is 2048 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES128-GCM-SHA256
    Session-ID: C400469BB70A725CCBD2C2B4DA90FECF73A1B80326E08EA706EAFB33500562A0
    Session-ID-ctx: 
    Master-Key: B88552D14A72199E7B23C85DC64E8FA32624776B77FF80FC367D0B9A841ABFE0CEE2482524C131BE8C0129CA14D4FA96
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 83949 (seconds)
    TLS session ticket:
    0000 - 01 40 3b ce ae c0 a2 4d-ee e2 63 3a fa 75 0c 6e   .@;....M..c:.u.n
    0010 - f8 76 16 24 9d 24 3f 3f-0d 04 d1 9d cb 43 a4 cf   .v.$.$??.....C..
    0020 - a6 ac 11 3f e1 e1 80 bb-05 97 e6 25 59 f3 9c 6b   ...?.......%Y..k
    0030 - 0b 90 fc 1a 9f 06 85 40-3d e3 b4 a6 0b 4d 06 ba   .......@=....M..
    0040 - 4c b7 4f a3 d3 5f 46 94-65 50 9c 8d ff 3e 75 fb   L.O.._F.eP...>u.
    0050 - f5 77 72 df 6f 96 30 04-36 c5 41 70 03 83 fb da   .wr.o.0.6.Ap....
    0060 - fa 88 39 a2 3f 8a 6a 0a-5e fe 50 64 6c 34 b9 35   ..9.?.j.^.Pdl4.5
    0070 - b9 b4 e0 ae d3 95 54 2c-ea 19 2e 2c 5b 3f 31 e4   ......T,...,[?1.
    0080 - 52 8f fb 10 86 1f e9 cb-ef 33                     R........3

    Start Time: 1790129979
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: yes
---
```
---

## Show certificate dates

```
openssl s_client \
  -connect example.com:443 \
  -servername example.com </dev/null 2>/dev/null \
  | openssl x509 -noout -dates
```
Output:

```bash
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https$ openssl s_client --connect httpbin.org:443 --servername httpbin.org </dev/null 2>/dev/null | openssl x509 -noout -dates
notBefore=Jun 19 00:00:00 2026 GMT
notAfter=Jan  2 23:59:59 2027 GMT
```
---

## Show subject and issuer

```
openssl s_client \
  -connect example.com:443 \
  -servername example.com </dev/null 2>/dev/null \
  | openssl x509 -noout -subject -issuer
```
```bash
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https$ openssl s_client --connect httpbin.org:443 --servername httpbin.org </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer
subject=CN = httpbin.org
issuer=C = US, O = Amazon, CN = Amazon RSA 2048 M01
```
---

## Show SAN

```
openssl s_client \
  -connect example.com:443 \
  -servername example.com </dev/null 2>/dev/null \
  | openssl x509 -noout -ext subjectAltName
```

Output:

```bash
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https$ openssl s_client --connect httpbin.org:443 --servername httpbin.org </dev/null 2>/dev/null | openssl x509 -noout -subject -ext subjectAltName
subject=CN = httpbin.org
X509v3 Subject Alternative Name: 
    DNS:httpbin.org, DNS:*.httpbin.org
```
---

## Test TLS 1.2

```
openssl s_client \
  -connect example.com:443 \
  -servername example.com \
  -tls1_2
```
Output:

```bash
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https$ openssl s_client \
  -connect example.com:443 \
  -servername example.com \
  -tls1_2
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
SSL handshake has read 4133 bytes and written 293 bytes
Verification: OK
---
New, TLSv1.2, Cipher is ECDHE-ECDSA-CHACHA20-POLY1305
Server public key is 256 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-ECDSA-CHACHA20-POLY1305
    Session-ID: 4E977F7A6AF76FDCF90860AD3306FCE13C038D5AD2A66189DE440C2D3085E30D
    Session-ID-ctx: 
    Master-Key: CB68AD062C1F0E3C913864049307554AEF8762B81150547BA18965702ADEE90ADE32C2F66E8DF47A040609E17D6781B5
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 64800 (seconds)
    TLS session ticket:
    0000 - ca 0c 06 65 e3 d4 fe a0-bd 65 98 c8 83 40 bc 39   ...e.....e...@.9
    0010 - 0d 77 b1 ad b1 7f 5a 3e-ce 45 dd 80 bd 53 86 72   .w....Z>.E...S.r
    0020 - a8 3f 21 51 26 2a f5 19-e3 73 c5 59 4a 89 36 31   .?!Q&*...s.YJ.61
    0030 - 19 04 d0 b1 b5 22 5a 7f-63 7d a8 74 87 ac 92 6d   ....."Z.c}.t...m
    0040 - c0 50 f4 ee 6f 4b 38 df-13 75 a4 58 3d 7a 34 2a   .P..oK8..u.X=z4*
    0050 - 9c 30 a0 95 aa 82 47 01-54 9e 08 1d 78 d3 2e 35   .0....G.T...x..5
    0060 - f2 87 2e 7d 67 dc ff 1a-08 cb 4c db 62 7f 8b b6   ...}g.....L.b...
    0070 - cd af 91 54 72 30 44 4e-fe 6a c5 c2 ae d6 55 05   ...Tr0DN.j....U.
    0080 - e2 51 86 a3 8c 8a 79 8c-b1 b7 19 25 b8 dd 15 2f   .Q....y....%.../
    0090 - cd f0 f7 10 39 cc 85 08-ab 7e 26 cf 59 1c f2 79   ....9....~&.Y..y
    00a0 - cd 20 fe d3 df 19 8f e0-af 90 15 a0 ad 17 88 ba   . ..............
    00b0 - 22 ca 8f 4d 10 e0 a5 cc-3c 3c 39 3b 2b cd 23 f1   "..M....<<9;+.#.

    Start Time: 1790130156
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: yes
---
```
---

## Test TLS 1.3

```
openssl s_client \
  -connect example.com:443 \
  -servername example.com \
  -tls1_3
```
Output:

```bash
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https$ openssl s_client -connect example.com:443 -servername example.com -tls1_3
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
SSL handshake has read 3982 bytes and written 325 bytes
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
```
---

## curl vs openssl

**curl:**

```bash
curl -v https://example.com
```
<img width="1450" height="1429" alt="Image" src="https://github.com/user-attachments/assets/498f59b5-da0b-4c7a-908e-fd286f7ef7cd" />


Good for:
- HTTPS request
- HTTP response
- TLS connection
- Client behavior

**openssl:**

```bash
openssl s_client ...
```
Good for:
- Certificate investigation
- TLS handshake investigation
- Chain inspection
- Protocol testing

---

## Key learning

When TLS is suspicious:

`curl -v`

and:

`openssl s_client -connect HOST:443 -servername HOST`

are two commands you should know.