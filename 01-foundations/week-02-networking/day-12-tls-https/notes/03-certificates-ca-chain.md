# TLS Certificates, CA and Certificate Chains

## 1. What is a TLS certificate?

A `TLS certificate` is a digitally signed document containing identity information and public-key information.

Important fields include:

- Subject
- Subject Alternative Name
- Public key
- Issuer
- Valid-from date
- Expiry date
- Signature
- Extensions

---

## 2. SAN

SAN means:

`Subject Alternative Name`

Example:

```bash
DNS:example.com
DNS:www.example.com
DNS:api.example.com
```

Modern hostname validation relies on SAN.

---

## 3. Certificate Authority

CA means:

```
Certificate Authority
```

A CA signs certificates.

Simplified:

```
Root CA
   |
   v
Intermediate CA
   |
   v
Server Certificate
```
---

## 4. Root CA

A Root CA is a trust anchor.

Operating systems and browsers maintain trusted CA certificates.

---

## 5. Intermediate CA

An intermediate CA sits between the root CA and the server certificate.

Example:

```
Root CA
   ↓
Intermediate CA
   ↓
api.example.com
```
---

## 6. Certificate chain

A client may validate:

```
Server certificate
       ↓
Intermediate CA
       ↓
Trusted Root CA
```
The server normally sends its certificate and required intermediate certificates.

---

## 7. Certificate validation

A client commonly checks:

1. Is the certificate currently valid?
2. Does the hostname match?
3. Can the chain reach a trusted CA?
4. Are required extensions/key usages appropriate?
5. Are there other verification failures?

---

## 8. Common errors

### Expired certificate
```
Certificate validity period has ended.
```
### Hostname mismatch

Requested:

```
api.example.com
```
Certificate:

```
www.example.com
```
### Unknown CA

The client does not trust the certificate chain.

### Missing intermediate

The server does not provide a required intermediate certificate.

---

## Key learning

Certificate:

```
Identity + public key + signed information
```
CA:
```
Trusted entity that signs certificates
```
Chain:
```
Server certificate → Intermediate → Trusted Root
```