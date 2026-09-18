# HTTP Basics

## What is HTTP?

HTTP stands for HyperText Transfer Protocol.

It is an application-layer protocol used for communication between clients and servers.

## Simple Architecture

Client → HTTP Request → Server

Client ← HTTP Response ← Server

Example:

Browser → GET /products → Web Server

Web Server → 200 OK → Browser

## Real World DevOps Example

User
↓
Load Balancer
↓
Ingress
↓
Kubernetes Service
↓
Pod
↓
Application

HTTP is commonly used between the user and application layers.

## Important Point

HTTP follows a request-response model.

The client normally initiates the request.

The server processes the request and returns a response.


## What I Understand

HTTP allows a client like curl or a browser to communicate with a server.

The client sends a request.

The server processes it and returns a response.

## Questions

- What happens before HTTP communication starts?
- How does HTTP know which server to contact?
- What is the difference between HTTP and TCP?

---

## HTTP Request Structure

Example:

GET /users HTTP/1.1
Host: example.com
Accept: application/json

The request contains:

1. Method
2. Path
3. HTTP version
4. Headers
5. Optional body

### Method

GET

Defines what operation the client wants to perform.

### Path

/users

Defines which resource the client wants.

### HTTP Version

HTTP/1.1

Defines which HTTP protocol version is being used.

### Headers

Host: example.com

Headers provide metadata about the request.

This method is important:

```bash
Concept
↓
Example
↓
Breakdown
↓
Your understanding

```

