# DNS Basics

## What is DNS?

DNS stands for Domain Name System.

DNS translates human-readable domain names into IP addresses.

Example:

```bash
example.com
     ↓
93.184.216.34

```

## Why do we need DNS?

Humans prefer names:

```bash
google.com
api.example.com
myapp.company.com
```

Computers communicate using IP addresses.


DNS provides the mapping between names and addresses.

Your first mental model:

```bash
Human
  |
  | myapp.example.com
  v
 DNS
  |
  | 10.20.30.40
  v
Server
```

## DNS + HTTP

Conceptually:

```bash
curl
 |
 | https://example.com
 |
 v
DNS
 |
 | "What IP belongs to example.com?"
 |
 v
IP address
 |
 v
Server
 |
 v
HTTP
```

When a client uses a hostname such as:

```bash
https://example.com
```

DNS can resolve:

```bash
example.com
     ↓
IP address
```

The client can then establish network communication with that destination.

`DNS` and `HTTP` are different layers.

DNS answers:

```bash
"Where is this hostname?"
```

HTTP answers:

```bash
"What resource do I want?"
```

## first DNS command

Check whether dig exists:

```bash
dig -v
```

If it exists, continue.

If not, check:

```bash
which dig
```

On Ubuntu/Debian, you may need:

```bash
sudo apt update
sudo apt install dnsutils
```

On RHEL/Rocky:

```bash
sudo dnf install bind-utils
```