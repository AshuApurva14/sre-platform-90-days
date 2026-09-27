# DNS Troubleshooting

- DNS troubleshoot is one of the most common issue in devops.

- To troubleshooting and fix this issue, one should have knowledge about the diff DNS related concepts.

- `dig` can be used to check status of DNS.

---

For **Short result:**

```
dig +short example.com
```
For **Specific record:**

```bash
dig example.com A
```
```bash
dig example.com AAAA
```

For **Compare resolvers:**

```bash
dig @8.8.8.8 example.com
```

```bash
dig @1.1.1.1 example.com
```

Example:

```bash
dig httpbin.org
```

Output:

```
shu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ dig httpbin.org

; <<>> DiG 9.18.39-0ubuntu0.24.04.7-Ubuntu <<>> httpbin.org
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 7251
;; flags: qr rd ra; QUERY: 1, ANSWER: 8, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;httpbin.org.                   IN      A

;; ANSWER SECTION:
httpbin.org.            15      IN      A       18.213.21.177
httpbin.org.            15      IN      A       13.223.216.61
httpbin.org.            15      IN      A       54.175.207.120
httpbin.org.            15      IN      A       32.194.24.163
httpbin.org.            15      IN      A       98.90.133.202
httpbin.org.            15      IN      A       107.21.166.194
httpbin.org.            15      IN      A       3.217.138.231
httpbin.org.            15      IN      A       13.216.58.208

;; Query time: 31 msec
;; SERVER: 10.255.255.254#53(10.255.255.254) (UDP)
;; WHEN: Sat Sep 26 12:32:38 UTC 2026
;; MSG SIZE  rcvd: 168

```
---

## DNS Troubleshooting Scenario

Suppose:

```bash
curl https://myapp.example.com
```

returns:

```
Could not resolve host: myapp.example.com
```

Your first action:

```bash
dig myapp.example.com
```

If:

```
NXDOMAIN
```
you have a DNS problem.

Do not waste time checking:

```
Kubernetes
TLS
HTTP
Application logs
```
yet.

Fix the lower layer first.