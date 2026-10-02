# Kubernetes Endpoints

## Objective

Understand which Pods receive Service traffic.

---

## Check Endpoints

```bash
kubectl get endpoints nginx -n day14-network
```

Expected Output:
```
Pod IP: 80
```

## Important Relationship

```
Service
↓
Selector
↓
Matching Pods
↓
Endpoints
↓
Traffic
```

## No Endpoints

If you see:

```
<none>
```

Investigate:


- Are Pods running?
- Are Pods Ready?
- Do Pod labels match Service selector?
- Is Service selector correct?
- Are readiness probes failing?


## Golden Rule

A Service can exist while having no usable backend Pods.
