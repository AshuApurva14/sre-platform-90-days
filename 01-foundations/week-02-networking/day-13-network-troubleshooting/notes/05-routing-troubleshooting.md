# Routing Troubleshooting

Important commands:

```bash
ip addr
```
```bash
ip route
```

```bash
ip route get 8.8.8.8
```

Output:

```ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ ip route get 8.8.8.8
8.8.8.8 via 192.168.96.1 dev eth0 src 192.168.105.235 uid 1000 
    cache 
```

The last one is particularly useful.

Example:

```bash
ip route get 8.8.8.8
```

It tells you which route/interface/gateway Linux would use.

Mental model:

```
Application
    ↓
Kernel
    ↓
Routing table
    ↓
Interface
    ↓
Gateway
    ↓
Network
```