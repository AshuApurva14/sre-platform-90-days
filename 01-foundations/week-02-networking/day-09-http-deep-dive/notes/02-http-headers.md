# HTTP Headers

`HTTP` headers provide metadata about an HTTP request or response.

`Headers` are `key-value` pairs.

Example:
```bash
Content-Type: application/json
Accept: application/json
User-Agent: curl
```

Now divide them:

```bash
Request headers
        |
        v
Client → Server


Response headers
        |
        v
Server → Client
```

## Request headers lab

Run:
```bash
curl -v https://httpbin.org/get
```
Look at:
```bash
> GET /get
> Host:
> User-Agent:
> Accept:
```

Check the response.

<img width="1573" height="1620" alt="Image" src="https://github.com/user-attachments/assets/7fa8f1a4-fe23-4dec-8ec7-09978f9f1139" />

You should see the headers reflected.

## Custom Headers

Now explicitly set headers:

Command:

```bash
curl -i \
-H "Accept: application/json" \
-H "X-Environment: test" \
https://httpbin.org/get
```

Check the response:

<img width="1569" height="677" alt="Image" src="https://github.com/user-attachments/assets/c78b9383-66f1-42f6-a43d-fb38b0e84584" />

Learning:

Custom headers allow clients to send additional metadata to servers.


## Understand Content-Type

This one is particularly important for your API/Kubernetes work.

You already encountered:

```bash
Content-Type: application/json
```

Understand:

```bash
Content-Type
     ↓
What format is the body?
```

Examples:

```bash
application/json
text/plain
text/html
application/xml
application/x-www-form-urlencoded
multipart/form-data
```

## Content-Type

Content-Type describes the media type of the message body.

Example:

```bash
Content-Type: application/json
```

means the body is JSON.

## Understand Accept

This is different.

```bash

Content-Type
     ↓
What am I sending?

Accept
     ↓
What response format do I want?
```

Example:

```bash
Content-Type: application/json
Accept: application/json
```

Think:

```bash
Client → "I'm sending JSON."

Client → "Please return JSON."
```