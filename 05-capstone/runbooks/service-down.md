# Runbook — Service Down

## Check

```bash
kubectl get pods -n sre-capstone
kubectl get svc -n sre-capstone
kubectl get events -n sre-capstone --sort-by=.lastTimestamp
```

## Mitigation

Check the most recent deployment and roll back when a release is implicated.

## Verification

- Pods Ready
- Health endpoint works
- Error rate normal
- Latency normal
