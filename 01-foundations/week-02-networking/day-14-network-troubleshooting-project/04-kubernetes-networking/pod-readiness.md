# Pod Readiness

## Running vs Ready

Running does not always mean Ready.

Example:

```
READY   STATUS

0/1     Running
```

The container is running but the application may not be ready to receive traffic.

---

## Readiness

Readiness determines whether a Pod should receive traffic.

---

## Concept

```
Pod starts
 ↓
Application initializes
 ↓
Readiness check
 ↓
Pass?
 ├── YES → Ready → traffic
 └── NO → Not Ready → no traffic
```
---

## Check

```bash
kubectl get pods -n day14-network
```

### Detailed:

```bash
kubectl describe pod <pod-name> -n day14-network
```
Look at:

```
Conditions
Readiness
Events
Probes
Troubleshooting
```

If Pod is Running but not Ready:


- Check readiness probe.
- Check application port.
- Check application logs.
- Check application health endpoint.
- Check environment variables.
- Check dependencies.

