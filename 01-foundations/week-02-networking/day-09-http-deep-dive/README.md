# Day 9 Cheat Sheet

## HTTP Methods

GET     → Retrieve
POST    → Create/process
PUT     → Replace
PATCH   → Partial update
DELETE  → Delete

## Important Headers

Content-Type
Accept
Authorization
Host
User-Agent
Cookie
Set-Cookie

## Authentication

Authentication → Who are you?

Authorization → What are you allowed to do?

## Important curl commands

curl URL

curl -i URL

curl -I URL

curl -v URL

curl -L URL

curl -X POST URL

curl -H "Header: value" URL

curl -d '{"key":"value"}' URL

## Status Codes

2xx → Success
3xx → Redirect
4xx → Client/request issue
5xx → Server/upstream issue