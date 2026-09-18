# HTTP Status Codes

HTTP status codes describe the result of an HTTP request.

## Status Code Families

| Range | Meaning |
|---|---|
| 1xx | Informational |
| 2xx | Success |
| 3xx | Redirection |
| 4xx | Client/request error |
| 5xx | Server/upstream error |

## Then only document important codes.

### 200 OK

Request completed successfully.

Example:

GET /users

Response:

200 OK

### 201 Created

A resource was successfully created.

Usually seen with POST requests.

### 400 Bad Request

The server cannot properly process the request.

Possible reasons:

- Invalid JSON
- Missing required data
- Incorrect request syntax

## Create a DevOps-focused status code table

This is worth memorizing.

Add:

### Important DevOps Status Codes

| Code | Meaning | What I Would Check |
|---|---|---|
| 401 | Unauthorized | Credentials/token |
| 403 | Forbidden | Permission/RBAC |
| 404 | Not Found | URL/path/Ingress route |
| 500 | Internal Server Error | Application logs |
| 502 | Bad Gateway | Proxy → backend connection |
| 503 | Service Unavailable | Pods/endpoints/readiness |
| 504 | Gateway Timeout | Slow/unreachable backend |

This is far better for interviews than memorizing definitions.

## Kubernetes examples

Since you work with Kubernetes, write this:

### 503 Example in Kubernetes
---
```bash
User
↓
Ingress
↓
Service
↓
No healthy Pod
```
Possible result:
```bash
503 Service Unavailable
```
Things I would check:
```bash
kubectl get pods
kubectl get svc
kubectl get endpoints
kubectl describe ingress
kubectl logs
```

## For 502:

### 502 Example
```bash

Ingress
↓
Backend service
↓
Application unavailable or incorrect port
```
Possible checks:
```bash
- Service targetPort
- Pod containerPort
- Application listening port
- Readiness status
- Ingress backend configuration
```
Now the HTTP lesson becomes directly useful to your work.