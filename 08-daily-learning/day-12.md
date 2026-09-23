# Day 12 — Learning Log

## Date
2026-09-18

## Week - 2

## Today's One Outcome

```
                 Application unavailable
                         |
                         ▼
                       DNS?
                         |
                         ▼
                        TCP?
                         |
                         ▼
                        TLS?
                         |
                         ▼
                    Certificate?
                         |
                         ▼
                        HTTP?
                         |
                         ▼
                    Application
```

## Planned Minutes

90

## Actual Focused Minutes

80

## What I Learned

Concepts
```
☐ What is TLS?
☐ What is HTTPS?
☐ Why do we need TLS?
☐ Confidentiality vs integrity vs authentication
☐ Symmetric vs asymmetric cryptography
☐ Public vs private key
☐ What is a certificate?
☐ What is a CA?
☐ Root vs intermediate CA
☐ What is a certificate chain?
☐ What is SAN?
☐ What is SNI?
☐ What is ALPN?
☐ What happens during TLS handshake?
```

Tools
```
☐ curl -v
☐ openssl s_client
☐ openssl x509
☐ nc -vz
```
Troubleshooting
```
☐ Expired certificate
☐ Hostname mismatch
☐ Unknown CA
☐ Missing intermediate
☐ TLS version mismatch
☐ TLS handshake failure
☐ TLS termination
```
Kubernetes
```
☐ TLS Secret
☐ Ingress TLS
☐ F5 TLS termination
☐ Service/backend relationship
☐ Where TLS terminates
```

## What I Built / Practiced

I have build a local server and tested and precticed TLS, TCP concepts 

## Evidence

- Git commit: ad243aa (HEAD -> main, origin/main, origin/HEAD) Add Day 12  TLS documentation and examples for Kubernetes and DevOps
- File/demo: https://github.com/AshuApurva14/sre-platform-90-days/blob/main/01-foundations/week-02-networking/day-12-tls-https/tls-lab/https_server.py

## Problem / Confusion

N/A

## How I Solved It
N/A

## What I Still Don't Understand
N/A

## Tomorrow's One Outcome


## Distractions (minutes)

25

## Focus Score (1-5)
3

## Status
Done / Partial / Missed

Done