# Day 08 - HTTP Fundamentals

## Goal

Understand how HTTP communication works between a client and server and learn how to troubleshoot HTTP applications using curl.

## Topics Covered

- Client and Server
- HTTP Request
- HTTP Response
- HTTP Methods
- HTTP Headers
- HTTP Status Codes
- Query Parameters
- Request Body
- curl
- Local HTTP Server
- Basic HTTP Troubleshooting

## Tools Used

- curl
- Python HTTP Server
- ss
- ps

## Labs

1. Inspect HTTP response using curl
2. Send GET and POST requests
3. Inspect headers
4. Start a local HTTP server
5. Check listening ports
6. Troubleshoot connection failure

## Commands Learned

### Basic request

```bash
curl https://example.com
```

### Response headers

```bash
curl -I https://example.com
```

### Verbose request

```bash
curl -v https://example.com
```

### POST request

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{"name":"test"}' \
https://httpbin.org/post
```

### Check listening ports

```bash
ss -lntp
```

### Find HTTP server process

```bash
ps aux | grep http.server
```

## Key Learning

HTTP works using a request-response model.

Client sends:

```bash
Method + Path + Headers + Body
```

Server returns:

```bash
Status Code + Headers + Body
```
---

## Mistakes / Problems I Faced

### Problem 1

Command:

```bash
curl http://localhost:8080
```

Error:

```bash
Connection refused.
```

### Root Cause

Python `HTTP` server was not running.

### Fix

Started the server:

```bash
python3 -m http.server 8080
```

### Learning

Connection refused normally means nothing is accepting connections on the requested port.

---

## Interview Revision

### What is `HTTP`?

HTTP is an application-layer protocol used for request-response communication between clients and servers.

### What is `503`?

503 means Service Unavailable.

In `Kubernetes` I would check:

- Pod health
- Readiness probes
- Service endpoints
- Service selectors
- Ingress configuration

### What is the difference between `503` and `connection refused`?

503 means I successfully reached an HTTP server or gateway and it returned an HTTP response.

Connection refused means a `TCP connection` could not be established, commonly because nothing is listening on the `target port`.