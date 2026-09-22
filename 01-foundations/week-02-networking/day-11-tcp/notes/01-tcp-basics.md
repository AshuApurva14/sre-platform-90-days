# TCP Basics

## 1. What is TCP?

TCP stands for **Transmission Control Protocol**.

TCP is a transport-layer protocol that provides reliable, connection-oriented communication between two endpoints.

Example:

```text
Client                         Server
10.10.10.10                   10.10.10.20
     |                              |
     |---------- TCP -------------->|
```

Before application data is exchanged, TCP establishes a connection.

## 2. Why do we need TCP?

Applications need a reliable way to exchange data over an IP network.

TCP provides:

- Connection establishment
- Reliable delivery
- Ordered delivery
- Error detection
- Retransmission of lost data
- Flow control
- Congestion control

Think of TCP as a reliable delivery mechanism between two applications.

## 3. IP vs TCP

IP answers:

> Which host should receive the packet?

TCP answers:

> Which application/service on that host should receive the data, and how should the connection be maintained?

Example:

```text
10.10.10.20:443
```

- `10.10.10.20` = IP address
- `443` = TCP port

## 4. TCP is connection-oriented

TCP establishes a connection before normal application data is exchanged.

Simplified flow:

```text
Client
  |
  | TCP connection setup
  v
Server
  |
  | Connection established
  v
Application data
```

The connection is normally established using:

```text
SYN
SYN-ACK
ACK
```

## 5. TCP in a web request

For a traditional HTTPS connection:

```text
DNS
 ↓
IP address
 ↓
TCP connection
 ↓
TLS handshake
 ↓
HTTP request
 ↓
HTTP response
```

For HTTP/1.1 and HTTP/2, TCP is traditionally the underlying transport.

HTTP/3 uses QUIC over UDP, so avoid the rule "all HTTP uses TCP."

## 6. Important Linux commands

Check TCP listeners:

```bash
ss -lntp
```

Check TCP connections:

```bash
ss -ant
```

Test a TCP port:

```bash
nc -vz HOST PORT
```

Test an HTTP endpoint:

```bash
curl -v http://HOST:PORT
```

## 7. DevOps troubleshooting

When an application is unreachable:

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

If DNS works but TCP fails, investigate:

- Listening process
- Port
- Firewall
- Security groups
- Network ACLs
- Routing
- Kubernetes NetworkPolicy
- Load balancer
- Service configuration

## 8. Key learning

Remember:

> TCP provides reliable, connection-oriented communication between application endpoints.

Core mental model:

```text
IP = host
Port = service endpoint
TCP = reliable connection
HTTP = application protocol
```
