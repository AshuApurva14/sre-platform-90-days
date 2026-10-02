# Failure Injection — Wrong Port

## Objective

Understand connection failure caused by an incorrect port.

---

## Test Correct Port

```bash
kubectl run debug \
  --image=curlimages/curl \
  --rm -it \
  --restart=Never \
  -n day14-network \
  -- sh
```

Inside:

```bash
nc -vz nginx 80
```

Expected output:

```
~ $ nc -vz nginx 80
nginx (10.102.178.39:80) open
```


## Explanation

Service exposes:
```
80
```

But we requested:
```
9999
```
There is no application listening on that port.

## Important Lesson

Always verify:

```
Service port
↓
targetPort
↓
Container port
```