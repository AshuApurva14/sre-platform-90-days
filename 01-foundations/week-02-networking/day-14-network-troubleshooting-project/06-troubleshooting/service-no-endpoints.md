# Kubernetes Service Has No Endpoints

## Symptom

```bash
kubectl get endpoints nginx
```

### shows:
```
<none>
```

### Investigation

### 1. Check Pods
```bash
kubectl get pods --show-labels
```

### 2. Check Service
```bash
kubectl get svc nginx -o yaml
```

### 3. Compare

Pod:

```bash
app=nginx
```

Service:

```
selector:
app=wrong-app
```

### Root Cause

- Selector does not match Pod labels.


### Fix

- Correct Service selector.

### Verification
```bash
kubectl get endpoints nginx
```

Endpoints should appear.

Then:

```bash
curl http://nginx
```

should succeed.

### Other Possible Causes

- Pods not Running
- Pods not Ready
- Readiness probe failure
- Wrong namespace
- Wrong selector
- EndpointSlice issue