# Network Troubleshooting Decision Tree

```
Application unreachable
        |
        v
Does DNS resolve?
   |
   +-- NO --> DNS investigation
   |
   +-- YES
        |
        v
Can TCP connect?
   |
   +-- REFUSED --> Port/listener/service
   |
   +-- TIMEOUT --> Routing/firewall/network
   |
   +-- YES
        |
        v
Does TLS work?
   |
   +-- NO --> Certificate/SNI/CA/TLS
   |
   +-- YES
        |
        v
What HTTP status?
   |
   +-- 4xx --> Client/auth/path
   |
   +-- 502 --> Proxy/backend
   |
   +-- 503 --> Backend unavailable
   |
   +-- 504 --> Backend timeout
   |
   +-- 2xx --> Request succeeded

Kubernetes:

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