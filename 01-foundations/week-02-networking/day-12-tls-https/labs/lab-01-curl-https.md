# Lab 1 - HTTPS iwth curl

Start:
```
curl -v https://example.com
```

Don't just run the command.

Find these pieces:

```
DNS resolution
       ↓
TCP connection
       ↓
TLS handshake
       ↓
Certificate
       ↓
HTTP response
```

Write down:

```
IP:  104.20.23.154, 172.66.147.243
TCP: Connection OK
TLS version: TLSv1.3
Certificate: ok
HTTP status: 200
```

<img width="2275" height="1288" alt="Image" src="https://github.com/user-attachments/assets/47724d8e-aa54-40cc-878c-7d94dc1072a5" />
---

Important learning

`curl -v` is not just an HTTP command.

It helps you see what happens underneath HTTP.