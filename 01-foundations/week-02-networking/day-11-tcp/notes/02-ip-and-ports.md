# IP Addresses, Ports and Sockets

## 1. IP Address

An IP address identifies a network interface/host in an IP network.

Example:

```text
10.10.10.20
```

Think of an IP address as the address of a building.

## 2. Port

A port identifies a service endpoint on a host.

Example:

```text
10.10.10.20:443
```

Here:

```text
IP   = 10.10.10.20
Port = 443
```

Think:

```text
IP   = building address
Port = apartment/service number
```

## 3. Why do we need ports?

A server can run multiple network services.

Example:

```text
10.10.10.20:22    → SSH
10.10.10.20:80    → HTTP
10.10.10.20:443   → HTTPS
10.10.10.20:8080  → Application
10.10.10.20:9090  → Prometheus
```

The IP gets traffic to the host.

The port helps direct the traffic to the appropriate service.

## 4. Common DevOps ports

| Port | Common use |
|---:|---|
| 22 | SSH |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 6443 | Kubernetes API server |
| 3000 | Common Grafana/dev application |
| 8080 | Common application port |
| 9090 | Prometheus |
| 9100 | Node Exporter |
| 5432 | PostgreSQL |
| 3306 | MySQL |
| 6379 | Redis |

Port numbers are conventions, not guarantees. An application can be configured to listen on a different port.

## 5. Privileged ports

On Linux, ports below 1024 are traditionally considered privileged ports.

Common examples:

```text
22
53
80
443
```

Modern systems have additional mechanisms and capabilities, so do not treat this as an absolute statement that only root can ever use these ports.

## 6. Socket

A socket represents an endpoint used for network communication.

A TCP endpoint can be thought of as:

```text
IP:Port
```

Example:

```text
10.10.10.20:443
```

A TCP connection involves both endpoints.

Example:

```text
Client                         Server
192.168.1.10:52143  ------->  10.10.10.20:443
```

## 7. Ephemeral ports

Clients usually use a temporary source port.

Example:

```text
Client: 192.168.1.10:52143
Server: 10.10.10.20:443
```

`52143` is an example of an ephemeral client port.

The exact range depends on the operating system and configuration.

## 8. Listening port

A server process can listen for incoming TCP connections.

Example:

```text
0.0.0.0:8080
```

Check listeners:

```bash
ss -lntp
```

Example:

```text
LISTEN 0 128 0.0.0.0:8080
```

## 9. Kubernetes connection

Consider:

```text
Client
  |
  v
Service :80
  |
  v
Pod :8080
```

Example:

```yaml
ports:
  - port: 80
    targetPort: 8080
```

The Service accepts traffic on port 80 and forwards it to the Pod's port 8080.

## 10. Key learning

Remember:

```text
IP   → Which host?
Port → Which service?
Socket → Network communication endpoint
```
