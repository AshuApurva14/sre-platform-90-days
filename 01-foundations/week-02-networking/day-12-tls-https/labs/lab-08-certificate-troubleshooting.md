# Lab 8: Certificate troubleshooting

Run:

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
* connect to ::1 port 4443 from ::1 port 60766 failed: Connection refused
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

Then:

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
* connect to ::1 port 4443 from ::1 port 51834 failed: Connection refused
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
< Date: Wed, 23 Sep 2026 03:17:34 GMT
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
Ask yourself:

Question 1

```
Did TCP connect? - Yes
```

Question 2

```
Did TLS negotiate? - Yes
```

Question 3

```
Why did certificate verification fail? - Because the cert is Self signed certificate
```

Question 4

```
Who issued my certificate? localhost issued the certificate
```
Run:

```bash
openssl s_client \
  -connect localhost:4443 \
  -servername localhost </dev/null 2>/dev/null \
  | openssl x509 -noout -issuer

```
Output:

```
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days$ openssl s_client -connect localhost:4443 -servername localhost </dev/null 2>/dev/null | openssl x509 -noout -issuer
issuer=CN = localhost
```
Question 5

Is it trusted?

```
No, because you created a self-signed certificate that your normal trust store doesn't automatically trust.
```