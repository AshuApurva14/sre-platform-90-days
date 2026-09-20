# DNS Troubleshooting Tools

## dig

Detailed DNS query tool.

Example:

```bash
dig example.com
```

## nslookup

Simple DNS lookup tool.

Example:

```bash
nslookup example.com
```

## host

Simple hostname lookup.

Example:

```bash
host example.com
```

<img width="1524" height="1197" alt="Image" src="https://github.com/user-attachments/assets/8f2147cb-c9fd-431e-8a12-4a68eeca7414" />

---

## Query a Specific DNS Server

```bash
dig @8.8.8.8 example.com
```

The @ syntax tells dig which DNS server to query.

This is useful when troubleshooting DNS resolver differences.

<img width="1335" height="1032" alt="Image" src="https://github.com/user-attachments/assets/ef43ab0b-e112-48b1-8abe-2d539adf0d42" />

---

# DNS TTL

TTL controls how long DNS information can be cached.

Example:

```bash

example.com 300 IN A <IP>

```

300 means the record has a TTL of 300 seconds.

Run:

```bash

dig httpbiin.org
```

<img width="1228" height="637" alt="Image" src="https://github.com/user-attachments/assets/8c61db4d-b65a-4fcf-8406-63af495b0c61" />

---

## DevOps Connection

DNS caching means clients/resolvers may continue using an older DNS answer until its TTL expires or the cache is refreshed.

Imagine:

```bash
api.company.com
      ↓
Old Load Balancer
```

You change it:

```bash
api.company.com
      ↓
New Load Balancer
```

But some clients may still have the old DNS answer cached.

That's why DNS changes aren't necessarily visible everywhere immediately.