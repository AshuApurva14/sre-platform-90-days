# Understand DNS + HTTPS

Suppose you have:

```bash
https://api.company.com
```

Conceptually:


1. DNS

```bash
api.company.com
       ↓
IP address
```

2. TCP

```bash
Client
   ↓
Server
```

3. TLS

```bash
Certificate + encryption
```
4. HTTP

```bash
GET /api/orders
```

Today you only need to understand that DNS comes first in this simplified flow.
