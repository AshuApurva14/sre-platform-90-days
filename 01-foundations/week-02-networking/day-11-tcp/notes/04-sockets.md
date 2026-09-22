# TCP Sockets and Connection States

## 1. What is a socket?

A socket is a software endpoint used by an application for network communication.

A simple representation is:

```text
IP:Port
```

Example:

```text
10.10.10.20:8080
```

## 2. Server socket

A server application creates a socket and listens for incoming connections.

Example:

```text
Python application
       |
       v
0.0.0.0:8080
       |
       v
     LISTEN
```

Check it with:

```bash
ss -lntp
```

## 3. Client socket

When a client connects, it normally gets an ephemeral source port.

Example:

```text
Client                         Server
10.10.10.10:52143  -------->  10.10.10.20:8080
```

The client source port is temporary.

## 4. Important TCP states

### LISTEN

A process is waiting for incoming connections.

```text
LISTEN 0 128 0.0.0.0:8080
```

### ESTABLISHED

A TCP connection has been established.

```text
ESTAB 0 0 10.10.10.10:52143 10.10.10.20:8080
```

### SYN-SENT

The client has sent a SYN and is waiting for a response.

### SYN-RECV

The server has received a SYN and is responding/awaiting completion of the handshake.

### TIME-WAIT

A TCP endpoint is waiting for a period after connection termination so delayed packets do not interfere with a future connection.

## 5. Useful commands

List listening TCP sockets:

```bash
ss -lntp
```

List all TCP connections:

```bash
ss -ant
```

Include process information:

```bash
ss -antp
```

Inspect one port:

```bash
ss -lntp | grep ':8080'
```

## 6. Find the process using a port

Example:

```bash
sudo ss -lntp | grep ':8080'
```

You may see:

```text
users:(("python3",pid=1234,fd=3))
```

This tells you which process owns the listening socket.

Depending on the Linux distribution, you can also use:

```bash
sudo lsof -iTCP:8080 -sTCP:LISTEN
```

## 7. Why sockets matter in DevOps

When an application is reported as unavailable, ask:

```text
Is the process running?
        ↓
Is it listening?
        ↓
Which address?
        ↓
Which port?
        ↓
Can a client connect?
```

For Kubernetes, the same thinking applies:

```text
Pod
 ↓
Application process
 ↓
Container port
 ↓
Service targetPort
 ↓
Service port
 ↓
Ingress/load balancer
```

## 8. Common mistake

Do not assume:

```text
Pod = application reachable
```

A Pod can be Running while:

- application process is not listening
- wrong port is configured
- readiness probe is failing
- Service has no endpoints
- NetworkPolicy blocks traffic

## 9. Key learning

Remember:

```text
LISTEN → waiting for connections
ESTAB  → connection established
```

And use:

```bash
ss -lntp
```

as one of your first Linux TCP troubleshooting commands.
