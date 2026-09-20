# The mental model for Day 10

Don't memorize DNS as a collection of record types.


Remember this:

```bash
             USER
               |
               | api.company.com
               v
              DNS
               |
       +-------+-------+
       |               |
    Resolver      DNS Records
       |               |
       +-------+-------+
               |
               v
          IP Address
               |
               v
        Load Balancer
               |
               v
            Ingress
               |
               v
           Kubernetes
               |
               v
              Pod
               |
               v
          Application

```

And your troubleshooting layers are becoming:

```bash
                Application problem
                       |
                       v
                    HTTP
                       |
                       v
                     TLS
                       |
                       v
                     TCP
                       |
                       v
                     DNS
```
