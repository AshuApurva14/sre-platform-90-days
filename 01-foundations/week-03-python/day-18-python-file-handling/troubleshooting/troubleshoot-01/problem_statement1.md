# Broken #1 — File doesn't exist

```python
with open("production.txt", "r") as file:
    print(file.read())

```

when production.txt doesn't exist.

Expected:
```
FileNotFoundError
```
Your task: catch it without crashing.