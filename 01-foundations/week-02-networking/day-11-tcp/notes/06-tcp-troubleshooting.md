# TCP Troubleshooting

## 1. TCP troubleshooting mindset

When an application is unavailable, do not immediately assume the application itself is broken.

Troubleshoot layer by layer:

```text
DNS
 ↓
IP connectivity
 ↓
TCP
 ↓
TLS
 ↓
HTTP
 ↓
Application
```

## 2. First question: Does DNS work?

Example:

```bash
dig example.com
```

or:

```bash
nslookup example.com
```

If DNS fails, fix DNS before troubleshooting TCP by hostname.

## 3. Check whether a TCP port is listening

On the server:

```bash
ss -lntp
```

Example:

```text
LISTEN 0 128 0.0.0.0:8080
```

If the expected port is absent, investigate:

- Application process
- Configuration
- Port binding
- Container configuration

## 4. Test TCP connectivity

Use netcat:

```bash
nc -vz HOST PORT
```

Example:

```bash
nc -vz example.com 443
```

If successful, TCP connectivity to the destination port was established.

## 5. Connection refused

Example:

```text
nc: connect to example.com port 8080 failed: Connection refused
```

A refusal commonly indicates that the destination host actively rejected the connection, often because no process is listening on that port.

Possible causes:

- No service listening
- Wrong port
- Service stopped
- Incorrect targetPort
- Load balancer forwarding to the wrong port
- Host-level configuration

Do not treat "connection refused" as proof of exactly one cause; verify with server-side checks.

## 6. Connection timeout

Example:

```text
Connection timed out
```

This means the connection was not established within the expected time.

Investigate the entire network path:

- Routing
- Firewall
- Security group
- Network ACL
- NetworkPolicy
- Load balancer
- Host availability
- Wrong IP
- Network failure

A timeout does not automatically mean "firewall."

## 7. Ping is not a TCP test

This is a common mistake:

```bash
ping example.com
```

uses ICMP.

It does not test TCP port 443.

Therefore:

```text
ping works
```

does not prove:

```text
TCP 443 works
```

Likewise, ICMP may be blocked while TCP 443 is allowed.

## 8. Useful commands

### Check listeners

```bash
ss -lntp
```

### Check connections

```bash
ss -antp
```

### Test TCP

```bash
nc -vz HOST PORT
```

### Test HTTP

```bash
curl -v http://HOST:PORT
```

### Test HTTPS

```bash
curl -vk https://HOST
```

Use `-k` only for troubleshooting certificate validation; do not use it as a production security workaround.

## 9. Troubleshooting example

Suppose:

```text
User
 ↓
F5
 ↓
Ingress
 ↓
Service
 ↓
Pod
 ↓
Spring Boot :8080
```

The user reports:

```text
Connection timeout
```

Investigate:

### Step 1 — DNS

```bash
dig app.example.com
```

Does it resolve to the expected address?

### Step 2 — TCP from an appropriate network location

```bash
nc -vz app.example.com 443
```

If it fails, investigate the network path.

### Step 3 — Load balancer

Verify:

- Listener port
- Backend pool
- Health checks
- Backend port
- Routing

### Step 4 — Kubernetes

```bash
kubectl get ingress
kubectl get svc
kubectl get endpointslices
kubectl get pods
```

### Step 5 — Pod

Check whether the application is actually listening:

```bash
kubectl exec -it POD -- ss -lntp
```

If `ss` is unavailable in the container, use an appropriate debugging/ephemeral container or inspect the application/container configuration.

## 10. Kubernetes port troubleshooting

Suppose:

```yaml
ports:
  - port: 80
    targetPort: 8080
```

But the application listens on:

```text
8081
```

Then:

```text
Service :80
    |
    | targetPort 8080
    X
Application :8081
```

The Service configuration and application listener do not match.

## 11. TCP troubleshooting decision tree

```text
Application unreachable
        |
        v
Does hostname resolve?
        |
   +----+----+
   |         |
  NO        YES
   |         |
 DNS        TCP test
             |
        +----+----+
        |         |
       FAIL      PASS
        |         |
   investigate   TLS
   TCP/network     |
                   v
                  HTTP
```

## 12. Key learning

Use this sequence:

```text
1. DNS
2. IP
3. TCP
4. TLS
5. HTTP
6. Application
```

Do not skip layers.

If TCP itself cannot connect, debugging HTTP status codes is premature.

## 13. Interview answer

### Question

How would you troubleshoot an application that is not reachable?

### Answer structure

```text
First I verify DNS resolution and confirm that the hostname
resolves to the expected IP.

Then I test TCP connectivity to the required port using
nc or another TCP connectivity tool.

If I get connection refused, I check whether the destination
service is listening on the expected port.

If I get a timeout, I investigate the network path, firewall,
security groups, routing, load balancer, or network policies.

If TCP succeeds, I move up the stack to TLS and then HTTP.

For Kubernetes, I additionally check the Service, EndpointSlices,
Ingress, targetPort, readiness, and the application listener
inside the Pod.
```
