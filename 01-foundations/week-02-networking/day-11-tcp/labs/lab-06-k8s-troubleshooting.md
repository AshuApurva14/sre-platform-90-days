# Kubernetes troubleshooting example

Suppose your application is unavailable.

You run:

```bash
kubectl get pods
```
and pods are:

```bash
Running
```

But the application still doesn't work.

Check:

```bash
kubectl get svc
```

Then:

```bash
kubectl get endpoints
```

or:

```bash
kubectl get endpointslices
```

You might discover:

```bash
Service
   ↓
No endpoints
```

Then your `TCP connection` may eventually fail at the service/backend layer.

Another common problem:

```bash
Service port: 80
targetPort: 8080
Application actually listening: 8081
```

Then:

```bash
Service
  ↓
:80
  ↓
:8080
  X
Application listening on :8081
```

That's a classic DevOps troubleshooting problem.