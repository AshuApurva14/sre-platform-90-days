# Day 11 mental model

Think about calling a restaurant.

You first need to know:

```bash
Restaurant name
      ↓
DNS
      ↓
Restaurant address
      ↓
TCP connection
      ↓
"Can I establish communication?"
      ↓
TLS
      ↓
HTTP
      ↓
Application
```

So your networking stack for this week is becoming:

```bash
User
  ↓
DNS
  ↓
IP
  ↓
TCP
  ↓
TLS
  ↓
HTTP
  ↓
Application
```

You already learned:

```bash
DNS → "Where is the server?"
HTTP → "What do I want from the server?"
```
Today:

```bash
TCP → "Can I establish a reliable connection to that server?"
```