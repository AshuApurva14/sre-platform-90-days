# Failure Injection — Service With No Endpoints

## Objective

Break the Service selector and troubleshoot the resulting failure.

---

## Step 1 — Verify Working State

```bash
kubectl get pods -n day14-network
kubectl get svc nginx -n day14-network
kubectl get endpoints nginx -n day14-network
```
Expected Output:

```
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ 
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ kubectl get pods -n day14-network
NAME                     READY   STATUS    RESTARTS   AGE
nginx-64dfb586d4-4lhc7   1/1     Running   0          41s
nginx-64dfb586d4-fpfz6   1/1     Running   0          41s
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ 
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ kubectl get svc -n day14-network
NAME    TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
nginx   ClusterIP   10.108.249.234   <none>        80/TCP    38s
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ 
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ kubectl get endpoinys nginx -n day14-network
error: the server doesn't have a resource type "endpoinys"
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ 
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ kubectl get endpoints nginx -n day14-network
Warning: v1 Endpoints is deprecated in v1.33+; use discovery.k8s.io/v1 EndpointSlice
NAME    ENDPOINTS                       AGE
nginx   10.244.0.26:80,10.244.0.27:80   63s
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ 
```
## Step 2 - Break the service

```bash
kubectl patch service nginx \
  -n day14-network \
  -p '{"spec":{"selector":{"app":"wrong-app"}}}'
```

## Step 3 — Observe
```bash
kubectl get endpoints nginx -n day14-network
```
Expected:
```
<none>
```

## Step 4 — Investigate Pods
```bash
kubectl get pods \
  -n day14-network \
  --show-labels
```
You should find:

```
app=nginx
```

## Step 5 — Investigate Service

```
kubectl get svc nginx \
  -n day14-network \
  -o yaml
```

Service selector:
```
app=wrong-app
```
## Root Cause

```
Service selector does not match Pod labels.
```

## Step 6 — Fix

```bash
kubectl patch service nginx \
  -n day14-network \
  -p '{"spec":{"selector":{"app":"nginx"}}}'
```

## Step 7 — Verify

```bash
kubectl get endpoints nginx -n day14-network
```

Then:

```bash
kubectl run curl \
  --image=curlimages/curl \
  --rm -it \
  --restart=Never \
  -n day14-network \
  -- curl -v http://nginx
```

Expected:

```
HTTP/1.1 200 OK
```

Command Line Steps:

