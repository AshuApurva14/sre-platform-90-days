# Retrieve users

```bash
curl -i https://httpbin.org/get
```

Create

```bash
curl -i -X POST \
-H "Content-Type: application/json" \
-d '{"name":"Ashutosh","role":"DevOps"}' \
https://httpbin.org/post
```

Update

```bash
curl -i -X PATCH \
-H "Content-Type: application/json" \
-d '{"role":"SRE"}' \
https://httpbin.org/patch
```

Delete

```bash
curl -i -X DELETE \
https://httpbin.org/delete
```

Document the mapping:


| Operation | HTTP Method |
|---|---|
| Retrieve | GET |
| Create | POST |
| Replace | PUT |
| Partial update | PATCH |
| Delete | DELETE |

<img width="1354" height="1671" alt="Image" src="https://github.com/user-attachments/assets/10c87e3d-4027-499b-b8a0-a06a68d559d5" />

---

## Learn the most useful curl debugging command

Now we're going to combine everything.

Run:

```bash
curl -v \
  -H "Accept: application/json" \
  -H "X-Environment: test" \
  https://httpbin.org/get
```

Study:

```bash
> GET
> Host
> User-Agent
> Accept
> X-Environment

< HTTP
< Content-Type
< Content-Length
```

You should now be able to visually separate:

```bash
CLIENT → REQUEST → SERVER

CLIENT ← RESPONSE ← SERVER
```

<img width="1256" height="1501" alt="Image" src="https://github.com/user-attachments/assets/c38ebd32-21f7-4432-8f77-9140534ad865" />