# Lab 4: Understand SNI

Run:

```bash
openssl s_client \
  -connect example.com:443 \
  -servername example.com
```

Now compare:

```bash
openssl s_client \
  -connect example.com:443
```

Why does `-servername` matter?


Because one IP can serve multiple websites:
```bash
             10.10.10.20
                  |
        +---------+---------+
        |                   |
 example.com          api.example.com
```

`SNI` allows the client to communicate the hostname during TLS negotiation.