```
Application URL failing
        |
        v
Can DNS resolve?
        |
       NO
        |
        +----> DNS troubleshooting
        |
       YES
        |
        v
Can TCP port connect?
        |
       NO
        |
        +----> Routing / firewall / LB / service
        |
       YES
        |
        v
Does TLS handshake succeed?
        |
       NO
        |
        +----> Certificate / SNI / TLS / CA
        |
       YES
        |
        v
Does HTTP request succeed?
        |
       NO
        |
        +----> HTTP / LB / Ingress / application
        |
       YES
        |
        v
Is application behavior correct?
        |
       NO
        |
        +----> Application investigation
        |
       YES
        |
        v
             SUCCESS

```