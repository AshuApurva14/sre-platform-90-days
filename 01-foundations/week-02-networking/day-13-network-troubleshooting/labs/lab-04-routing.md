# Lab 4 — Routing

Run:

```bash
ip route
```

Then:

```
ip route get 8.8.8.8
```

Then:

```bash
ip route get 1.1.1.1
```

Compare the output.

```
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days$ ip route get 1.1.1.1
1.1.1.1 via 192.168.96.1 dev eth0 src 192.168.105.235 uid 1000 
    cache 
```

Document:

```
Destination - 8.8.8.8
Gateway - 192.168.96.1
Interface - eth0
Source IP - 192.168.105.235
```
