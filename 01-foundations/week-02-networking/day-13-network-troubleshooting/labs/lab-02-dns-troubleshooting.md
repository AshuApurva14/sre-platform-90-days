# Lab 2 — DNS Failure Simulation

Test a valid domain:

```bash
dig example.com
```

Output:

```
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ dig httpbin.org

; <<>> DiG 9.18.39-0ubuntu0.24.04.7-Ubuntu <<>> httpbin.org
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 63553
;; flags: qr rd ra; QUERY: 1, ANSWER: 8, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;httpbin.org.                   IN      A

;; ANSWER SECTION:
httpbin.org.            19      IN      A       98.90.133.202
httpbin.org.            19      IN      A       13.216.58.208
httpbin.org.            19      IN      A       54.175.207.120
httpbin.org.            19      IN      A       44.221.208.192
httpbin.org.            19      IN      A       44.219.150.215
httpbin.org.            19      IN      A       107.21.166.194
httpbin.org.            19      IN      A       18.213.21.177
httpbin.org.            19      IN      A       34.200.179.76

;; Query time: 36 msec
;; SERVER: 10.255.255.254#53(10.255.255.254) (UDP)
;; WHEN: Sat Sep 26 17:21:18 UTC 2026
;; MSG SIZE  rcvd: 168
```

Then deliberately test a nonexistent domain:

```bash
dig this-domain-should-not-exist-123456.example
```
Output:

```
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ dig this-domain-should-not-exist-123456.example

; <<>> DiG 9.18.39-0ubuntu0.24.04.7-Ubuntu <<>> this-domain-should-not-exist-123456.example
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 4946
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;this-domain-should-not-exist-123456.example. IN        A

;; AUTHORITY SECTION:
.                       86400   IN      SOA     a.root-servers.net. nstld.verisign-grs.com. 2026092600 1800 900 604800 86400

;; Query time: 78 msec
;; SERVER: 10.255.255.254#53(10.255.255.254) (UDP)
;; WHEN: Sat Sep 26 17:21:55 UTC 2026
;; MSG SIZE  rcvd: 147
```

Observe:

```
NXDOMAIN
```

Then:

```bash
curl https://this-domain-should-not-exist-123456.example
```

Observe the failure.

```
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ curl https://this-domain-should-not-exist-123456.example
curl: (6) Could not resolve host: this-domain-should-not-exist-123456.example
```

Document:

```bash
Application symptom
        ↓
DNS command
        ↓
DNS result
        ↓
Root cause
```
