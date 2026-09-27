# Kubernetes Connection

This is where Day 13 becomes highly relevant to your actual DevOps work.

Your architecture can look like:

```
                    Internet
                       |
                       v
                    DNS
                       |
                       v
                     F5
                       |
                       v
                   Ingress
                       |
                       v
                    Service
                       |
             +---------+---------+
             |                   |
             v                   v
           Pod A               Pod B
             |                   |
             +---------+---------+
                       |
                       v
                 Spring Boot

```

**When something fails, don't jump directly to the Pod.**

## Kubernetes Network Troubleshooting Commands

Start with:

```bash
kubectl get pods -n <namespace>
```

Then:

```bash
kubectl get svc -n <namespace>
```

Then:

```bash
kubectl get endpoints -n <namespace>
```

or preferably:

```bash
kubectl get endpointslices -n <namespace>
```

Then:

```bash
kubectl get ingress -n <namespace>
```

Then:

```bash
kubectl describe ingress <name> -n <namespace>
```

## Critical Kubernetes Relationship

Remember:

```
Ingress
   ↓
Service
   ↓
Endpoints
   ↓
Pod
```

Suppose:

```bash
kubectl get svc
```

shows a Service.

But:

```bash
kubectl get endpoints
```

shows:

```
<none>
```

Then:

```bash
Service exists
       ↓
but has no backend endpoints
```

Potential reasons:

- Pod not Ready
- selector mismatch
- pod labels incorrect
- readiness probe failing
- pod not running

This is a very common Kubernetes troubleshooting scenario