# Proxy and Firewall

A surprising number of corporate DevOps networking problems come from:


- Proxy
- Firewall
- NO_PROXY

Check environment variables:

```bash
env | grep -i proxy
```

You may see:

```
HTTP_PROXY
HTTPS_PROXY
NO_PROXY
```

Check:

```bash
echo $HTTP_PROXY
echo $HTTPS_PROXY
echo $NO_PROXY
```

Important:

```bash
NO_PROXY
```
defines destinations that should bypass the proxy.

This matters heavily in:

- Kubernetes
- Docker
- GitHub Actions
- Linux servers
- corporate networks