```
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ kubectl apply -f 02-lab-setup/deployment.yaml 
deployment.apps/nginx created
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ kubectl apply -f 02-lab-setup/service.yaml 
service/nginx created
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ 
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ kubectl get deploy -n day14-network
NAME    READY   UP-TO-DATE   AVAILABLE   AGE
nginx   2/2     2            2           16s
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ kubectl get svc -n day14-network
NAME    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
nginx   ClusterIP   10.102.178.39   <none>        80/TCP    20s
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ 
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ kubectl patch service nginx \
  -n day14-network \
  -p '{"spec":{"selector":{"app":"wrong-app"}}}'
service/nginx patched
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ 
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ kubectl get svc -n day14-network
NAME    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
nginx   ClusterIP   10.102.178.39   <none>        80/TCP    44s
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ 
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ kubectl get deploy -n day14-network
NAME    READY   UP-TO-DATE   AVAILABLE   AGE
nginx   2/2     2            2           56s
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ 
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ kubectl patch service nginx \
  -n day14-network \
  -p '{"spec":{"selector":{"app":"wrong-app"}}}'^C
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ ^C
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ ^C
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ ^C
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ ^C
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ ^C
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ ^C
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ ^C
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ 
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ kubectl get endpoints nginx -n day14-network
Warning: v1 Endpoints is deprecated in v1.33+; use discovery.k8s.io/v1 EndpointSlice
NAME    ENDPOINTS   AGE
nginx   <none>      82s
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ kubectl get pod -n day14-network --show-labels
NAME                     READY   STATUS    RESTARTS   AGE    LABELS
nginx-64dfb586d4-ns5v9   1/1     Running   0          2m6s   app=nginx,pod-template-hash=64dfb586d4
nginx-64dfb586d4-wcx7t   1/1     Running   0          2m6s   app=nginx,pod-template-hash=64dfb586d4
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ kubectl get svc -n day14-network -o yaml
apiVersion: v1
items:
- apiVersion: v1
  kind: Service
  metadata:
    annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"name":"nginx","namespace":"day14-network"},"spec":{"ports":[{"port":80,"targetPort":80}],"selector":{"app":"nginx"}}}
    creationTimestamp: "2026-10-02T05:42:01Z"
    name: nginx
    namespace: day14-network
    resourceVersion: "25058"
    uid: c4d58906-05aa-49c3-bc30-5b73ef55f61c
  spec:
    clusterIP: 10.102.178.39
    clusterIPs:
    - 10.102.178.39
    internalTrafficPolicy: Cluster
    ipFamilies:
    - IPv4
    ipFamilyPolicy: SingleStack
    ports:
    - port: 80
      protocol: TCP
      targetPort: 80
    selector:
      app: wrong-app
    sessionAffinity: None
    type: ClusterIP
  status:
    loadBalancer: {}
kind: List
metadata:
  resourceVersion: ""
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ kubectl patch service nginx   -n day14-network   -p '{"spec":{"selector":{"app":"nginx"}}}'
service/nginx patched
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ kubectl get svc -n day14-network -o yaml
apiVersion: v1
items:
- apiVersion: v1
  kind: Service
  metadata:
    annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"name":"nginx","namespace":"day14-network"},"spec":{"ports":[{"port":80,"targetPort":80}],"selector":{"app":"nginx"}}}
    creationTimestamp: "2026-10-02T05:42:01Z"
    name: nginx
    namespace: day14-network
    resourceVersion: "25276"
    uid: c4d58906-05aa-49c3-bc30-5b73ef55f61c
  spec:
    clusterIP: 10.102.178.39
    clusterIPs:
    - 10.102.178.39
    internalTrafficPolicy: Cluster
    ipFamilies:
    - IPv4
    ipFamilyPolicy: SingleStack
    ports:
    - port: 80
      protocol: TCP
      targetPort: 80
    selector:
      app: nginx
    sessionAffinity: None
    type: ClusterIP
  status:
    loadBalancer: {}
kind: List
metadata:
  resourceVersion: ""
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ kubectl get endpoints nginx -n day14-network
Warning: v1 Endpoints is deprecated in v1.33+; use discovery.k8s.io/v1 EndpointSlice
NAME    ENDPOINTS                       AGE
nginx   10.244.0.28:80,10.244.0.29:80   3m8s
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ 
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project$ kubectl run curl \
  --image=curlimages/curl \
  --rm -it \
  --restart=Never \
  -n day14-network \
  -- curl -v http://nginx
All commands and output from this session will be recorded in container logs, including credentials and sensitive information passed through the command prompt.
If you don't see a command prompt, try pressing enter.
* Host nginx:80 was resolved.
* IPv6: (none)
* IPv4: 10.102.178.39
*   Trying 10.102.178.39:80...
* Established connection to nginx (10.102.178.39 port 80) from 10.244.0.32 port 40046 
* using HTTP/1.x
> GET / HTTP/1.1
> Host: nginx
> User-Agent: curl/8.22.0
> Accept: */*
> 
* Request completely sent off
< HTTP/1.1 200 OK
< Server: nginx/1.31.6
< Date: Fri, 02 Oct 2026 05:45:49 GMT
< Content-Type: text/html
< Content-Length: 896
< Last-Modified: Tue, 15 Sep 2026 12:54:15 GMT
< Connection: keep-alive
< ETag: "6aa93ff7-380"
< Accept-Ranges: bytes
< 
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, nginx is successfully installed and working.
Further configuration is required for the web server, reverse proxy, 
API gateway, load balancer, content cache, or other features.</p>

<p>For online documentation and support please refer to
<a href="https://nginx.org/">nginx.org</a>.<br/>
To engage with the community please visit
<a href="https://community.nginx.org/">community.nginx.org</a>.<br/>
For enterprise grade support, professional services, additional 
security features and capabilities please refer to
<a href="https://f5.com/nginx">f5.com/nginx</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
* Connection #0 to host nginx:80 left intact
Session ended, resume using 'kubectl attach curl -c curl -n day14-network -i -t' command
pod "curl" deleted from day14-network namespace
```

## Lesson

```
Service selector + Pod labels determine Service backends.
```