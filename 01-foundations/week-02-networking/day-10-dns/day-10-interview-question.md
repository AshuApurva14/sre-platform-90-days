# Day 10 interview questions

At the end of today's session, close your notes and answer these.

Fundamentals

```bash
What is DNS?
Why do we need DNS?
What is an IP address?
What is a DNS resolver?
What is an authoritative DNS server?
What is a DNS zone?
What is TTL?
```
```bash
Records
What is an A record?
What is an AAAA record?
What is a CNAME?
What is an MX record?
What is an NS record?
What is a TXT record?
```

Troubleshooting

```bash
What does dig do?
How do you query a specific DNS server?
How do you get a simplified DNS answer?
What is NXDOMAIN?
How do you compare two DNS resolvers?
What would you check if curl cannot resolve a hostname?
How does DNS relate to Kubernetes Ingress?
```

## Scenario

Someone reports:

```bash
https://api.company.com
```

is not working.

Explain your troubleshooting sequence.

Your answer should start approximately:

First I would verify DNS resolution:

```bash
dig api.company.com
```

Then I would verify the returned IP.

If `DNS` works, I would move to `TCP` connectivity.

After that I would check `TLS` and then `HTTP`.