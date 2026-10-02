# TCP Lab

## Objective

Understand TCP connectivity and ports.

---

## Test Kubernetes Service Port

Run:

```bash
kubectl run debug \
  --image=curlimages/curl \
  --rm -it \
  --restart=Never \
  -n day14-network \
  -- sh
```

Inside:

```bash
nc -vz nginx 80
```

Expected:

```
Connection succeeded
```

Test Wrong Port

```bash
nc -vz nginx 9999
```

Expected:
```
Connection failure.
```

## Connection Refused

Usually means:

Destination was reachable but nothing accepted the connection on that port.

Connection Timeout

Means:
```
No response was received within the expected time.
```
Possible causes:

```
Firewall
Routing
NetworkPolicy
Security group
Load balancer
Network failure
```

Useful Commands

```bash
ss -lntp
ss -ant
nc -vz host port
```