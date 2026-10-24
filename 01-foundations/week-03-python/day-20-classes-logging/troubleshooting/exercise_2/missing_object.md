# Troubleshooting exercise 2 — Missing object attribute


```python
class Server:    
    def __init__(self, hostname):       
     hostname = hostname    def show(self):        print(self.hostname)
```


Then:

```python
server = Server("web01")server.show()
```

Why doesn't:

```
hostname = hostname
```

create:

```
self.hostname
```

?

Understand the difference between:
```
local variable
```
and:

```
object attribute
```