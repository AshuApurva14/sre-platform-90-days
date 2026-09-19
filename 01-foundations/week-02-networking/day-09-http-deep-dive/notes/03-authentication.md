# Authentication and Authorization

## Authentication

Authentication answers:

```bash
"Who are you?"
```

Examples:

- Username/password
- API key
- OAuth token
- JWT
- Client certificate

## Authorization

Authorization answers:

```ash
"What are you allowed to do?"
```

Simple example:

```bash
User
 |
 | Login
 v
Authentication
 |
 | Identity confirmed
 v
Authorization
 |
 | Is this user allowed?
 v
Resource
```

Remember:

```bash
Authentication = identity

Authorization = permissions

```

## Basic Authentication

Command:

```bash
curl -i -u testuser:testpass \
https://httpbin.org/basic-auth/testuser/testpass

```

The `-u` option supplies `username` and `password.`

<img width="1639" height="395" alt="Image" src="https://github.com/user-attachments/assets/3c413e06-5e76-4b86-8eff-869588c09060" />

Important:

```bash
Basic authentication should be protected by HTTPS in real systems.

```

## Bearer Token

Bearer authentication sends a token using the Authorization header.

Example:

```bash
Authorization: Bearer <token>
            or

Authorization: Bearer eyJ..
```

Meaning:

```bash
Client
  |
  | Authorization: Bearer <token>
  v
API
```

The token represents the client's authenticated access.

Try:

```bash
curl -i \
  -H "Authorization: Bearer my-demo-token" \
  https://httpbin.org/get
```

The server will reflect the authorization header.

<img width="1389" height="609" alt="Image" src="https://github.com/user-attachments/assets/83872975-f7ca-4969-9bc2-a0ec19d73f10" />

---

**Never put real production tokens in your Git repository or screenshots.**

Use fake values like:

```bash
my-demo-token
```