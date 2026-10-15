# Learn `.read()` vs `.readline()` vs `.readlines()`


`read()`

```python
with open("sample.txt", "r") as file:
    content = file.read()

print(content)
```

Reads the whole file into one string.

Conceptually:

```
"web01\nweb02\ndb01\n"
```
---

`readline()`

```python

with open("sample.txt", "r") as file:
    first_line = file.readline()

print(first_line)
```

Reads one line.

---

`readlines()`

```python
with open("sample.txt", "r") as file:
    lines = file.readlines()

print(lines)
```


You may get:
```
['web01\n', 'web02\n', 'db01\n']
```

Notice:
```
\n
```

That's the newline character.