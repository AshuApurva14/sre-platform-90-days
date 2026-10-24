# `__init__`

We want every server to have a hostname.
```
class Server:    
    def __init__(self, hostname):        
        self.hostname = hostname

```

Now:
```
server1 = Server("web01")
server2 = Server("db01")

print(server1.hostname)
print(server2.hostname)
```

Output:

```
web01
db01
```

The important part:
```python
Server("web01")
```

causes Python to initialize the new object using:

```python3
__init__(...)
```

For now, think of __init__ as:

```
Configure the initial state of my new object.
```

---

## What is `self?`

This confuses almost every Python beginner.

Consider:

```
server1 = Server("web01")
server2 = Server("db01")
```

Each object needs its own hostname.

Conceptually:
```
server1
   ↓
hostname = web01
```

```
server2
   ↓
hostname = db01
```

Inside:

```
self.hostname = hostname
```

self refers to the current object.

So when creating:
```
server1 = Server("web01")

```
conceptually:

```
self
 ↓
server1
```

And:
```
server2 = Server("db01")
```

conceptually:

```
self
 ↓
server2
```

Don't overcomplicate self today.

Remember:
```
self lets a method access data belonging to that particular object.
```