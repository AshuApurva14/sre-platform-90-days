# HTTPS / TLS Troubleshooting

## Troubleshoot bottom-up

```
DNS
 ↓
TCP
 ↓
TLS
 ↓
HTTP
 ↓
Application
```
---

## Step 1 — DNS

```bash
dig httpbin.org
```
Output:

```
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https/tls-lab$ dig httpbin.org 

; <<>> DiG 9.18.39-0ubuntu0.24.04.7-Ubuntu <<>> httpbin.org
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 24280
;; flags: qr rd ra; QUERY: 1, ANSWER: 8, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;httpbin.org.                   IN      A

;; ANSWER SECTION:
httpbin.org.            21      IN      A       34.199.248.12
httpbin.org.            21      IN      A       44.194.230.42
httpbin.org.            21      IN      A       44.214.102.151
httpbin.org.            21      IN      A       100.31.16.17
httpbin.org.            21      IN      A       44.221.208.192
httpbin.org.            21      IN      A       3.217.138.231
httpbin.org.            21      IN      A       3.208.246.33
httpbin.org.            21      IN      A       3.234.28.4

;; Query time: 31 msec
;; SERVER: 10.255.255.254#53(10.255.255.254) (UDP)
;; WHEN: Wed Sep 23 02:56:55 UTC 2026
;; MSG SIZE  rcvd: 168
```

Question:

Does the hostname resolve to the expected address?

---

## Step 2 — TCP

```bash
nc -vz httpbin.org 443
```
Output:

```bash
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https/tls-lab$ nc -vz httpbin.org 443
Connection to httpbin.org (100.31.16.17) 443 port [tcp/https] succeeded!

```

If TCP fails, investigate:

- Firewall
- Security group
- Network ACL
- Routing
- NetworkPolicy
- Load balancer
- Listener
- Wrong port

TLS has not started if TCP cannot connect.

---

## Step 3 — TLS

```bash
openssl s_client \
  -connect httpbin.org:443 \
  -servername httpbin.org
```
Output:

```
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https/tls-lab$ openssl s_client -connect httpbin.org:443 -servername httpbin.org
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
    Session-ID: 62CD830920EDC1D3CDFBA495802BC9FEBFC1A3154B6EBB727712262184F1B26A
    Session-ID-ctx: 
    Master-Key: ED49830028ED9AD2BADBDA171539D6060AD350F2412F500DC92570C9D2FF6F3309B66E4361624CD035F70343DBB5FB35
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 83184 (seconds)
    TLS session ticket:
    0000 - 01 bf 1e ca f9 26 45 83-1b 4f a4 b5 c1 a0 d3 4a   .....&E..O.....J
    0010 - 8b 75 6b c7 f7 0f ba 1d-35 88 4b 15 b7 28 3f af   .uk.....5.K..(?.
    0020 - 7f f3 1f eb 28 0d 42 00-1f 7f 30 0d 26 28 69 52   ....(.B...0.&(iR
    0030 - 40 02 d7 96 6d 86 90 a8-ee 17 54 27 24 90 b3 25   @...m.....T'$..%
    0040 - 61 13 94 ba 87 14 c5 c6-06 7b 30 b1 69 f6 c6 18   a........{0.i...
    0050 - aa 95 a4 a4 d8 42 f5 33-a3 8a 5e ab 88 41 4d 38   .....B.3..^..AM8
    0060 - 31 e8 e7 3d 1d 24 65 da-47 de fc b7 64 0a 4d 7b   1..=.$e.G...d.M{
    0070 - f8 0d 4b 20 ae f9 9e bf-53 b0 8d f3 a8 bd fb e4   ..K ....S.......
    0080 - f6 ef a9 b9 5d 43 18 04-ab 9c                     ....]C....

    Start Time: 1790132383
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: yes
---
```

Investigate:

- TLS version
- Certificate
- Certificate chain
- Verification
- Cipher
- SNI

---

## Step 4 — Certificate

```bash
openssl s_client \
  -connect app.example.com:443 \
  -servername app.example.com </dev/null 2>/dev/null \
  | openssl x509 -noout -subject -issuer -dates
```
Output:

```bash
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https/tls-lab$ openssl s_client -connect httpbin.org:443 -servername httpbin.org </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates
subject=CN = httpbin.org
issuer=C = US, O = Amazon, CN = Amazon RSA 2048 M01
notBefore=Jun 19 00:00:00 2026 GMT
notAfter=Jan  2 23:59:59 2027 GMT
```


Check:

- Subject
- Issuer
- Expiry

