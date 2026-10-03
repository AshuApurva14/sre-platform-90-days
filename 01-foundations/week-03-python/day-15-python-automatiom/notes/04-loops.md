# Python Loops

Loops allow us to repeat an operation.

---

## for Loop

Example:

```python
servers = [
    "server01",
    "server02",
    "server03"
]

for server in servers:
    print(server)
```

Example 1:

Loop through numbers


```
cpu = [60, 70, 80, 90]

for cpu_valUes in cpu:
    print(CPU)
```

## loop + condiitons

Example 2:

```
cpu = [60, 70, 80, 90]

for cpu_values in cpu:

    if cpu_values > 80:
        print(f" CPU is consumed at 80%")
    else:
       
```

## while Loop

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

## SRE Example

Imagine checking multiple servers

```
servers = [
    "server01",
    "server02",
    "server03"
]

for server in servers:
    print(f"Checking {server}")


```

## Key Idea

Use loops when you have to perform same tasks multiple times.

