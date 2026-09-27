# HTTP Troubleshooting

Run:

```bash
curl -v https://example.com
```

Observe:

```
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days$ curl -v https://example.com
* Host example.com:443 was resolved.
* IPv6: 2606:4700:8d95:72db:f20c:548:ef6b:ff98
* IPv4: 104.20.23.154, 172.66.147.243
*   Trying 104.20.23.154:443...
* Connected to example.com (104.20.23.154) port 443
* ALPN: curl offers h2,http/1.1
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
*  CAfile: /etc/ssl/certs/ca-certificates.crt
*  CApath: /etc/ssl/certs
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384 / X25519 / id-ecPublicKey
* ALPN: server accepted h2
* Server certificate:
*  subject: CN=example.com
*  start date: Sep 26 22:49:11 2026 GMT
*  expire date: Dec 25 22:56:35 2026 GMT
*  subjectAltName: host "example.com" matched cert's "example.com"
*  issuer: C=US; O=SSL Corporation; CN=Cloudflare TLS Issuing ECC CA 3
*  SSL certificate verify ok.
*   Certificate level 0: Public key type EC/prime256v1 (256/128 Bits/secBits), signed using ecdsa-with-SHA256
*   Certificate level 1: Public key type EC/prime256v1 (256/128 Bits/secBits), signed using ecdsa-with-SHA384
*   Certificate level 2: Public key type EC/secp384r1 (384/192 Bits/secBits), signed using ecdsa-with-SHA384
*   Certificate level 3: Public key type EC/secp384r1 (384/192 Bits/secBits), signed using ecdsa-with-SHA384
* using HTTP/2
* [HTTP/2] [1] OPENED stream for https://example.com/
* [HTTP/2] [1] [:method: GET]
* [HTTP/2] [1] [:scheme: https]
* [HTTP/2] [1] [:authority: example.com]
* [HTTP/2] [1] [:path: /]
* [HTTP/2] [1] [user-agent: curl/8.5.0]
* [HTTP/2] [1] [accept: */*]
> GET / HTTP/2
> Host: example.com
> User-Agent: curl/8.5.0
> Accept: */*
> 
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* old SSL session ID is stale, removing
< HTTP/2 200 
< date: Sun, 27 Sep 2026 02:25:37 GMT
< content-type: text/html
< server: cloudflare
< last-modified: Sat, 26 Sep 2026 09:10:30 GMT
< allow: GET, HEAD
< accept-ranges: bytes
< age: 11409
< cf-cache-status: HIT
< cf-ray: a4170f10393cf4d3-IXC
< 
<!doctype html><html lang="en"><head><title>Example Domain</title><link rel="icon" href="data:,"><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{background:#eee;width:60vw;margin:15vh auto;font-family:system-ui,sans-serif}h1{font-size:1.5em}div{opacity:0.8}a:link,a:visited{color:#348}</style></head><body><div><h1>Example Domain</h1><p>This domain is for use in documentation examples without needing permission. Avoid use in operations.</p><p><a href="https://iana.org/domains/example">Learn more</a></p></div></body></html>
* Connection #0 to host example.com left intact

```


Then interpret status.

`200`
```
Request succeeded
```

`301/302`

```
Redirect
```

`401`

```
Authentication required/failed
```

`403`

```
Request understood,
but access denied
```

`404`

```
Resource/path not found
```

`502`

Usually:

```
Proxy/LB/Ingress
       ↓
couldn't get a valid upstream response
```

`503`

Usually:

```
Service unavailable
```

`504`

Usually:

```
Gateway/proxy timed out waiting for upstream
```