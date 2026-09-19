## Kubernetes Connection

A typical request path may look like:

```bash
Client
  ↓
F5 / Load Balancer
  ↓
Ingress
  ↓
Kubernetes Service
  ↓
Pod
  ↓
Spring Boot application
```

`HTTP` troubleshooting should identify which layer is failing.

Example:

```bash
404

Could indicate:

- Wrong URL
- Incorrect Ingress path
- Application context path mismatch
```

```
503

Could indicate:

- No ready pods
- Service has no endpoints
- Readiness probe failure
- Backend unavailable
```

```
502

Could indicate:

- Incorrect backend port
- Ingress cannot communicate with upstream
- Backend connection failure
```
