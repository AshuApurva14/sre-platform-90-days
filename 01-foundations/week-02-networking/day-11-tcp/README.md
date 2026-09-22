# Day 11 — TCP Fundamentals

## Objective

Understand TCP from a DevOps troubleshooting perspective.

## Concepts

1. TCP basics
2. IP addresses, ports and sockets
3. TCP three-way handshake
4. TCP sockets and connection states
5. TCP vs UDP
6. TCP troubleshooting

## Labs

The concepts should be reinforced with:

- `python3 -m http.server`
- `ss -lntp`
- `ss -ant`
- `nc -vz`
- Netcat client/server
- `curl`
- Connection refused troubleshooting

## Core mental model

```text
DNS
 ↓
IP
 ↓
TCP
 ↓
TLS
 ↓
HTTP
 ↓
Application
```

## Most important TCP concept

```text
Client                 Server

  SYN -------------------->

  <---------------- SYN-ACK

  ACK -------------------->

       TCP ESTABLISHED
```

## DevOps commands

```bash
ss -lntp
ss -antp
nc -vz HOST PORT
curl -v URL
```

## Documentation method

For every lab:

```text
Objective
Command
Output
Observation
Why?
Learning
```

## Success criteria

Before moving to Day 12, explain:

- TCP
- IP vs port
- Socket
- Listening port
- Ephemeral port
- SYN/SYN-ACK/ACK
- TCP vs UDP
- `ss`
- `nc`
- Connection refused
- Connection timeout
- Why ping does not test TCP
- TCP troubleshooting
- Kubernetes Service/targetPort relationship
