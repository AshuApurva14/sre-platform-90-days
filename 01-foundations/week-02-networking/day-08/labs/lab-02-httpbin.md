# Lab 02 - **GET** and **POST** Requests

## Test 1 - **GET**

Command:
```bash

curl https://httpbin.org/get
```
### Observation

The server returned information about my GET request.

### Learning

**GET** is used to retrieve information from a resource.

---
Now:

```bash
curl "https://httpbin.org/get?environment=test&service=payment"
```

## Test 2 - Query Parameters

Request:

```bash

/get?environment=test&service=payment

Query parameters:

environment=test
service=payment
```
### Learning

`Query parameters` appear after `?` in the `URL.`

Multiple parameters are normally separated using `&`.


## POST Request

Command:

curl -X POST \
-H "Content-Type: application/json" \
-d '{"service":"payment","environment":"test"}' \
https://httpbin.org/post

<img width="1373" height="640" alt="Image" src="https://github.com/user-attachments/assets/c7f00e9e-25e5-479a-85ef-a021b9dd16ea" />


### Command Breakdown

```bash
-X POST
```

Use POST as the HTTP method.

```bash
-H
```

Adds an HTTP header.

```bash
-H "Content-Type: application/json"
```

Tells the server that the body contains JSON.

```bash
-d
```
Sends request data.

### Request Body

```bash
{
  "service": "payment",
  "environment": "test"
}
```
