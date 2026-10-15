# Broken #2 — Wrong mode

Suppose:
```
servers.txt
```

contains production server information.

You accidentally write:

```python
with open("servers.txt", "w") as file:    
    file.write("web01")
```


You just destroyed the previous contents.

Question to answer in your notes:

```
Why was "w" dangerous here?
```

