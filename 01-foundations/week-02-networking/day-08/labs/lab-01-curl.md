# Lab 01 - HTTP with curl

## Objective

Use curl to understand HTTP requests and responses.

## Environment

OS:
Linux

Tools:

- curl
- Internet connection

## Verify curl

Command:

```bash
curl --version
```
Result:

```bash

curl is installed and available.

curl 8.5.0 (x86_64-pc-linux-gnu) libcurl/8.5.0 OpenSSL/3.0.13 zlib/1.3 brotli/1.1.0 zstd/1.5.5 libidn2/2.3.7 libpsl/0.21.2 (+libidn2/2.3.7) libssh/0.10.6/openssl/zlib nghttp2/1.59.0 librtmp/2.3 OpenLDAP/2.6.10
```

## Perform your first `curl` request

Run:

```bash
curl https://www.google.com
```

## Test 1 - Basic GET Request

Command:

curl https://www.google.com

### Observation

The server returned HTML content.

### What Happened

curl acted as the HTTP client.

example.com acted as the HTTP server.

curl sent an HTTP GET request.

The server returned an HTTP response containing HTML.


Document:
```bash
Command
Observation
Explanation
```
That is how your notes become useful.

## Inspect HTTP headers

## Test 2 - Inspect Response Headers

Command:

curl -I https://example.com

Example response:

HTTP/2 200
content-type: text/html
content-length: ...

### Observation

The HTTP status code was 200.

The response Content-Type was text/html.

### Learning

- curl -I retrieves response headers without downloading the complete response body.
- The response has all details about the date,time,cache, content type and security policies.

<img width="2689" height="336" alt="Image" src="https://github.com/user-attachments/assets/4a8b2c03-a4ea-4cd9-9def-041e14a568b7" />

---

## Perform verbose 

Run:
```bash
curl -v https://example.com
```
Don't panic when you see lots of output.

Focus on:
```bash
> GET /
> Host:
> User-Agent:
> Accept:

< HTTP/...
< content-type:
```
Add to your lab:

## Test 3 - Verbose HTTP Request

Command:

curl -v https://example.com

### Important Output

> GET / HTTP/...
> Host: example.com
> User-Agent: curl/...

< HTTP/... 200
< content-type: text/html

### Understanding

Lines starting with:
```bash
> represent data sent by the client.
```
Lines starting with:
```bash
< represent data returned by the server.
```
<img width="2702" height="785" alt="Image" src="https://github.com/user-attachments/assets/ad68b476-bd72-4cb3-b5c0-11544d1b8625" />

This is extremely important for your future troubleshooting work.

