# Kubernetes Cheat Sheet

```bash
kubectl get pods -A
kubectl describe pod <pod>
kubectl logs <pod>
kubectl get events --sort-by=.lastTimestamp
kubectl rollout status deploy/<name>
kubectl rollout undo deploy/<name>
```
