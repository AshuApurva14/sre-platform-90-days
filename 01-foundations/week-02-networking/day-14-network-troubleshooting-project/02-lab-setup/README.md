# Kubernetes Service Architecture
The architecture is:

```
curl client
     │
     ▼
Kubernetes Service
     │
     ▼
nginx Pod
```

Your goal is to understand the traffic path before breaking it.


## Verify the Kubernetes traffic path
Time: 30 minutes

Now prove:

```
Service
   ↓
Endpoints
   ↓
Pods
```

Step 1 — Service

```bash
kubectl get svc nginx -n day14-network
```

Step 2 — Endpoints

```bash
kubectl get endpoints nginx -n day14-network
```

You should see pod IP addresses.

For example:

```
NAME    ENDPOINTS
nginx   10.42.0.10:80,10.42.0.11:80
```

Step 3 — EndpointSlices

```bash
kubectl get endpointslice -n day14-network
```

Step 4 — Pods

```bash
kubectl get pods -n day14-network -o wide
```

Now connect the information:

```
Service
ClusterIP
   ↓
Endpoint IP
   ↓
Pod IP
```

This is one of today's most important exercises.


```ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project/02-lab-setup$ kubectl create -f  deployment.yaml 
deployment.apps/nginx created


ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project/02-lab-setup$ kubectl get deploy -n day14-network
NAME    READY   UP-TO-DATE   AVAILABLE   AGE
nginx   2/2     2            2           12s



ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project/02-lab-setup$ kubectl create -f service.yaml 
service/nginx created



ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project/02-lab-setup$ kubectl svc -n day14-network
error: unknown command "svc" for "kubectl"

Did you mean this?
        set


ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project/02-lab-setup$ kubectl get svc -n day14-network
NAME    TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
nginx   ClusterIP   10.108.135.102   <none>        80/TCP    14s


ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project/02-lab-setup$ kubectl get pods -n day14-network
NAME                     READY   STATUS    RESTARTS   AGE
nginx-64dfb586d4-54jc8   1/1     Running   0          49s
nginx-64dfb586d4-wcm4b   1/1     Running   0          49s


ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project/02-lab-setup$ kubectl get endpoints nginx -n day14-network
Warning: v1 Endpoints is deprecated in v1.33+; use discovery.k8s.io/v1 EndpointSlice
NAME    ENDPOINTS                           AGE
nginx   10.244.0.12:8080,10.244.0.13:8080   53s


ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project/02-lab-setup$ kubectl apply -f service.yaml 
Warning: resource services/nginx is missing the kubectl.kubernetes.io/last-applied-configuration annotation which is required by kubectl apply. kubectl apply should only be used on resources created declaratively by either kubectl create --save-config or kubectl apply. The missing annotation will be patched automatically.
service/nginx configured


ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project/02-lab-setup$ kubectl get endpoints nginx -n day14-network
Warning: v1 Endpoints is deprecated in v1.33+; use discovery.k8s.io/v1 EndpointSlice
NAME    ENDPOINTS                       AGE
nginx   10.244.0.12:80,10.244.0.13:80   118s


 
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-14-network-troubleshooting-project/02-lab-setup$ kubectl get endpointslice -n day14-network
NAME          ADDRESSTYPE   PORTS   ENDPOINTS                 AGE
nginx-kgrv6   IPv4          80      10.244.0.13,10.244.0.12   2m11s





```