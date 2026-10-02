# DNS Failure

## Symptom

Application hostname cannot be resolved.

Example:

```
Could not resolve host
```
---

## First Test

```bash
dig <hostname>
```

## Possible Causes:


- DNS server unavailable
- Incorrect DNS record
- Wrong hostname
- NXDOMAIN
- Network connectivity to DNS
- Kubernetes CoreDNS problem

## Evidence

Check:

```
dig <hostname>
nslookup <hostname>
```

## Kubernetes

Check CoreDNS:

```
kubectl get pods -n kube-system
```

Look for CoreDNS Pods.


Troubleshooting Flow:
```
Hostname
↓
dig
↓
DNS response?
├── NO → DNS investigation
└── YES → Continue to TCP
```

Verification

- DNS resolves correctly.