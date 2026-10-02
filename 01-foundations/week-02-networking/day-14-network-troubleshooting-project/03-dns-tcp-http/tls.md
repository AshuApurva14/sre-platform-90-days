# TLS Lab

## Objective

Understand HTTPS and TLS troubleshooting.

---

## Test HTTPS

```bash
curl -v https://example.com
```

### Inspect Certificate:

Look for:

```
Subject
Issuer
Validity
SAN
TLS version
Cipher
Verification
```

### SAN

Subject Alternative Name contains the hostnames for which the certificate is valid.

### SNI

Server Name Indication allows the client to indicate the hostname during TLS negotiation.
```
Common TLS Failures
Certificate expired
Hostname mismatch
Unknown CA
Missing intermediate certificate
TLS version mismatch
Handshake failure
```

### Troubleshooting Tools


- `curl -v`

- `openssl s_client`

- `openssl x509`
