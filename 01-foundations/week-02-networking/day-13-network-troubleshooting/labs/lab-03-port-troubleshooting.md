# Lab 3 — Port Troubleshooting

Start a server:

```bash
python3 -m http.server 8080
```

In another terminal:

```bash
ss -lntp | grep 8080
```

Observe:

```
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days$ ss -lntp | grep 8080
LISTEN 0      5             0.0.0.0:8080      0.0.0.0:*    users:(("python3",pid=1961,fd=3))
```

Then:

```bash
nc -vz localhost 8080
```

Observe:

```
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days$ nc -vz localhost 8080
Connection to localhost (127.0.0.1) 8080 port [tcp/http-alt] succeeded!
```

Then:

```bash
curl http://localhost:8080
```

Observe:
```
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days$ curl htttp://localhost:8080
curl: (1) Protocol "htttp" not supported or disabled in libcurl
```
Now stop the server.

Run:

```bash
nc -vz localhost 8080
```
Output:
```
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days$ nc -vz localhost 8080
nc: connect to localhost (127.0.0.1) port 8080 (tcp) failed: Connection refused
```

Observe:

```
Connection refused
Your conclusion
```

Before:


```bash
TCP port 8080 → listening
HTTP → works
```

After:

```bash
TCP port 8080 → no listener
HTTP → cannot start
```