# Day 14 Golden Notes

## Application Request Flow

```
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
Load Balancer
 ↓
Ingress
 ↓
Service
 ↓
Endpoints
 ↓
Pod
 ↓
Application
```

---

## Troubleshooting Order

1. DNS
2. Routing
3. TCP
4. TLS
5. HTTP
6. Load Balancer
7. Ingress
8. Service
9. Endpoints
10. Pod
11. Application

---

## Key Commands

### DNS

```bash
dig <host>
dig +short <host>
nslookup <host>
```

### Routing
```
ip route
ip route get <destination>
```

### TCP

```
ss -lntp
ss -ant
nc -vz <host> <port>
HTTP
curl -i <url>
curl -v <url>
```

### TLS

```bash
openssl s_client \
  -connect <host>:443 \
  -servername <host>
```

### Kubernetes

```bash
kubectl get pods
kubectl get svc
kubectl get endpoints
kubectl get endpointslice
kubectl get ingress
kubectl describe
kubectl get events
kubectl logs
```

## Important Failure Meanings

### DNS failure

- Hostname cannot resolve.

### Connection refused

- Destination reached but port isn't accepting.

### Connection timeout

- No response received.

### TLS failure

Secure connection could not be established.

### 502

Gateway/proxy couldn't successfully communicate with backend.

### 503

Backend/service unavailable.

### 504

Gateway/proxy timed out waiting for backend.

### Kubernetes

```
Service
↓
Selector
↓
Matching Pods
↓
Endpoints
```

### Important:
```
Running != Ready
```
A Service can exist without usable endpoints.

### Troubleshooting Principle

- Do not guess.

- Collect evidence.

### Symptom

```
→ Hypothesis
→ Test
→ Evidence
→ Root Cause
→ Fix
→ Verification
```

