`03-dns-tcp-http/03-http.md`

```markdown
# HTTP Lab

## Objective

Understand HTTP request/response behavior.

---

## Test Application

```bash
kubectl run curl \
  --image=curlimages/curl \
  --rm -it \
  --restart=Never \
  -n day14-network \
  -- curl -i http://nginx

```

Expected:

```
HTTP/1.1 200 OK
```

Verbose Mode
```
curl -v http://nginx
```
Observe:

```
DNS resolution
Connection
HTTP request
HTTP response
Headers
Important Status Codes
```

```
200 → Success

301/302 → Redirect

400 → Bad request

401 → Authentication required

403 → Forbidden

404 → Resource not found

500 → Application error

502 → Bad gateway

503 → Service unavailable

504 → Gateway timeout
```

