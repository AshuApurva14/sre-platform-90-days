# HTTP 5xx Troubleshooting

## 502

Bad Gateway.

Usually investigate communication between proxy/load balancer and backend.

---

## 503

`Service unavailable.`

Investigate:

- No healthy backend
- Service unavailable
- Pod readiness
- Ingress
- Backend availability

---

## 504

`Gateway timeout.`

Investigate:

- Slow backend
- Network problem
- Backend timeout
- Load balancer timeout
- Application dependency

---

## Commands

```bash
curl -v <url>

kubectl get ingress
kubectl get svc
kubectl get endpoints
kubectl get pods
kubectl logs <pod>
```

## Important

- The exact root cause depends on where the status code was generated.