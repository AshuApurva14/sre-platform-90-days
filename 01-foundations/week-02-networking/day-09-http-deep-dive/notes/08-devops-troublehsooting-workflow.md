# DevOps troubleshooting flow

This is where Day 9 becomes valuable for your actual job.

Document:

```bash
Application/API problem
        |
        v
curl -v URL
        |
        v
Can connection be established?
        |
   +----+----+
   |         |
  NO        YES
   |         |
DNS/TCP/    HTTP
network     response
            |
            v
        Status code
            |
     +------+------+
     |             |
    4xx           5xx
     |             |
Auth/path       Server/proxy
request         upstream
problem         problem
```

Then:

```bash
401
 ↓
Authentication

403
 ↓
Authorization/permission

404
 ↓
Path/routing/resource

502
 ↓
Gateway/upstream

503
 ↓
Service unavailable

504
 ↓
Timeout
```