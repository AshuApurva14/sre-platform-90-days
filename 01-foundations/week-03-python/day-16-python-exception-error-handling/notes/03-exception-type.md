# Exception types in python


1. `ValueError`

```python
number = int("hello")
```

2. `ZeroDivisionError`
```python
result = 10 / 0
```

3. `FileNotFoundError`

```python
with open("missing.txt") as file:
    data = file.read()
```

4. `KeyError`
```python
server = {
    "hostname": "server01"
}
print(server["ip"])
```

5. `IndexError`

```python
servers = ["server01"]
print(servers[5])
```

6. `TypeError`

```python
cpu = "85"
print(cpu + 10)
```

Your job today isn't to memorize every Python exception.

Learn to recognize:

What failed, why it failed, and whether I should recover or stop.