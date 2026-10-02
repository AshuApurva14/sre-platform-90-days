# Kubernetes Service

## Objective

Understand how a Service exposes Pods.

---

## Architecture

```
Client
 ↓
Service
 ↓
Pod
```
---

## Check Service

```bash
kubectl get svc nginx -n day14-network
```

### Detailed Configurations

```bash
kubectl get svc nginx -n day14-network -o yaml

```

Look for:

```yaml
app: nginx
```

And:

```yaml
port: 80
targetPort: 80
```

### Important Concepts

port:

Port exposed by Service.

targetPort:

Port on the backend Pod.

selector:

Determines which Pods belong to the Service.


### Important Relationship

Pod labels:

```
app=nginx
```

Service selector:

```
app=nginx
```

Therefore:

```
Service → Pod
```