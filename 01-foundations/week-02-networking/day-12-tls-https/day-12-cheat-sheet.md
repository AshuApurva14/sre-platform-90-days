# TLS / HTTPS CHEAT SHEET

`HTTPS = HTTP over TLS`

Flow:
```
DNS
 ↓
TCP
 ↓
TLS
 ↓
HTTP
```
TLS provides:
```
Confidentiality
Integrity
Authentication
```
Certificate:
```
Identity
+
Public key
+
CA signature
```
Chain:
```
Server certificate
       ↓
Intermediate CA
       ↓
Trusted Root CA
```
Important:
```
SAN = hostname validation
SNI = hostname sent during TLS negotiation
ALPN = application protocol negotiation
```
Tools:
```
curl -v https://HOST

openssl s_client \
  -connect HOST:443 \
  -servername HOST

openssl x509
```

Troubleshooting:
```
DNS
 ↓
TCP 443
 ↓
TLS
 ↓
Certificate
 ↓
HTTP
```

Common failures:

- Expired certificate
- Hostname mismatch
- Unknown CA
- Missing intermediate
- TLS version mismatch
- Handshake failure

Kubernetes:

```
F5
 ↓
Ingress
 ↓
Service
 ↓
Pod
```

First question:
```
Where does TLS terminate?
```