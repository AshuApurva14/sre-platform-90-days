# Day 11 interview questions

Don't memorize answers yet. Try answering them yourself.

Beginner
```bash
What is TCP?
What is a port?
What is a socket?
What is the difference between IP and port?
What is a TCP connection?
What is the TCP three-way handshake?
What is SYN?
What is SYN-ACK?
What is ACK?
What does LISTEN mean?
``

DevOps level
```bash
How do you check listening TCP ports in Linux?
How do you test whether port 443 is reachable?
What does connection refused mean?
What can cause a TCP timeout?
Does ping test TCP?
How do you troubleshoot an application that is not reachable?
What is an ephemeral port?
TCP vs UDP?
How does TCP relate to HTTP?
How does TCP relate to Kubernetes Services?
```

Scenario

Imagine:

```bash
User
 ↓
F5
 ↓
Ingress
 ↓
Service
 ↓
Pod
```

Application is running but users receive:
```bash
Connection timeout
```

Walk through your investigation.

Start:

```bash
DNS
 ↓
IP
 ↓
TCP
 ↓
F5
 ↓
Ingress
 ↓
Service
 ↓
Pod
 ↓
Application
```

Don't immediately jump to Kubernetes.