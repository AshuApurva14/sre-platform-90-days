# Broken #3 — Closed file

Try:

```python
with open("servers.txt", "r") as file:   
     content = file.read()
     
print(file.read())
```

The second:

```python
file.read()
```

is outside the with block.

You'll encounter:

```python
ValueError: I/O operation on closed file
```

Ask yourself:
```
Why?
```

Because leaving the with block closes the file automatically.