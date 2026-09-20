# Lab 01 - Basic DNS Lookup

## Objective

Use dig to resolve a domain name.

## Command

```bash
dig example.com
```

## Important Sections

QUESTION SECTION

```bash
Shows what DNS question was asked.
```

ANSWER SECTION

```bash
Shows the DNS answer.
```

## Learning

DNS can resolve a domain name to an IP address.

Example:

```bash
example.com
    ↓
IP address
```
<img width="1214" height="434" alt="Image" src="https://github.com/user-attachments/assets/9e29f48a-5464-4c69-af18-62df59cf3350" />

---

# A Record

An `A` record maps a hostname to an IPv4 address.

Example:

```bash
example.com → 93.184.216.34
```
A = IPv4 address

<img width="1284" height="487" alt="Image" src="https://github.com/user-attachments/assets/4ccfe95f-965d-4645-b5b1-27fc021edddd" />

---

# AAAA Record

`AAAA` records map a hostname to an IPv6 address.

```bash
A  → IPv4
AAAA → IPv6
```

<img width="1387" height="513" alt="Image" src="https://github.com/user-attachments/assets/488be7a2-f2c7-4b8f-ac79-3abfbbd15e31" />

---

# CNAME

`CNAME` means Canonical Name.

- It creates an alias from one hostname to another hostname.

- You may or may not get a CNAME depending on the domain.

- Instead of relying on one domain, use a domain you know has a CNAME when available.

The concept:

```bash
www.example.com
        |
        | CNAME
        v
example.com
        |
        | A
        v
IP address
```

A `CNAME` is essentially an alias from one DNS name to another DNS name.

Example:

```bash
www.example.com
       ↓
example.com
       ↓
IP address
```

<img width="1219" height="488" alt="Image" src="https://github.com/user-attachments/assets/1e109f92-2143-4f47-ad91-cfe2002d702a" />

---

## Why CNAME matters in DevOps

Imagine your application:

```bash
api.company.com
```

points to a load balancer.

Instead of hardcoding the load balancer's IP everywhere:

```bash
api.company.com
       ↓
Load Balancer hostname
       ↓
IP address
```

DNS gives you a level of abstraction.

This is particularly useful when infrastructure changes.

---

# MX Record

It tells DNS which servers handle email for a domain.

`MX` records identify mail servers responsible for receiving email for a domain.

MX is primarily related to email infrastructure, not web traffic.


Run:

```bash
dig example.com MX
```

MX means:

```bash
Mail Exchange.
```

<img width="1349" height="525" alt="Image" src="https://github.com/user-attachments/assets/e1b91b88-0ecd-4c0a-bedc-12f9f8b47dad" />

---

# NS Record

NS records identify the authoritative name servers for a DNS zone.

Mental model:

```bash
Domain
  |
  v
Authoritative DNS servers
  |
  v
DNS records
```

Run:

```bash
dig example.com NS
```

NS means:

```bash
Name Server.
```

These records identify authoritative DNS servers for the domain.

<img width="1225" height="543" alt="Image" src="https://github.com/user-attachments/assets/bca7dee3-ddef-400f-b8c3-f02f07b0036e" />

---

# TXT Record

TXT records contain text associated with a domain.

Common uses:

- Domain verification
- Email security
- SPF
- Other service metadata

Run:

```bash
dig example.com TXT
```

<img width="1177" height="540" alt="Image" src="https://github.com/user-attachments/assets/6dcae3cd-4789-4e6d-8b70-90559a370ea8" />

---

