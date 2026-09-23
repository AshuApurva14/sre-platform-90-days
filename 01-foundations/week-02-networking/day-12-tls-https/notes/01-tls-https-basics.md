# TLS and HTTPS Basics

## 1. What is TLS?

TLS stands for:

`Transport Layer Security`

TLS protects communication between two endpoints.

TLS provides three important security properties:

1. Confidentiality
2. Integrity
3. Authentication

---

## 2. What is HTTPS?

HTTPS means:

HTTP over TLS.

Simplified:

```bash
Client
  |
  | HTTPS
  |
  v
TLS
  |
  v
TCP
  |
  v
IP
```

For a traditional HTTPS connection:

```bash
DNS
 ↓
TCP handshake
 ↓
TLS handshake
 ↓
HTTP request
 ↓
HTTP response
```
---

## 3. HTTP vs HTTPS

HTTP:

```bash
Client ---- HTTP ----> Server
```

HTTPS:

```bash
Client ---- TLS-protected HTTP ----> Server
```

HTTPS protects the HTTP communication channel.

---

## 4. Default ports

HTTP:

80

HTTPS:

443

---

## 5. Why TLS?

TLS protects sensitive information such as:

- Passwords
- Session cookies
- API tokens
- Personal information
- Application requests
- Application responses

---

## 6. TLS provides confidentiality

Encryption prevents unauthorized parties from easily reading protected traffic.

Example:
```bash
username=alice
password=secret
```
becomes protected/encrypted TLS data.

---

## 7. TLS provides integrity

TLS helps detect unauthorized modification of protected data.

---

## 8. TLS provides authentication

The server normally presents a certificate.

The client validates the certificate.

This helps verify that the server is authorized for the requested hostname.

---

## 9. DevOps mental model

When HTTPS fails:

```bash
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

Do not immediately assume that an HTTP problem is the cause.

---

## Key learning

`HTTPS = HTTP protected by TLS`.

Remember:

```bash
DNS → TCP → TLS → HTTP
```