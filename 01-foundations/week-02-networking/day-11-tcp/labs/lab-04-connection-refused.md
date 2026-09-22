# Lab 04 -  `Connection Refused`

Now Run:

```bash
curl http://localhost:8080
```
You should get something like this:

```bash
curl: (7) Failed to connect to localhost port 8080 after 0 ms: Couldn't connect to server
```
try:

```bash
nc -vz localhost 8080
```
you may get:

```bash
nc: connect to localhost (127.0.0.1) port 8080 (tcp) failed: Connection refused
```

Now ask:

```bash
why?
```

Because:

```bash
localhost:8080
        ↓
No process listening
        ↓
Connection refused
```
Check:

```bash
ss -lntp | grep 8080
```

## Connection refused vs timeout

This distinction is very important for DevOps interviews.

`Connection refused`

Usually means:

```bash
Host reachable
      ↓
Port reachable
      ↓
Nothing accepting connection
```

Example:

```bash
curl → server:8080
             ↓
       no listener
             ↓
    Connection refused
```

`Timeout`

Usually means:

```bash
Client
  ↓
Network
  ↓
???
```

The connection attempt isn't getting an appropriate response within the timeout.

Possible causes include:

- firewall
- security group
- network ACL
- routing issue
- network policy
- unreachable host
- service not reachable through the network path

Don't memorize `"timeout = firewall"` as an absolute rule. A `timeout` tells you the `connection` `wasn't established` within the expected time, and you investigate the network path.

## Very important troubleshooting table

```bash
Symptom	                       First thing to investigate

DNS resolution fails	         DNS
Connection refused	            Listener/service/port
Connection timeout	            Network path/firewall/routing/etc.
TCP connects	                Move to TLS/HTTP
HTTP 404	                    Application/path/routing
HTTP 503	                    Service/backend availability
HTTP 502	                    Proxy/upstream problem
```
Your troubleshooting flow should now be:

```bash
Application unavailable
        │
        ↓
DNS working?
        │
        ├── NO → DNS investigation
        │
        ↓ YES
TCP connection working?
        │
        ├── NO → port/network/firewall/listener
        │
        ↓ YES
TLS working?
        │
        ├── NO → TLS/certificate investigation
        │
        ↓ YES
HTTP working?
        │
        ├── NO → HTTP/application investigation
        │
        ↓
Application
```

This is the beginning of your real DevOps troubleshooting methodology.