Check SAN:

```bash
openssl s_client \
  -connect app.example.com:443 \
  -servername app.example.com </dev/null 2>/dev/null \
  | openssl x509 -noout -ext subjectAltName
```
Output:

```
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https/tls-lab$ openssl s_client -connect httpbin.org:443 -servername httpbin.org </dev/null 2>/dev/null | openssl x509 -noout -ext subjectAltName
X509v3 Subject Alternative Name: 
    DNS:httpbin.org, DNS:*.httpbin.org
```
---

## Step 5 — HTTP

```bash
curl -v https://app.example.com
```

Output:

```
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https/tls-lab$ curl -v httpbin.org
* Host httpbin.org:80 was resolved.
* IPv6: (none)
* IPv4: 100.61.72.171, 52.6.70.163, 3.217.138.231, 13.216.221.169, 107.21.166.194, 34.229.28.177, 3.234.28.4, 13.216.58.208
*   Trying 100.61.72.171:80...
* Connected to httpbin.org (100.61.72.171) port 80
> GET / HTTP/1.1
> Host: httpbin.org
> User-Agent: curl/8.5.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Date: Wed, 23 Sep 2026 03:03:56 GMT
< Content-Type: text/html; charset=utf-8
< Content-Length: 9593
< Connection: keep-alive
< Server: gunicorn/19.9.0
< Access-Control-Allow-Origin: *
< Access-Control-Allow-Credentials: true
< 
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>httpbin.org</title>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700|Source+Code+Pro:300,600|Titillium+Web:400,600,700"
        rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="/flasgger_static/swagger-ui.css">
    <link rel="icon" type="image/png" href="/static/favicon.ico" sizes="64x64 32x32 16x16" />
    <style>
        html {
            box-sizing: border-box;
            overflow: -moz-scrollbars-vertical;
            overflow-y: scroll;
        }

        *,
        *:before,
        *:after {
            box-sizing: inherit;
        }

        body {
            margin: 0;
            background: #fafafa;
        }
    </style>
</head>

<body>
    <a href="https://github.com/requests/httpbin" class="github-corner" aria-label="View source on Github">
        <svg width="80" height="80" viewBox="0 0 250 250" style="fill:#151513; color:#fff; position: absolute; top: 0; border: 0; right: 0;"
            aria-hidden="true">
            <path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path>
            <path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2"
                fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path>
            <path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z"
                fill="currentColor" class="octo-body"></path>
        </svg>
    </a>
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="position:absolute;width:0;height:0">
        <defs>
            <symbol viewBox="0 0 20 20" id="unlocked">
                <path d="M15.8 8H14V5.6C14 2.703 12.665 1 10 1 7.334 1 6 2.703 6 5.6V6h2v-.801C8 3.754 8.797 3 10 3c1.203 0 2 .754 2 2.199V8H4c-.553 0-1 .646-1 1.199V17c0 .549.428 1.139.951 1.307l1.197.387C5.672 18.861 6.55 19 7.1 19h5.8c.549 0 1.428-.139 1.951-.307l1.196-.387c.524-.167.953-.757.953-1.306V9.199C17 8.646 16.352 8 15.8 8z"></path>
            </symbol>

            <symbol viewBox="0 0 20 20" id="locked">
                <path d="M15.8 8H14V5.6C14 2.703 12.665 1 10 1 7.334 1 6 2.703 6 5.6V8H4c-.553 0-1 .646-1 1.199V17c0 .549.428 1.139.951 1.307l1.197.387C5.672 18.861 6.55 19 7.1 19h5.8c.549 0 1.428-.139 1.951-.307l1.196-.387c.524-.167.953-.757.953-1.306V9.199C17 8.646 16.352 8 15.8 8zM12 8H8V5.199C8 3.754 8.797 3 10 3c1.203 0 2 .754 2 2.199V8z"
                />
            </symbol>

            <symbol viewBox="0 0 20 20" id="close">
                <path d="M14.348 14.849c-.469.469-1.229.469-1.697 0L10 11.819l-2.651 3.029c-.469.469-1.229.469-1.697 0-.469-.469-.469-1.229 0-1.697l2.758-3.15-2.759-3.152c-.469-.469-.469-1.228 0-1.697.469-.469 1.228-.469 1.697 0L10 8.183l2.651-3.031c.469-.469 1.228-.469 1.697 0 .469.469.469 1.229 0 1.697l-2.758 3.152 2.758 3.15c.469.469.469 1.229 0 1.698z"
                />
            </symbol>

            <symbol viewBox="0 0 20 20" id="large-arrow">
                <path d="M13.25 10L6.109 2.58c-.268-.27-.268-.707 0-.979.268-.27.701-.27.969 0l7.83 7.908c.268.271.268.709 0 .979l-7.83 7.908c-.268.271-.701.27-.969 0-.268-.269-.268-.707 0-.979L13.25 10z"
                />
            </symbol>

            <symbol viewBox="0 0 20 20" id="large-arrow-down">
                <path d="M17.418 6.109c.272-.268.709-.268.979 0s.271.701 0 .969l-7.908 7.83c-.27.268-.707.268-.979 0l-7.908-7.83c-.27-.268-.27-.701 0-.969.271-.268.709-.268.979 0L10 13.25l7.418-7.141z"
                />
            </symbol>


            <symbol viewBox="0 0 24 24" id="jump-to">
                <path d="M19 7v4H5.83l3.58-3.59L8 6l-6 6 6 6 1.41-1.41L5.83 13H21V7z" />
            </symbol>

            <symbol viewBox="0 0 24 24" id="expand">
                <path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z" />
            </symbol>

        </defs>
    </svg>


    <div id="swagger-ui">
        <div data-reactroot="" class="swagger-ui">
            <div>
                <div class="information-container wrapper">
                    <section class="block col-12">
                        <div class="info">
                            <hgroup class="main">
                                <h2 class="title">httpbin.org
                                    <small>
                                        <pre class="version">0.9.2</pre>
                                    </small>
                                </h2>
                                <pre class="base-url">[ Base URL: httpbin.org/ ]</pre>
                            </hgroup>
                            <div class="description">
                                <div class="markdown">
                                    <p>A simple HTTP Request &amp; Response Service.
                                        <br>
                                        <br>
                                        <b>Run locally: </b>
                                        <code>$ docker run -p 80:80 kennethreitz/httpbin</code>
                                    </p>
                                </div>
                            </div>
                            <div>
                                <div>
                                    <a href="https://kennethreitz.org" target="_blank">the developer - Website</a>
                                </div>
                                <a href="mailto:me@kennethreitz.org">Send email to the developer</a>
                            </div>
                        </div>
                        <!-- ADDS THE LOADER SPINNER -->
                        <div class="loading-container">
                            <div class="loading"></div>
                        </div>

                    </section>
                </div>
            </div>
        </div>
    </div>


    <div class='swagger-ui'>
        <div class="wrapper">
            <section class="clear">
                <span style="float: right;">
                    [Powered by
                    <a target="_blank" href="https://github.com/rochacbruno/flasgger">Flasgger</a>]
                    <br>
                </span>
            </section>
        </div>
    </div>



    <script src="/flasgger_static/swagger-ui-bundle.js"> </script>
    <script src="/flasgger_static/swagger-ui-standalone-preset.js"> </script>
    <script src='/flasgger_static/lib/jquery.min.js' type='text/javascript'></script>
    <script>

        window.onload = function () {
            

            fetch("/spec.json")
                .then(function (response) {
                    response.json()
                        .then(function (json) {
                            var current_protocol = window.location.protocol.slice(0, -1);
                            if (json.schemes[0] != current_protocol) {
                                // Switches scheme to the current in use
                                var other_protocol = json.schemes[0];
                                json.schemes[0] = current_protocol;
                                json.schemes[1] = other_protocol;

                            }
                            json.host = window.location.host;  // sets the current host

                            const ui = SwaggerUIBundle({
                                spec: json,
                                validatorUrl: null,
                                dom_id: '#swagger-ui',
                                deepLinking: true,
                                jsonEditor: true,
                                docExpansion: "none",
                                apisSorter: "alpha",
                                //operationsSorter: "alpha",
                                presets: [
                                    SwaggerUIBundle.presets.apis,
                                    // yay ES6 modules ↘
                                    Array.isArray(SwaggerUIStandalonePreset) ? SwaggerUIStandalonePreset : SwaggerUIStandalonePreset.default
                                ],
                                plugins: [
                                    SwaggerUIBundle.plugins.DownloadUrl
                                ],
            
            // layout: "StandaloneLayout"  // uncomment to enable the green top header
        })

        window.ui = ui

        // uncomment to rename the top brand if layout is enabled
        // $(".topbar-wrapper .link span").replaceWith("<span>httpbin</span>");
        })
    })
}
    </script>  <div class='swagger-ui'>
    <div class="wrapper">
        <section class="block col-12 block-desktop col-12-desktop">
            <div>

                <h2>Other Utilities</h2>

                <ul>
                    <li>
                        <a href="/forms/post">HTML form</a> that posts to /post /forms/post</li>
                </ul>

                <br />
                <br />
            </div>
        </section>
    </div>
</div>
</body>

* Connection #0 to host httpbin.org left intact
```

