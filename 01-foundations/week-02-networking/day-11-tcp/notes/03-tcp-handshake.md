# TCP Three-Way Handshake

## 1. Why does TCP need a handshake?

TCP is connection-oriented.

Before normal application data is exchanged, the client and server establish a TCP connection.

The connection is normally established using three steps:

```text
SYN
SYN-ACK
ACK
```

## 2. Step 1 — SYN

The client sends a SYN packet.

```text
Client ---------------- SYN ----------------> Server
```

Meaning:

> I want to establish a TCP connection.

SYN stands for **Synchronize**.

## 3. Step 2 — SYN-ACK

The server responds:

```text
Client <------------- SYN-ACK --------------- Server
```

Meaning approximately:

> I received your request and I am willing to establish the connection.

The server acknowledges the client's SYN and sends its own synchronization information.

## 4. Step 3 — ACK

The client responds:

```text
Client ---------------- ACK ----------------> Server
```

Meaning:

> I received your response.

The TCP connection can now be considered established.

## 5. Complete handshake

```text
Client                              Server

   |                                  |
   | ----------- SYN ---------------> |
   |                                  |
   | <---------- SYN-ACK ------------ |
   |                                  |
   | ----------- ACK ---------------> |
   |                                  |
   |       CONNECTION ESTABLISHED     |
   |                                  |
```

Remember:

> SYN → SYN-ACK → ACK

## 6. What happens after the handshake?

Application data can now be exchanged.

For HTTPS:

```text
DNS
 ↓
TCP SYN
 ↓
TCP SYN-ACK
 ↓
TCP ACK
 ↓
TLS handshake
 ↓
HTTP request
 ↓
HTTP response
```

TLS is covered separately.

## 7. How can we observe connections?

Use:

```bash
ss -ant
```

You may see:

```text
ESTAB
```

`ESTAB` means an established TCP connection.

Use:

```bash
ss -lntp
```

to see listening TCP sockets.

## 8. TCP connection termination

TCP also has a process for closing a connection.

A simplified representation is:

```text
Client ---------------- FIN -------------> Server
Client <---------------- ACK ------------- Server
Client <---------------- FIN ------------- Server
Client ---------------- ACK -------------> Server
```

This is commonly described as a four-segment connection termination process, although the exact exchange can vary.

## 9. Troubleshooting connection establishment

If the handshake cannot complete, investigate:

- Is the server reachable?
- Is the destination IP correct?
- Is the port correct?
- Is a process listening?
- Is a firewall blocking traffic?
- Is routing correct?
- Is a security group blocking traffic?
- Is a Kubernetes NetworkPolicy involved?
- Is a load balancer forwarding correctly?

## 10. Key learning

The most important Day 11 concept:

```text
SYN
 ↓
SYN-ACK
 ↓
ACK
 ↓
TCP connection established
```
