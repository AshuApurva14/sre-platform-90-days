# Lab 9: Kubernetes TLS

If you have access to your Kubernetes cluster, start here:

```kubectl
kubectl get ingress -A
```

Pick an application.

Then:

```kubectl
kubectl describe ingress <INGRESS_NAME> -n <NAMESPACE>
```

Look for:

```
TLS:
  Hosts:
  Secret Name:
```

Find the Secret:

```kubectl
kubectl get secret -n <NAMESPACE>
```

Check its type:

```kubectl
kubectl get secret <TLS_SECRET> \
  -n <NAMESPACE> \
  -o jsonpath='{.type}'
```

You may get:

```
kubernetes.io/tls
```

Now inspect certificate metadata without exposing the private key:

```kubectl
kubectl get secret <TLS_SECRET> \
  -n <NAMESPACE> \
  -o jsonpath='{.data.tls\.crt}' \
  | base64 -d \
  | openssl x509 \
      -noout \
      -subject \
      -issuer \
      -dates \
      -ext subjectAltName

```