Now inspect:

- HTTP status
- Headers
- Response
- Redirects

---

## Common TLS failures

### Certificate expired

- Fix certificate renewal/deployment.

### Hostname mismatch

- Certificate SAN does not contain the requested hostname.

### Unknown CA

- Client cannot build a trusted chain.

### Missing intermediate

- Server certificate chain is incomplete.

### TLS version mismatch

- Client and server cannot agree on a protocol version.

---

## curl -k

```bash
curl -k https://httpbin.org
```
Output:

```
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-12-tls-https/tls-lab$ curl -k https://httpbin.org
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>httpbin.org</title>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700|Source+Code+Pro:300,600|Titillium+Web:400,600,700"
        rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="/flasgger_static/swagger-ui.css">
    <link rel="icon" type="image/png" href="/static/favicon.ico" sizes="64x64 32x32 16x16" />
    <style>
        html {
            box-sizing: border-box;
            overflow: -moz-scrollbars-vertical;
            overflow-y: scroll;
        }

        *,
        *:before,
        *:after {
            box-sizing: inherit;
        }

        body {
            margin: 0;
            background: #fafafa;
        }
    </style>
</head>

<body>
    <a href="https://github.com/requests/httpbin" class="github-corner" aria-label="View source on Github">
        <svg width="80" height="80" viewBox="0 0 250 250" style="fill:#151513; color:#fff; position: absolute; top: 0; border: 0; right: 0;"
            aria-hidden="true">
            <path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path>
            <path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2"
                fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path>
            <path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z"
                fill="currentColor" class="octo-body"></path>
        </svg>
    </a>
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="position:absolute;width:0;height:0">
        <defs>
            <symbol viewBox="0 0 20 20" id="unlocked">
                <path d="M15.8 8H14V5.6C14 2.703 12.665 1 10 1 7.334 1 6 2.703 6 5.6V6h2v-.801C8 3.754 8.797 3 10 3c1.203 0 2 .754 2 2.199V8H4c-.553 0-1 .646-1 1.199V17c0 .549.428 1.139.951 1.307l1.197.387C5.672 18.861 6.55 19 7.1 19h5.8c.549 0 1.428-.139 1.951-.307l1.196-.387c.524-.167.953-.757.953-1.306V9.199C17 8.646 16.352 8 15.8 8z"></path>
            </symbol>

            <symbol viewBox="0 0 20 20" id="locked">
                <path d="M15.8 8H14V5.6C14 2.703 12.665 1 10 1 7.334 1 6 2.703 6 5.6V8H4c-.553 0-1 .646-1 1.199V17c0 .549.428 1.139.951 1.307l1.197.387C5.672 18.861 6.55 19 7.1 19h5.8c.549 0 1.428-.139 1.951-.307l1.196-.387c.524-.167.953-.757.953-1.306V9.199C17 8.646 16.352 8 15.8 8zM12 8H8V5.199C8 3.754 8.797 3 10 3c1.203 0 2 .754 2 2.199V8z"
                />
            </symbol>

            <symbol viewBox="0 0 20 20" id="close">
                <path d="M14.348 14.849c-.469.469-1.229.469-1.697 0L10 11.819l-2.651 3.029c-.469.469-1.229.469-1.697 0-.469-.469-.469-1.229 0-1.697l2.758-3.15-2.759-3.152c-.469-.469-.469-1.228 0-1.697.469-.469 1.228-.469 1.697 0L10 8.183l2.651-3.031c.469-.469 1.228-.469 1.697 0 .469.469.469 1.229 0 1.697l-2.758 3.152 2.758 3.15c.469.469.469 1.229 0 1.698z"
                />
            </symbol>

            <symbol viewBox="0 0 20 20" id="large-arrow">
                <path d="M13.25 10L6.109 2.58c-.268-.27-.268-.707 0-.979.268-.27.701-.27.969 0l7.83 7.908c.268.271.268.709 0 .979l-7.83 7.908c-.268.271-.701.27-.969 0-.268-.269-.268-.707 0-.979L13.25 10z"
                />
            </symbol>

            <symbol viewBox="0 0 20 20" id="large-arrow-down">
                <path d="M17.418 6.109c.272-.268.709-.268.979 0s.271.701 0 .969l-7.908 7.83c-.27.268-.707.268-.979 0l-7.908-7.83c-.27-.268-.27-.701 0-.969.271-.268.709-.268.979 0L10 13.25l7.418-7.141z"
                />
            </symbol>


            <symbol viewBox="0 0 24 24" id="jump-to">
                <path d="M19 7v4H5.83l3.58-3.59L8 6l-6 6 6 6 1.41-1.41L5.83 13H21V7z" />
            </symbol>

            <symbol viewBox="0 0 24 24" id="expand">
                <path d="M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z" />
            </symbol>

        </defs>
    </svg>


    <div id="swagger-ui">
        <div data-reactroot="" class="swagger-ui">
            <div>
                <div class="information-container wrapper">
                    <section class="block col-12">
                        <div class="info">
                            <hgroup class="main">
                                <h2 class="title">httpbin.org
                                    <small>
                                        <pre class="version">0.9.2</pre>
                                    </small>
                                </h2>
                                <pre class="base-url">[ Base URL: httpbin.org/ ]</pre>
                            </hgroup>
                            <div class="description">
                                <div class="markdown">
                                    <p>A simple HTTP Request &amp; Response Service.
                                        <br>
                                        <br>
                                        <b>Run locally: </b>
                                        <code>$ docker run -p 80:80 kennethreitz/httpbin</code>
                                    </p>
                                </div>
                            </div>
                            <div>
                                <div>
                                    <a href="https://kennethreitz.org" target="_blank">the developer - Website</a>
                                </div>
                                <a href="mailto:me@kennethreitz.org">Send email to the developer</a>
                            </div>
                        </div>
                        <!-- ADDS THE LOADER SPINNER -->
                        <div class="loading-container">
                            <div class="loading"></div>
                        </div>

                    </section>
                </div>
            </div>
        </div>
    </div>


    <div class='swagger-ui'>
        <div class="wrapper">
            <section class="clear">
                <span style="float: right;">
                    [Powered by
                    <a target="_blank" href="https://github.com/rochacbruno/flasgger">Flasgger</a>]
                    <br>
                </span>
            </section>
        </div>
    </div>



    <script src="/flasgger_static/swagger-ui-bundle.js"> </script>
    <script src="/flasgger_static/swagger-ui-standalone-preset.js"> </script>
    <script src='/flasgger_static/lib/jquery.min.js' type='text/javascript'></script>
    <script>

        window.onload = function () {
            

            fetch("/spec.json")
                .then(function (response) {
                    response.json()
                        .then(function (json) {
                            var current_protocol = window.location.protocol.slice(0, -1);
                            if (json.schemes[0] != current_protocol) {
                                // Switches scheme to the current in use
                                var other_protocol = json.schemes[0];
                                json.schemes[0] = current_protocol;
                                json.schemes[1] = other_protocol;

                            }
                            json.host = window.location.host;  // sets the current host

                            const ui = SwaggerUIBundle({
                                spec: json,
                                validatorUrl: null,
                                dom_id: '#swagger-ui',
                                deepLinking: true,
                                jsonEditor: true,
                                docExpansion: "none",
                                apisSorter: "alpha",
                                //operationsSorter: "alpha",
                                presets: [
                                    SwaggerUIBundle.presets.apis,
                                    // yay ES6 modules ↘
                                    Array.isArray(SwaggerUIStandalonePreset) ? SwaggerUIStandalonePreset : SwaggerUIStandalonePreset.default
                                ],
                                plugins: [
                                    SwaggerUIBundle.plugins.DownloadUrl
                                ],
            
            // layout: "StandaloneLayout"  // uncomment to enable the green top header
        })

        window.ui = ui

        // uncomment to rename the top brand if layout is enabled
        // $(".topbar-wrapper .link span").replaceWith("<span>httpbin</span>");
        })
    })
}
    </script>  <div class='swagger-ui'>
    <div class="wrapper">
        <section class="block col-12 block-desktop col-12-desktop">
            <div>

                <h2>Other Utilities</h2>

                <ul>
                    <li>
                        <a href="/forms/post">HTML form</a> that posts to /post /forms/post</li>
                </ul>

                <br />
                <br />
            </div>
        </section>
    </div>
</div>
</body>
```

This disables certificate verification.

Use it only as a diagnostic.

Do not use it as a production solution.

---

## Key learning

- If TCP succeeds but TLS fails:

- HTTP has not been reached yet.

- The troubleshooting order is:

- DNS → TCP → TLS → HTTP