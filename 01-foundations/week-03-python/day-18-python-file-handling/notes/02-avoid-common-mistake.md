# Don't make open() + close() your normal pattern

This works:
```python
file = open("servers.txt", "r")

content = file.read()

file.close()
```

But what happens if an exception occurs before:
```python
file.close()
```

?

You may leave the resource open longer than intended.

Python gives us a better pattern.

```python
with open("servers.txt", "r") as file:
    content = file.read()

print(content)
```

This should become your default.

Think:

```python
with open(...)
     │
     ├── open resource
     ├── work with resource
     │
     └── automatically clean it up
```

This is called a `context manager.`

For Day 18, you don't need to understand how context managers are implemented internally.

Just remember:

Prefer with `open(...)` for file operations.