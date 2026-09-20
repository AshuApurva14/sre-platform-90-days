# Lab 03 - DNS Troubleshooting

## Scenario

An application URL is not working.

Example:

```bash
https://api.example.com
```

Before investigating the application, verify DNS.

Run:

```bash
dig api.example.com
```

Ask:

```bash
Did I receive any answer?
```

Then:

```bash
dig +short httpbin.org
```

Then:

```bash
nslookup httpbin.org
```

Then:

```bash
host httpbin.org
```

<img width="1310" height="1529" alt="Image" src="https://github.com/user-attachments/assets/c6c44104-1463-496d-8e63-4ba7dee1928c" />

---

## Learn the first troubleshooting distinction

Suppose:

```bash
curl https://api.example.com
```

fails.

Don't immediately assume:

Application is down.

First test:

```bash
dig api.example.com
```

If DNS doesn't resolve:

```bash
Client
 |
 X
DNS
 |
Application
```

You haven't even reached the HTTP layer yet.

This gives you a very important troubleshooting hierarchy:

```bash
DNS
 ↓
TCP
 ↓
TLS
 ↓
HTTP
 ↓
Application
```

<img width="1216" height="546" alt="Image" src="https://github.com/user-attachments/assets/4eda2d47-f57d-4f6b-8d65-6f693d7f9ab0" />

---

## NXDOMAIN

`NXDOMAIN` indicates that the queried domain name does not exist according to the responding DNS system.

Example:

```bash
dig this-domain-definitely-does-not-exist-12345.com
```

Observe the response.

You may see:

```bash
NXDOMAIN
```
NXDOMAIN means approximately:

The queried domain name does not exist.


<img width="1442" height="1105" alt="Image" src="https://github.com/user-attachments/assets/fad68b0c-b11a-40fd-85eb-3a7e42fdaa9e" />

---

# DNS Failure vs HTTP Failure

DNS failure:

```bash
example.com
    ↓
DNS lookup fails
    ↓
No IP address
    ↓
HTTP cannot start
```

HTTP failure:

```bash
example.com
    ↓
DNS succeeds
    ↓
IP address
    ↓
Server reached
    ↓
HTTP 404/500/503/etc.
```

# DNS Troubleshooting Incident

## Problem

```bsh
Application URL is reported as unavailable.
```

## Step 1 - DNS Check

Command:

```bash
dig example.com
```

Result:

```bash
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking$ dig xample.com

; <<>> DiG 9.18.39-0ubuntu0.24.04.6-Ubuntu <<>> xample.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 57079
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;xample.com.                    IN      A

;; ANSWER SECTION:
xample.com.             3600    IN      A       23.227.38.65

;; Query time: 2184 msec
;; SERVER: 10.255.255.254#53(10.255.255.254) (UDP)
;; WHEN: Sun Sep 20 06:50:10 UTC 2026
;; MSG SIZE  rcvd: 44
```

## Step 2 - A Record

Command:

```bash
dig example.com A
```

Result:

```bash

ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking$ dig example.com A

; <<>> DiG 9.18.39-0ubuntu0.24.04.6-Ubuntu <<>> example.com A
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 12514
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;example.com.                   IN      A

;; ANSWER SECTION:
example.com.            178     IN      A       104.20.23.154
example.com.            178     IN      A       172.66.147.243

;; Query time: 34 msec
;; SERVER: 10.255.255.254#53(10.255.255.254) (UDP)
;; WHEN: Sun Sep 20 06:51:03 UTC 2026
;; MSG SIZE  rcvd: 72
```

## Step 3 - Resolver Comparison

Commands:

```bash
dig @8.8.8.8 example.com +short

dig @1.1.1.1 example.com +short
```

Result:

```bash
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking$ dig @8.8.8.8 example.com +short
172.66.147.243
104.20.23.154

ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking$ 
ashu@DESKTOP-ITELHM3:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking$ dig @1.1.1.1 example.com +short
172.66.147.243
104.20.23.154
```

## Step 4 - HTTP Check

Command:

```bash
curl -I https://example.com
```

Result:

<img width="1363" height="332" alt="Image" src="https://github.com/user-attachments/assets/669df77e-8a63-4f1e-99ef-68d67c8be91a" />

## Conclusion

DNS successfully resolved the hostname.

The next troubleshooting layer is network connectivity/TCP.

## Learning

DNS resolution must be verified before assuming the application itself is unavailable.