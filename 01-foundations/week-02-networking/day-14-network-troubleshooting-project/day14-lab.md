## Lab 1 — Build

```bash
kubectl apply -f 02-lab-setup/namespace.yaml

kubectl apply -f 02-lab-setup/deployment.yaml

kubectl apply -f 02-lab-setup/service.yaml
```

### Verify:

```
kubectl get all -n day14-network
```

## Lab 2 — Service → Endpoints → Pods
```
kubectl get svc -n day14-network

kubectl get endpoints -n day14-network

kubectl get endpointslice -n day14-network

kubectl get pods -n day14-network -o wide
```

### Your task:

Identify which Pod IPs appear as Service endpoints.

Write the answer in your notes.

## Lab 3 — Kubernetes DNS

```
kubectl run curl \
  --image=curlimages/curl \
  --rm -it \
  --restart=Never \
  -n day14-network \
  -- sh
```

Inside:

```
nslookup nginx

curl -v http://nginx
```

Expected:

```
HTTP/1.1 200 OK
```

## Lab 4 — TCP

Inside the debug container:
```
nc -vz nginx 80
```

Then:

```
nc -vz nginx 9999
```

Document:
```
Port 80:
Result:

Port 9999:
Result:

Why are they different?
```

Exit:

```
exit
```

## Lab 5 — HTTP

```
kubectl run curl \
  --image=curlimages/curl \
  --rm -it \
  --restart=Never \
  -n day14-network \
  -- curl -v http://nginx
```

Find:

```
HTTP status
Server header
Content
Connection information
```

## Lab 6 — TLS

From your normal machine:

curl -v https://example.com

Then:

openssl s_client \
  -connect example.com:443 \
  -servername example.com

Find:

Subject
Issuer
SAN
TLS version
Certificate verification


## Lab 7 — Break Service

```
kubectl patch service nginx \
  -n day14-network \
  -p '{"spec":{"selector":{"app":"wrong-app"}}}'
```
Now:

```
kubectl get endpoints nginx -n day14-network
```

You should see no endpoints.

Now troubleshoot without looking at the solution.

Run:

```
kubectl get pods -n day14-network --show-labels

kubectl get svc nginx -n day14-network -o yaml

kubectl get endpoints nginx -n day14-network
```

### Identify the mismatch.

Then fix:

```

kubectl patch service nginx \
  -n day14-network \
  -p '{"spec":{"selector":{"app":"nginx"}}}'
```

### Verify:

```
kubectl get endpoints nginx -n day14-network
```

### Finally:
```
kubectl run curl \
  --image=curlimages/curl \
  --rm -it \
  --restart=Never \
  -n day14-network \
  -- curl -v http://nginx
```

## Lab 8 — Delete Pod
```
kubectl get pods -n day14-network
```

### Delete one:

```
kubectl delete pod <pod-name> -n day14-network
```

Watch:

```
kubectl get pods -n day14-network -w
```

Observe the replacement.

Then:
```
kubectl get endpoints nginx -n day14-network
```
Observe whether the endpoint changes.

## Lab 9 — Production troubleshooting simulation

Now close your notes.

Pretend you receive:
```
"Users cannot access the application."
```

You must answer:

1. What is the first thing you check?
2. What command do you run?
3. What does the result tell you?
4. What do you check next?

Follow:

```
DNS
 ↓
TCP
 ↓
TLS
 ↓
HTTP
 ↓
Ingress
 ↓
Service
 ↓
Endpoints
 ↓
Pods
 ↓
Application
```

Document the entire investigation in:
