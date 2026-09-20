# Day 10 - DNS Fundamentals

## Objective

Understand how DNS translates domain names into IP addresses and learn how to troubleshoot DNS problems using dig, nslookup, and host.

## Topics

- What is DNS?
- Domain names
- IP addresses
- DNS resolver
- DNS records
- A record
- AAAA record
- CNAME
- MX
- NS
- TXT
- DNS resolution
- Recursive DNS
- Authoritative DNS
- TTL
- DNS caching
- DNS troubleshooting

## Tools

- dig
- nslookup
- host
- curl

## Labs

1. Basic DNS lookup
2. DNS record investigation
3. DNS troubleshooting

## DevOps Connection

DNS is involved before an HTTP request can reach an application.

Typical flow:

Client
↓
DNS
↓
IP address
↓
Load Balancer / Ingress
↓
Application

# Day 10 Cheat Sheet

## DNS

DNS translates names into network addresses.

## Important Records

A       → IPv4
AAAA    → IPv6
CNAME   → Alias
MX      → Mail
NS      → Name server
TXT     → Text/verification

## Commands

dig example.com

dig example.com A

dig example.com AAAA

dig example.com NS

dig example.com MX

dig example.com TXT

dig +short example.com

dig @8.8.8.8 example.com

nslookup example.com

host example.com

## Troubleshooting

Hostname doesn't resolve
        ↓
Check DNS

DNS resolves
        ↓
Check TCP

TCP works
        ↓
Check TLS

TLS works
        ↓
Check HTTP

HTTP works
        ↓
Check application