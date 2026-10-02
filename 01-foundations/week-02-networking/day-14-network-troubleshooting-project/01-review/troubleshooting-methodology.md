# Troubleshooting Methodology

## Golden Rule

Do not guess.

Collect evidence.

---

## Troubleshooting Process

### Step 1 — Understand the symptom

Example:
```
Users cannot access application.
```
---

### Step 2 — Define impact

Questions:

- All users or some users?
- One application or multiple?
- One environment or all environments?
- Since when?
- What HTTP status?

---

### Step 3 — Understand the architecture
```
Client
 ↓
DNS
 ↓
TCP
 ↓
TLS
 ↓
Load Balancer
 ↓
Ingress
 ↓
Service
 ↓
Pod
 ↓
Application
```
---

### Step 4 — Test each layer

DNS:
```
dig
```
TCP:
```
nc
```
TLS:
```
openssl
```
HTTP:
```
curl
```
Kubernetes:
```
kubectl
```
---

## Evidence-Based Troubleshooting

Bad approach:
```
"I think Kubernetes is broken."
```
Good approach:
```
"DNS resolves correctly and TCP 443 succeeds. TLS also succeeds, but the request returns HTTP 503. I will investigate the backend path."
```
---

## Troubleshooting Pattern
```
Symptom
 ↓
Hypothesis
 ↓
Test
 ↓
Evidence
 ↓
Root Cause
 ↓
Fix
 ↓
Verification
```