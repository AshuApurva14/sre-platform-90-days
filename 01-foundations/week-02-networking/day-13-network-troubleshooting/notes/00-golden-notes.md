# DAY 13 — NETWORK TROUBLESHOOTING

Core flow:
```
DNS → Routing → TCP → TLS → HTTP → Application
```
DNS:
```
dig
nslookup
host
```

Routing:
```
ip addr
ip route
ip route get
```

TCP:
```
ss -lntp
ss -ant
nc -vz
```

TLS:
```
openssl s_client
openssl x509
```

HTTP:
```
curl -v
```

Packets:
```
tcpdump
```

Kubernetes:

```
Ingress
   ↓
Service
   ↓
Endpoints
   ↓
Pods
```

Common failures:

```
Could not resolve host
→ DNS

NXDOMAIN
→ DNS

No route to host
→ Routing/network

Connection refused
→ No listener/service rejecting connection

Connection timeout
→ Firewall/network/LB/routing

TLS handshake failure
→ TLS/certificate/SNI/version

401
→ Authentication

403
→ Authorization

404
→ URL/routing/resource

502
→ Proxy/LB/upstream problem

503
→ Service unavailable/no healthy backend

504
→ Upstream timeout
```

Golden troubleshooting question:

```
"Which layer is failing?"
```
Never jump directly to application logs.

First prove:

```
DNS
 ↓
TCP
 ↓
TLS
 ↓
HTTP
 ↓
Kubernetes
 ↓
Application
```