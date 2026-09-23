# TLS Handshake

## 1. Where does TLS happen?

**HTTPS:**

```bash
DNS
 ↓
TCP handshake
 ↓
TLS handshake
 ↓
HTTP
```

TCP must be established before the TLS handshake can proceed.

---

## 2. Simplified TLS 1.3 handshake

```bash
Client                         Server

ClientHello -------------------->

                         ServerHello
                         Certificate
                         CertificateVerify
                         Finished

Finished ----------------------->
```
The exact exchange can contain additional messages/extensions.

---

## 3. ClientHello

The client can communicate:

- Supported TLS versions
- Cryptographic capabilities
- Key-share information
- SNI
- ALPN

---

## 4. ServerHello

The server selects parameters for the connection.

---

## 5. Certificate

The server presents its certificate chain.

The client validates it.

---

## 6. CertificateVerify

The server proves possession of the private key corresponding to the certificate.

---

## 7. Finished

Both sides confirm the handshake.

After successful TLS establishment:

HTTP application data can be protected.

---

## 8. SNI

SNI:

`Server Name Indication`

SNI allows the client to indicate the hostname it wants.

This is important when multiple HTTPS sites share an IP address.

Example:

10.10.10.10

    |
    +-- example.com
    |
    +-- api.example.com

---

## 9. ALPN

ALPN:

`Application-Layer Protocol Negotiation`

It can negotiate protocols such as:

```
http/1.1
h2
```

---

## 10. TLS 1.2 vs TLS 1.3

For Day 12, understand the high level:

```
TLS 1.2:
Older protocol version still encountered.

TLS 1.3:
Newer protocol version with a more streamlined handshake and modern cryptographic design.
```

---

## Key learning

- TCP establishes the transport connection.

- TLS establishes the secure cryptographic context.

- Then HTTP can operate over the protected connection.