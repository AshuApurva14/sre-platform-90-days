# Production Incident Report

## Incident Title

Application Unavailable

---

## 1. Summary

Describe the incident in 2–3 sentences.

---

## 2. Impact

Who was affected?

What functionality was unavailable?

How long did it last?

---

## 3. Architecture

```
Client
 ↓
DNS
 ↓
F5 / Load Balancer
 ↓
Ingress
 ↓
Service
 ↓
Endpoints
 ↓
Pod
 ↓
Application
```
---

## 4. Symptom

Example:

Users received HTTP 503.

---

## 5. Investigation

### DNS

Command:

```bash
dig <hostname>
```

Result:

### TCP

Command:
```bash
nc -vz <hostname> 443
```

Result:

### TLS

Command:

```bash
openssl s_client ...
```

Result:

### HTTP

Command:

```bash
curl -vk ...
```

Result:

### Kubernetes

Commands:

```bash
kubectl get ingress
kubectl get svc
kubectl get endpoints
kubectl get pods
```

Results:

### Application

Command:
```bash
kubectl logs <pod>
```

Result:

### 6. Evidence

- List the evidence that proves the root cause.


### 7. Root Cause

State the actual root cause.

### 8. Fix

Describe the remediation.

### 9. Verification

How did you prove the application recovered?

### 10. Prevention

Possible prevention:

```
Monitoring
Alerting
Better readiness probes
Configuration validation
Automated testing
Deployment checks
Documentation
```

### 11. Lessons Learned

What did I learn from this incident?