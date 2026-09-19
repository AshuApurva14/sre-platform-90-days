# Cookies

## Understand the basic flow:


```bash
Server
  |
  | Set-Cookie
  v
Browser
  |
  | Cookie
  v
Server

```

A server might return:

```bash
Set-Cookie: session_id=abc123
```

The browser stores it and later sends:

```bash
Cookie: session_id=abc123
```

Run:

```bash
curl -i \
  https://httpbin.org/cookies/set/session_id/abc123

```

<img width="2523" height="483" alt="Image" src="https://github.com/user-attachments/assets/82e521aa-3471-4c7d-ae24-e1a0d376ab22" />
---

Then use curl's cookie handling:

```bash
curl -c cookies.txt \
  -b cookies.txt \
  -L \
  https://httpbin.org/cookies/set/session_id/abc123
```

Check:

```bash
cat cookies.txt
```

You should see cookie information.

<img width="1774" height="460" alt="Image" src="https://github.com/user-attachments/assets/b48ab118-6e26-4da3-935f-cf374b767585" />

---

## Cookie Jar

```bash
-c cookies.txt
```

Save cookies.

```bash
-b cookies.txt
```

Send cookies from the file.

Cookies can be used to maintain state between HTTP requests.


## Understand sessions

HTTP itself is fundamentally stateless.

That means:

```bash
Request 1
Request 2
Request 3
```

are separate HTTP requests.

Applications can create state using mechanisms such as:

```bash
Cookies
Sessions
Tokens
Databases

```

Example:

```bash
Login
 ↓
Server creates session
 ↓
Session ID sent to client
 ↓
Client sends session ID with future requests

```

