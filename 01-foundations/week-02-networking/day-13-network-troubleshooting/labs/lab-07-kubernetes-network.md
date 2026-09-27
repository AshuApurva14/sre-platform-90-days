# Lab 7 — Kubernetes Network Investigation

Use a test namespace if you have access.

```bash

kubectl create namespace network-lab
```

Create deployment:

```kubectl
kubectl create deployment nginx \
  --image=nginx \
  -n network-lab
```

Check:

```kubectl
kubectl get pods -n network-lab
```

Create Service:

```kubectl
kubectl expose deployment nginx \
  --port=80 \
  --target-port=80 \
  -n network-lab
```

Check:

```kubectl
kubectl get svc -n network-lab
```

Then:

```kubectl
kubectl get endpoints -n network-lab
```

You should see the Pod IP.

Now investigate:

```kubectl
kubectl describe svc nginx -n network-lab
```

## Test Service From Inside Kubernetes

Run:

```kubectl
kubectl run curl \
  --image=curlimages/curl \
  --rm -it \
  --restart=Never \
  -n network-lab \
  -- sh
```

Inside the container:

```
curl http://nginx
```

Then:

```
nslookup nginx
```

Now you've demonstrated:

```
Pod
 ↓
Kubernetes DNS
 ↓
Service
 ↓
Endpoint
 ↓
nginx Pod
```

This is an excellent hands-on exercise.