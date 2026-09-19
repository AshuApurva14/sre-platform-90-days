# Idempotency and REST

## What is Idempotency?

An operation is idempotent when repeating the same request has the same intended effect on the resource as making it once.

Common HTTP methods considered idempotent:

- GET
- HEAD
- PUT
- DELETE
- OPTIONS

POST is generally not considered idempotent.

Example:

```bash
GET /users/123
GET /users/123
GET /users/123
```

You're repeatedly asking for the same resource.

But:

```bash
POST /orders
```
may create:

```bash
Order 1001
```
and repeating it may create:

```bash
Order 1002
```
This becomes very important in:

```bash
CI/CD
retries
APIs
automation
distributed systems
```

## Why idempotency matters to DevOps

Imagine your deployment pipeline runs:

```bash
Deploy application
       |
       X network timeout
```

Your pipeline doesn't know whether the deployment actually happened.

Should it retry?

If the operation is designed to be idempotent:

```bash
Retry
  ↓
Same desired state
```

This is one reason infrastructure tools such as Terraform are designed around desired state/idempotent operations.

## DevOps Connection

Retries are common in automation.

If an operation is safely repeatable, retries are easier to handle.

This is especially important for:

- CI/CD pipelines
- Infrastructure automation
- API calls
- Kubernetes automation

## REST API Fundamentals

REST is an architectural style commonly used for HTTP APIs.

A REST-style API typically represents resources using URLs.

Example:

```bash
/users
/users/123
/orders
/orders/1001
/products
/products/10
```

```bash
GET /users
      ↓
Retrieve users

POST /users
      ↓
Create user

GET /users/123
      ↓
Retrieve user 123

PATCH /users/123
      ↓
Modify user 123

DELETE /users/123
      ↓
Delete user 123
```

## Important REST principle

Don't think:

```bash
/users/getUser
/users/createUser
/users/deleteUser
```

A REST-style design often uses:

```bash
GET    /users/123
POST   /users
DELETE /users/123
```

The HTTP method expresses the operation.

The URL identifies the resource.

This isn't an absolute rule—real APIs often use action endpoints—but it's the useful baseline.