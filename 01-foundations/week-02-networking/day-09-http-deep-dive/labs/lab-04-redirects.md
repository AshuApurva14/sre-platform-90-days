# Lab 04 - HTTP Redirects

## Objective

Understand HTTP redirects and how curl handles them.

## Test

```bash
curl -I http://httpbin.org/redirect/1
```

## Follow Redirect

```bash
curl -L http://httpbin.org/redirect/1
```

## Learning


The server can tell the client to request another URL.

```bash
curl -L follows redirects automatically.
```
