# Lab 5: Test TLS versions

Test TLS 1.2:

```bash
openssl s_client \
  -connect example.com:443 \
  -servername example.com \
  -tls1_2
```

Then:

```bash
openssl s_client \
  -connect example.com:443 \
  -servername example.com \
  -tls1_3
```

Record:

```
TLS 1.2 → Success/Failure
TLS 1.3 → Success/Failure

TLS 1.2 - Success
TLS 1.2 - Success
```

Don't interpret failure automatically as a server bug.

Protocol policies can intentionally disable versions.