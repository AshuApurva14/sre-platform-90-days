# TLS Failure

## Symptom

HTTPS connection fails during TLS handshake.

---

## Test

```bash
openssl s_client \
  -connect <host>:443 \
  -servername <host>
```

## Check

```
Certificate validity
SAN
Issuer
Trust chain
TLS version
SNI
Cipher compatibility
```

## Common Causes

- Expired certificate

- Hostname mismatch

- Unknown CA

- Missing intermediate

- TLS version mismatch


## Verification

- TLS handshake succeeds and certificate validates.