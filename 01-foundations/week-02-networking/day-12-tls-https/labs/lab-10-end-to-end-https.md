# Lab 10: Complete HTTPS troubleshooting

This is the most important lab of Day 12.

Imagine:

```
https://app.example.com
```
is not working.

Don't randomly run commands.

Use your layers.

Step 1 — `DNS`

```bash
dig httpbin.org
```

Ask:

Does it resolve?

Step 2 — `TCP`

```bash
nc -vz httpbin.org 443
```

Ask:

Can I establish TCP connectivity?

Step 3 — `TLS`

```bash

openssl s_client \
  -connect httpbin.org:443 \
  -servername httpbin.org
```

Ask:

Did TLS handshake succeed?

Step 4 — `Certificate`

```bash
openssl s_client \
  -connect httpbin.org:443 \
  -servername httpbin.org </dev/null 2>/dev/null \
  | openssl x509 \
      -noout \
      -subject \
      -issuer \
      -dates \
      -ext subjectAltName
```

Ask:

```
Expired?
Hostname?
Issuer?
SAN?
```

Step 5 — `HTTP`

```bash
curl -v https://httpbin.org
```

Now inspect:

```
HTTP status
Headers
Response
Redirect
```