# Failure Injection — Pod Deletion

## Objective

Understand Kubernetes desired state and automatic Pod replacement.

---

## Step 1

```bash
kubectl get pods -n day14-network
```

## Step 2 

Delete a Pod:
```
kubectl delete pod <pod-name> -n day14-network
```

## Step 3

Watch Pods

```
kubectl get pods -n day14-network -w
```

## Important Concept

- Kubernetes is declarative.

- You specify desired state.

- Controllers continuously work toward that state.

