# Kubernetes Service DNS

## Objective

Understand how applications discover Services.

---

## Test

```bash
kubectl run curl \
  --image=curlimages/curl \
  --rm -it \
  --restart=Never \
  -n day14-network \
  -- sh

```

Inside:

```bash

nslookup nginx
```

Then:

```bash
curl -i http://nginx
```

Full DNS Name:

```
nginx.day14-network.svc.cluster.local
```

## Flow

```
Application
↓
DNS lookup
↓
Service ClusterIP
↓
Service
↓
Endpoint
↓
Pod
```
