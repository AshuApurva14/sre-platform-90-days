# Important command set to memorize

For TCP troubleshooting:

```bash
ss -lntp
```

Check listeners.

```bash
ss -ant
```

Check TCP connections.

```bash
nc -vz HOST PORT
```

Test TCP connectivity.

```bash
curl -v URL
```

Test HTTP/HTTPS and see connection details.

```bash
ping HOST
```

Test `IP/ICMP reachability` — but remember that ping does NOT test TCP.

This is important.

A server can:

```bash
ping → works
TCP 443 → fails
```

or:

```bash
ping → blocked
TCP 443 → works
```

So don't conclude that **"ping works = application network works."**