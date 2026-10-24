# Classes

## Why do we need classes?

Suppose you're monitoring three servers.

You could write:

```python
server1_name = "web01"
server1_cpu = 80
server1_memory = 60

server2_name = "web02"
server2_cpu = 95
server2_memory = 75
```

This quickly becomes messy.
You learned dictionaries:

server = {    
    "hostname": "web01",    
    "cpu": 80,    
    "memory": 60
}


That's better.

But imagine a server should also know how to determine its own health:

```
Server
├── hostname
├── cpu
├── memory
├── disk
│
├── check_cpu()
├── check_memory()
└── get_status()
```

A class lets us describe this kind of object.

Think:
```
Class  = blueprint

Object = actual thing created
        from the blueprint
```

Analogy:

```
Server blueprint
       ↓
     Server
     /    \
 web01    web02
```