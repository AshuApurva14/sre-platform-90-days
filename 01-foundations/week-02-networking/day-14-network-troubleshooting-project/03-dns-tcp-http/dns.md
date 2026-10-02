# DNS Lab

## Objective

Understand how hostname resolution works.

---

## Theory

DNS converts names into IP addresses.

Example:
```text
example.com
    ↓
IP address
```
---

## External DNS Test

Run:

```bash
dig example.com
```

Then:

```bash
dig +short example.com
```
Then:

```bash
nslookup example.com
```

## Kubernetes DNS

Start a debug container:

```
kubectl run curl \
  --image=curlimages/curl \
  --rm -it \
  --restart=Never \
  -n day14-network \
  -- sh
```

Inside:

```
nslookup nginx
```

Then:
```
nslookup nginx.day14-network.svc.cluster.local
```

Observe:

- The name nginx resolves to the Kubernetes Service IP.

- Important Learning

- Kubernetes provides DNS names for Services.

Short name:

```
nginx
```

Full name:

```
nginx.day14-network.svc.cluster.local
```

Troubleshooting

If DNS fails:


- Check Pod DNS configuration.
- Check CoreDNS.
- Check Service name.
- Check namespace.
- Check DNS policy.