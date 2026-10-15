# Better pattern for server lists

Instead of:

```python
servers = file.readlines()
```


you can iterate directly:

```python
with open("sample.txt", "r") as file:
    for line in file:
        print(line)
```


But you'll notice extra spacing because each line usually contains \n.

Use:

```python
line.strip()
```


Example:

```python

with open("sample.txt", "r") as file:
    for line in file:
        server = line.strip()
        print(server)
```


Output:
```
web01
web02
db01
```

This pattern is very important for automation.