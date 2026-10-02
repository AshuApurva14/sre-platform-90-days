# Failure Injection — Pod Not Ready

## Objective

Understand why Running does not always mean traffic-ready.

---

## Observe

```bash
kubectl get pods -n day14-network
```

## Expected States

Healthy:

```
1/1 Running
```

Potential problem:

```
0/1 Running
```

