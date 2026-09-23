# Encryption, Integrity and Authentication

## 1. Confidentiality

Confidentiality means unauthorized people should not be able to read protected communication.

Example:

Client:

```bash
username=alice
password=secret
```

TLS:

```bash
encrypted/protected data
```
---

## 2. Integrity

Integrity means the communication can be protected against undetected modification.

Conceptually:

```bash
Sender
  |
Protected data
  |
Network
  |
Receiver
  |
Integrity verification
```

---

## 3. Authentication

Authentication answers:

```bash
"Who am I communicating with?"
```

In normal `HTTPS`, the `server` `presents` a `certificate.`

The `client` `validates` the `certificate`.`

---

## 4. These concepts are different

`Confidentiality:`

**Can someone read the data?**

`Integrity:`

**Was the data modified?**

`Authentication:`

**Who is the server?**

---

## 5. Symmetric encryption

**Symmetric cryptography** uses a shared secret key.

Conceptually:

```bash
Key
 ↓
Encrypt
 ↓
Ciphertext
 ↓
Decrypt
 ↓
Same secret
```

**Symmetric cryptography** is efficient for large amounts of application data.

---

## 6. Asymmetric cryptography

**Asymmetric cryptography** uses:

```bash
Public key
Private key
```

The private key must remain secret.

The public key can be distributed.

TLS uses `asymmetric` cryptography/signatures during connection establishment and `symmetric` cryptography for efficient application-data protection.

---

## 7. DevOps security rule

Never:

- Commit private keys to Git
- Print private keys in CI logs
- Put private keys in tickets
- Share private keys in chat

Use appropriate secret-management systems.

Examples:

- Kubernetes Secrets
- HashiCorp Vault
- Cloud secret managers
- Enterprise PKI

---

## Key learning

```bash
Confidentiality → prevent unauthorized reading

Integrity → detect unauthorized modification

Authentication → establish identity
```
