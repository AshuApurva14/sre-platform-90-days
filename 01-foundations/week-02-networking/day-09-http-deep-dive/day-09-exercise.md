# Day 9 exercise

Imagine you receive this request:

```bash
POST /api/orders HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer <token>
Accept: application/json

{
  "product": "laptop",
  "quantity": 1
}
```

You should be able to explain:

```bash
POST
 ↓
We're sending/creating something

/api/orders
 ↓
Target resource

Host
 ↓
Target hostname

Content-Type
 ↓
Request body is JSON

Authorization
 ↓
Credentials/access token

Accept
 ↓
Client wants JSON response

Body
 ↓
Order information
```

Then imagine:

```bash
HTTP/1.1 503 Service Unavailable
```

Your next question should be:
```bash
Why is the service unavailable?
```

In your Kubernetes environment, you'd investigate:

```bash
kubectl get pods
kubectl get svc
kubectl get endpoints
kubectl describe pod <pod>
kubectl describe svc <service>
kubectl logs <pod>
```

That is the transition we're building toward:

```bash
Day 8
HTTP basics
   ↓
Day 9
HTTP/API understanding
   ↓
Day 10
DNS
   ↓
Day 11
TCP
   ↓
Day 12
TLS
   ↓
Day 13
Network troubleshooting
   ↓
Day 14
Complete application troubleshooting
```