# Connection Refused

## Meaning

The destination was reached but the requested port rejected the connection.

---

## Example

```bash
nc -vz host 9999
```

Possible Causes:

- Nothing listening
- Wrong port
- Service targetPort incorrect
- Application stopped
- Listener bound to another port
- Investigation

```bash
ss -lntp
```

For Kubernetes:

```bash
kubectl get svc
kubectl get endpoints
kubectl get pods
```

## Important Difference

Connection refused:
```
Destination reached.
```

Connection timeout:
```
No response received.
```

Verification

- Confirm correct port and listener.