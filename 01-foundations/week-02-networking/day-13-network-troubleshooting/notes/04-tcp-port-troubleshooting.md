# TCP/Port Troubleshooting

There are three situations.

## Situation 1  - Connection Refused

Example:

```bash
nc -vz localhost 9999
```

Observe:

```
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ nc -vz localhost 9999
nc: connect to localhost (127.0.0.1) port 9999 (tcp) failed: Connection refused
```
Possible:
```
failed: Connection refused
```

Usually means:

```
Host reachable
    |
TCP Connection attempted
    |
Nothing listening in port
```

## Situation 2 - Connection Timeout

Example:

```bash
nc -vz 10.10.12.109 443
```
and it hangs and timeout.

Observe:

```
ashu@LAPTOP-ASHU:/mnt/d/my_workspace/sre-platform-90-days/01-foundations/week-02-networking/day-13-network-troubleshooting$ nc -vz 10.10.12.109 443
nc: connect to 10.10.12.109 port 443 (tcp) failed: Connection timed out
```

Potential causes:

```
Firewall
Security group
Network ACL
NetworkPolicy
Routing
Load balancer
Service unavailable
```

Don't immediately conclude the application is down.


## Situation 3 — No Route to Host

Example:
```
No route to host
```
Think:

```
Routing
network configuration
gateway
firewall behavior
```

Check:

```bash
ip route
```

## Very Important Comparison

Memorize:

```
Connection refused = I reached the destination, but nobody accepted the connection on that port.
```

Whereas:

```
Connection timeout = I did not get a response to the connection attempt.
```

And:

```
Could not resolve host = DNS problem.
```

And:

```
TLS handshake failure = TCP worked, but TLS negotiation failed.
```

And:

```
HTTP 503 = HTTP communication succeeded, but service is unavailable.
```

This layered thinking is far more important than memorizing commands.