# Lab 01 - HTTP Methods

## Objective

Understand how different HTTP methods create different types of requests.

## Environment

Tool: `curl`

Target: `httpbin.org`

## GET

Command:

```bash
curl -i https://httpbin.org/get
```

<img width="1834" height="540" alt="Image" src="https://github.com/user-attachments/assets/55db5b56-75da-4837-8dea-76179c1ddef0" />

Observation:

The server returned information about the `GET` request.

Learning:

`GET` is normally used to retrieve information.

---

## POST

Command:

```bash
curl -i -X POST \
-H "Content-Type: application/json" \
-d '{"name":"Ashutosh","role":"DevOps"}' \
https://httpbin.org/post
```

<img width="2551" height="663" alt="Image" src="https://github.com/user-attachments/assets/30a47237-fd68-47f2-988d-9f4c7e57726f" />

Observation:

The server received the JSON request body.

Learning:

`POST` is commonly used to `submit data` or `create/process` a resource.

## PUT

command:

```bash
curl -i -X PUT \
  -H "Content-Type: application/json" \
  -d '{"name":"Ashutosh","role":"Senior DevOps"}' \
  https://httpbin.org/put
```

<img width="1540" height="843" alt="Image" src="https://github.com/user-attachments/assets/b1c1c800-3b18-4a84-a41f-bc1e939c786b" />

Understand:

```bash
PUT
 ↓
Replace/update resource representation

```

## PUT vs POST

`POST` commonly means:
```bash
"Process this data/create something."
```

`PUT` commonly means:

```bash
"Set/replace this resource at this location."
```
---

## PATCH

command:

```bash

curl -i -X PATCH \
  -H "Content-Type: application/json" \
  -d '{"role":"SRE"}' \
  https://httpbin.org/patch

```
Think:

```bash
PUT

User:
{
  name: Ashutosh
  role: DevOps
  team: Platform
}

PUT might replace the representation.

PATCH

{
  role: SRE
}

PATCH modifies part of it.

```

DELETE
curl -i -X DELETE \
  https://httpbin.org/delete

Document:

## DELETE

DELETE requests are used to request deletion of a resource.

Example:

DELETE /users/1

