# TLS in Kubernetes and DevOps

## Common architecture

```
Client
  |
  | HTTPS
  v
F5 / Load Balancer
  |
  v
Ingress
  |
  v
Service
  |
  v
Pod
  |
  v
Spring Boot
```
---

## Where can TLS terminate?

### Option 1 — F5

```
Client
  |
 HTTPS
  v
F5
  |
 HTTP/HTTPS
  v
Ingress
```
---

### Option 2 — Ingress

```
Client
  |
 HTTPS
  v
F5
  |
 HTTPS
  v
Ingress
  |
 HTTP
  v
Service
```
---

### Option 3 — Application
```
Client
  |
 HTTPS
  v
F5
  |
 HTTPS
  v
Ingress
  |
 HTTPS
  v
Application
```
---

## Most important question

Where does `TLS` terminate?

```
This determines where you investigate certificates.
```
---

## Kubernetes TLS Secret

Typical Secret:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-tls
type: kubernetes.io/tls
data:
  tls.crt: <certificate>
  tls.key: <private-key>
```

Never expose tls.key.

---

## Useful commands

```kubectl
kubectl get ingress -A

kubectl describe ingress <name> -n <namespace>

kubectl get secret -n <namespace>

kubectl get svc -n <namespace>

kubectl get endpointslices -n <namespace>

kubectl get pods -n <namespace>
```
---

## Inspect certificate metadata

If authorized:

```kubectl

kubectl get secret app-tls -n <namespace> \
  -o jsonpath='{.data.tls\.crt}' \
  | base64 -d \
  | openssl x509 -noout \
      -subject \
      -issuer \
      -dates \
      -ext subjectAltName
```

Only inspect the certificate.

Do not expose the private key.

---

## Production certificate lifecycle

```
Create
 ↓
Deploy
 ↓
Monitor expiry
 ↓
Renew
 ↓
Rotate
 ↓
Verify
```
---

## Key learning

- In a production incident, first determine:

- Where does TLS terminate?

- Then troubleshoot that component.