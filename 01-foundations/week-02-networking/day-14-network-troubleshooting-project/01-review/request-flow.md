# Request Flow

## Objective

Understand what happens when a user accesses an application.

---

## Complete Request Flow
```
Client
  ↓
DNS
  ↓
IP Address
  ↓
TCP :443
  ↓
TLS
  ↓
HTTP
  ↓
Load Balancer
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

## 1. DNS

Question:

Can the hostname be converted into an IP address?

Example:
```
application.example.com
        ↓
    10.10.10.20
```
Tool:
```
dig
nslookup
```
---

## 2. TCP

Question:

Can I establish a TCP connection to the destination port?

Example:
```
10.10.10.20:443
```
Tools:
```
nc
ss
```
---

## 3. TLS

Question:

Can HTTPS establish a secure connection?

Tools:
```
openssl s_client
curl -v
```
---

## 4. HTTP

Question:

What response did the server return?

Tool:
```
curl
```
Examples:
```
200
301
400
401
403
404
500
502
503
504
```
---

## 5. Load Balancer

The Load Balancer receives traffic and forwards it to the backend.

Example:
```
Client
 ↓
F5
 ↓
Ingress
```
---

## 6. Ingress

Ingress routes HTTP/HTTPS traffic to Kubernetes Services.

Example:
```
/api
 ↓
api-service
```
---

## 7. Service

A Kubernetes Service provides a stable endpoint for Pods.
```
Service
 ↓
Selector
 ↓
Endpoints
```
---

## 8. Endpoints

Endpoints identify the Pod IPs that can receive traffic.
```
Service
 ↓
10.42.0.10:8080
10.42.0.11:8080
```
---

## 9. Pod

The Pod contains the application container.

---

## 10. Application

Finally the application processes the request.

For example:
```
Spring Boot
Nginx
Python
Node.js
```