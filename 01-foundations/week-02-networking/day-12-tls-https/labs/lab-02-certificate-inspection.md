# Lab 2: Certificate inspection

Run:

```BASH
openssl s_client \
  -connect example.com:443 \
  -servername example.com
```

Look for:

```bash
Certificate chain
Server certificate
Protocol
Cipher
Verify
```

Then:

```
openssl s_client \
  -connect example.com:443 \
  -servername example.com </dev/null 2>/dev/null \
  | openssl x509 -noout -subject -issuer -dates
```

Then:

```
openssl s_client \
  -connect example.com:443 \
  -servername example.com </dev/null 2>/dev/null \
  | openssl x509 -noout -ext subjectAltName

```
Record:

```
Subject: CN = example.com
Issuer: C = US, O = SSL Corporation, CN = Cloudflare TLS Issuing ECC CA 3
Valid From: Jul 26, 2026
Valid Until: Oct 27 2026
SAN: DNS:example.com, DNS:*.example.com
```

<img width="1669" height="1601" alt="Image" src="https://github.com/user-attachments/assets/792409ef-9a9b-4551-9cb5-5d20246b7f39" />

<img width="1317" height="423" alt="Image" src="https://github.com/user-attachments/assets/856053ca-7d7d-4b55-b739-9c51faf70901" />

---
