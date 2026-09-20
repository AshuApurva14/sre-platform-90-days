# Connect DNS to your Kubernetes environment

This is especially important for you.

Imagine:

```bash
User
 |
 | https://prepaid.company.com
 v
DNS
 |
 | IP address
 v
F5 Load Balancer
 |
 v
Kubernetes Ingress
 |
 v
Service
 |
 v
Pod
 |
 v
Spring Boot
```

If DNS is wrong:

```bash
prepaid.company.com
        X
      DNS
```

The request never reaches:

```bash
F5
Ingress
Service
Pod
Spring Boot
```

Therefore, when debugging an application URL:

```bash
dig prepaid.company.com
```

should be one of your early checks.