# ASCII diagrams are enough.

## Request Flow
```bash
My Machine
   |
   | curl https://example.com
   |
   v
HTTP Request
   |
   v
Web Server
   |
   | HTTP Response
   |
   v
My Machine
```
Now extend it to a Kubernetes architecture:

## DevOps Application Flow

```bash
Client
  |
  v
Load Balancer
  |
  v
Ingress
  |
  v
Kubernetes Service
  |
  v
Pod
  |
  v
Application
```
This connects networking fundamentals with your actual DevOps experience.