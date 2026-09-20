# DNS Resolution

A DNS resolver receives a DNS query from a client and obtains an answer.

Example:

```bash
Client
  |
  | example.com
  v
DNS Resolver
  |
  | IP address
  v
Client
```

## DNS Hierarchy

DNS is hierarchical.

Understand the conceptual chain:

```bash
Client
   |
   v
Recursive DNS Resolver
   |
   v
Root DNS
   |
   v
TLD DNS (.com)
   |
   v
Authoritative DNS
   |
   v
IP address
```

For:

```bash
www.example.com
```

```bash
.
|
+-- com
     |
     +-- example.com
             |
             +-- www
```

the DNS hierarchy conceptually involves:

```bash
Root
 ↓
TLD
 ↓
Domain
 ↓
Subdomain/hostname
```

## Important DNS Terms

`Root:`

```bash
.
```
Top of the DNS hierarchy.


`TLD:`

TLD means Top-Level Domain such as `.com` or `.in.`

Examples:

```bash
.com
.org
.net
.in
```


`Authoritative DNS:`

The DNS system responsible for authoritative answers for a DNS zone.

`Recursive Resolver:`

A DNS server that obtains answers on behalf of clients.

## Useful dig option

```bash
dig +short example.com
```

Returns a simplified answer.

Useful when troubleshooting quickly.

Now make DNS output easier to understand.


Run:

```bash
dig +short example.com
```

You'll get a much simpler output.

For A record:

```bash
dig +short example.com A
```

For AAAA:

```bash
dig +short example.com AAAA
```

<img width="1355" height="611" alt="Image" src="https://github.com/user-attachments/assets/28dd644f-ad83-47f7-a27b-b84a13ba8b03" />

