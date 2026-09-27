# What is Network Troubleshooting?

Network troubleshooting means systematically identifying where communication between two systems is failing.

**Every networking troubleshooting must follow below structure:**

```bash
DNS
 ↓
Routing
 ↓
TCP
 ↓
TLS
 ↓
HTTP
 ↓
Application

```

Suppose:

```bash
curl https://prepaid.example.com
```

fails.

Don't immediately say:

```
Application is down.
```
## Follow below steps to troubleshoot it:

###  Question 1
Can DNS resolve the hostname?

```bahs
dig prepaid.example.com
```

### Question 2

Can I reach port 443?

```bash
nc -vz prepaid.example.com 443
```

## Question 3

Can TLS establish?


```bash
openssl s_client \
  -connect prepaid.example.com:443 \
  -servername prepaid.example.com
```

## Question 4

Can HTTP communicate?

```bash
curl -v https://prepaid.example.com
```

```bash

ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ dig prepaid.example.com

; <<>> DiG 9.18.39-0ubuntu0.24.04.7-Ubuntu <<>> prepaid.example.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 11964
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;prepaid.example.com.           IN      A

;; AUTHORITY SECTION:
example.com.            1800    IN      SOA     elliott.ns.cloudflare.com. dns.cloudflare.com. 2415729022 10000 2400 604800 1800

;; Query time: 403 msec
;; SERVER: 10.255.255.254#53(10.255.255.254) (UDP)
;; WHEN: Thu Sep 24 16:44:33 UTC 2026
;; MSG SIZE  rcvd: 110

ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ nc -vz prepaid.example.com 443
nc: getaddrinfo for host "prepaid.example.com" port 443: No address associated with hostname
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ 
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ openssl s_client -connect prepaid.example.com:443 -servername prepaid.example.com
4057F2785E790000:error:10080002:BIO routines:BIO_lookup_ex:system lib:../crypto/bio/bio_addr.c:738:No address associated with hostname
connect:errno=2
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ 

```

## Question 5

What does the HTTP response say?

```

200
401
403
404
502
503
504
```
Then investigate the corresponding layer.