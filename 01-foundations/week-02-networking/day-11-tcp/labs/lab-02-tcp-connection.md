## Lab 02 - `TCP` connections

Run:

```bash
curl http://localhost:8080
```
You should see HTML directory listing.

```bash
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days$ curl http://localhost:8080
<!DOCTYPE HTML>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Directory listing for /</title>
</head>
<body>
<h1>Directory listing for /</h1>
<hr>
<ul>
<li><a href="day-11-mental-model.md">day-11-mental-model.md</a></li>
<li><a href="labs/">labs/</a></li>
<li><a href="notes/">notes/</a></li>
<li><a href="README.md">README.md</a></li>
<li><a href="screenshots/">screenshots/</a></li>
</ul>
<hr>
</body>
</html>
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days$ 
```

## Visual model

```bash
curl
 ↓
localhost
 ↓
TCP connection
 ↓
port 8080
 ↓
Python HTTP server
 ↓
HTTP response
```

## Check Established TCP Connections

Run:

```bash
ss -ant
```

You may see:

<img width="2362" height="248" alt="Image" src="https://github.com/user-attachments/assets/59317531-48e6-4468-a799-2b8fb7024446" />

---

## What does LISTEN mean?

If you see:

```bash
LISTEN 0 128 0.0.0.0:8080
```

it means:

A process has opened port 8080 and is waiting for incoming `TCP connections`.

For example:

```bash
Spring Boot
     │
     ↓
LISTEN :8080
```

If nobody is listening:

```bash
No process
     ↓
:8080
```

and a client attempting to connect may receive:

```bash
Connection refused
```