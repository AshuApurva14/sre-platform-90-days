# Lab 03 - Local HTTP Server

## Objective

Run my own HTTP server and communicate with it using curl.

## Setup index.html file
```bash
echo "Hello from Day 8" > index.html
```
## Start Server

```bash
python3 -m http.server 8080
```

<img width="1454" height="264" alt="Image" src="https://github.com/user-attachments/assets/52832284-5404-46fd-ad5d-ac1d2a5fe7c4" />

<img width="1261" height="119" alt="Image" src="https://github.com/user-attachments/assets/42226c6a-86b5-4322-86e6-2afd5c5fd467" />

### Meaning

Python started an `HTTP` server listening on `TCP` port `8080`.

---

## Understanding localhost

localhost represents my own machine.

It normally resolves to:

```bash
127.0.0.1
```

## Understanding Port

The server is listening on:

```bash
8080
```

Simple mental model:

```bash
IP Address = which machine

Port = which application/service
```

## Verify Listening Port

Command:

```bash
ss -lntp | grep 8080
```

### Observation


Python is listening on port `8080.`

### Learning

`ss` can be used to identify applications listening on TCP ports.

Also run:

```bash
ps aux | grep http.server
```

Now connect the pieces:

```bash
Process
   ↓
Python
   ↓
Listening port
   ↓
8080
   ↓
HTTP server

```
<img width="1232" height="180" alt="Image" src="https://github.com/user-attachments/assets/f7c5fc01-bcd1-48e5-8fff-6b16b63668b1" />

## Failure Test

Server stopped.

Command:

```bash
curl http://localhost:8080
```

Result:

```bash
Connection refused.
```

## Why?

- There is no application listening on TCP port `8080.`

- This is NOT an `HTTP 404` or `HTTP 500` error.

- The HTTP request could not even reach an HTTP server.

- Below is the error you get:
 ```bash
 curl: (7) Failed to connect to localhost port 8080 after 0 ms: Couldn't connect to server
 ```