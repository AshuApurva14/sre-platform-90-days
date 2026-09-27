# Major Lab — End-to-End Incident

Imagine this incident:

```bash
Users report that https://prepaid.example.com is not working.
```

Your job is to troubleshoot it systematically.

Step 1 — DNS

```bash
dig prepaid.example.com
```

Question:

Does hostname resolve?

Step 2 — TCP

```bash
nc -vz prepaid.example.com 443
```

Question:

Can I reach port 443?

Step 3 — TLS

```bash
openssl s_client \
-connect prepaid.example.com:443 \
-servername prepaid.example.com
```

Observe:

```
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days$ dig prepaid.example.com


; <<>> DiG 9.18.39-0ubuntu0.24.04.7-Ubuntu <<>> prepaid.example.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 19741
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;prepaid.example.com.           IN      A

;; AUTHORITY SECTION:
example.com.            1800    IN      SOA     elliott.ns.cloudflare.com. dns.cloudflare.com. 2415949263 10000 2400 604800 1800

;; Query time: 420 msec
;; SERVER: 10.255.255.254#53(10.255.255.254) (UDP)
;; WHEN: Sun Sep 27 10:35:17 UTC 2026
;; MSG SIZE  rcvd: 110

ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days$ 
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days$ mc -vz prepaid.example.com 443
Command 'mc' not found, but can be installed with:
sudo apt install mc
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days$ nc -vz prepaid.example.com 443
nc: getaddrinfo for host "prepaid.example.com" port 443: No address associated with hostname
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days$ 
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days$ openssl s_client -connect prepaid.example.com:443 -servername prepaid.example.com
4047601F57790000:error:10080002:BIO routines:BIO_lookup_ex:system lib:../crypto/bio/bio_addr.c:738:No address associated with hostname
connect:errno=2
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days$ 
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days$ 
```

Questions:

- Does handshake succeed?

- Is certificate valid?

- Is hostname present in SAN?

- Who issued certificate?

- Is certificate expired?

Does chain verify?

Step 4 — HTTP

```bash
curl -v https://prepaid.example.com
```

Check:

```bash
HTTP status
headers
response
redirects
latency
```

Step 5 — Load Balancer

Ask:

```
Where does TLS terminate?
``
For your architecture:

```bash
Client
 ↓
F5
 ↓
Ingress
```
Determine whether:

```
Client → F5
```
uses TLS and whether:

```
F5 → Ingress
```

is HTTP or HTTPS.

Step 6 — Kubernetes

Check:

```bash
kubectl get ingress -A
```

Then:

```bash
kubectl describe ingress <name> -n <namespace>
```

Then:

```bash
kubectl get svc -n <namespace>
```

Then:

```bash
kubectl get endpointslices -n <namespace>
```

Then:

```bash
kubectl get pods -n <namespace>
```

Then:

```bash
kubectl get events -n <namespace> --sort-by=.lastTimestamp
```