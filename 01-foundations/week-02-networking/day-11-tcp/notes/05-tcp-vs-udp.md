# TCP vs UDP

## 1. TCP

TCP stands for:

**Transmission Control Protocol**

TCP is connection-oriented and provides reliable, ordered byte-stream delivery.

Important characteristics:

- Connection-oriented
- Reliable delivery
- Ordered delivery
- Retransmission
- Flow control
- Congestion control
- More protocol overhead than UDP

## 2. UDP

UDP stands for:

**User Datagram Protocol**

UDP is connectionless and does not provide TCP-style guarantees for delivery or ordering.

Important characteristics:

- Connectionless
- No TCP-style delivery guarantee
- No TCP-style ordering guarantee
- Low protocol overhead
- Application can implement its own reliability if needed

## 3. Comparison

| Feature | TCP | UDP |
|---|---|---|
| Connection | Connection-oriented | Connectionless |
| Reliability | Built in | Not provided by UDP |
| Ordering | Yes | Not guaranteed |
| Retransmission | Yes | Not provided by UDP |
| Handshake | TCP handshake | No TCP handshake |
| Overhead | Higher | Lower |
| Typical use | HTTPS, SSH, databases | DNS, streaming/real-time protocols |
| Modern HTTP | HTTP/1.1 and HTTP/2 commonly use TCP | HTTP/3 uses QUIC over UDP |

## 4. Does UDP mean unreliable applications?

Not necessarily.

An application using UDP can implement its own reliability, sequencing, acknowledgements, or retransmission.

UDP itself simply does not provide the same guarantees that TCP provides.

## 5. DNS example

Traditional DNS queries commonly use UDP.

Example:

```text
Client
  |
  | DNS query
  v
DNS resolver
```

DNS can also use TCP in situations where TCP is required.

Therefore:

> DNS is not "UDP only."

## 6. HTTP example

Traditional web traffic:

```text
HTTP/1.1
HTTP/2
   |
   v
 TCP
```

HTTP/3:

```text
HTTP/3
   |
   v
 QUIC
   |
   v
 UDP
```

QUIC provides transport functionality above UDP.

## 7. When should you think about TCP?

Think about TCP when you need to troubleshoot:

- SSH
- HTTPS
- HTTP/1.1
- HTTP/2
- Database connections
- Kubernetes API
- Application service ports
- Load balancer backend connections

## 8. Key learning

Do not memorize:

> TCP is good, UDP is bad.

Instead:

> TCP and UDP provide different transport characteristics for different application requirements.

Core comparison:

```text
TCP → connection + reliability + ordering

UDP → lightweight datagrams without TCP's reliability guarantees
```
