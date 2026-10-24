# methods

A method is essentially a function associated with a class/object.

```python
class Server:    
    def __init__(self, hostname, cpu):        
        self.hostname = hostname        
        self.cpu = cpu    

    def check_cpu(self):        
        if self.cpu >= 90:            
            return "CRITICAL"   

        if self.cpu >= 80:            
            return "WARNING"  

        return "OK"
```

Then:

```python
server = Server("web01", 85)
status = server.check_cpu()
print(status)
```

Output:
```
WARNING
```

Notice:

```
server.check_cpu()
```

can access:

```
self.cpu
```

You don't need:

```
check_cpu(server["cpu"])
```

anymore.