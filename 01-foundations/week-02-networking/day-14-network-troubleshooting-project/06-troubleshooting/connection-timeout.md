# Connection Timeout

## Meaning

Connection attempt did not receive a response within the expected time.

---

## Possible Causes

- Firewall
- Routing
- NetworkPolicy
- Security group
- Network ACL
- Load balancer
- Network failure

---

## Investigation

```bash
ip route
ip route get <destination>
nc -vz <host> <port>
traceroute <host>
```

If Kubernetes:

```
kubectl get networkpolicy -A
```

Important

- Do not immediately assume the application is down.

- The traffic may not even be reaching the application.