# Lab 01 — Listening Port

## Objective

Understand how to identify a TCP listening port.

## Command

```bash
python3 -m http.server 8080

ss -lntp
```

## Observation

- Python was listening on port 8080.

- `ss -lntp` : Shows TCP ports currently listening and the processes usn them.

```bash
ss
│
├── -l → listening
├── -n → don't resolve names
├── -t → TCP
└── -p → process information
```
You get the output like below:

```bash                                                      
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days$ ss -lntp | grep 8080
LISTEN 0      5             0.0.0.0:8080      0.0.0.0:*    users:(("python3",pid=1990,fd=3))
```

## Why?

The Python HTTP server opened TCP port 8080
and waited for incoming connections.

## Learning

LISTEN means a process is waiting for incoming
TCP connections.