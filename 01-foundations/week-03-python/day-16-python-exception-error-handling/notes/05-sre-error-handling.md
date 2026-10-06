# This is the most important part of Day 16.

Yesterday you had something like:

```python
cpu = 85
memory = 75
disk = 91
```
But what if someone gives:
```
cpu = "eighty"
```
Your health checker shouldn't blindly crash.

You want:
```
Input
 ↓
Validate
 ↓
Valid? ── No → useful error
 ↓ Yes
Check resource
 ↓
Health result
```

## Handle TypeError 


```python
server = {
    "hostname": "server01",
    "cpu": "eighty",
    "memory": 75,
    "disk": 92
}

cpu = server["cpu"]

if cpu >= 90:
    print("CRITICAL")
elif cpu >= 80:
    print("WARNING")
else:
    print("OK")

```

Python tries:

```
"eighty" >= 90
```

That doesn't make sense.

You will get something like:

```
TypeError: '>=' not supported between instances of 'str' and 'int'
```

### Mental Model for fixing issue

Refer: [01-foundations/week-03-python/day-16-python-exception-error-handling/labs/server_checker.py]

```
"eighty"
    ↓
isinstance()
    ↓
False
    ↓
raise ValueError
```

This is deliberate validation.

---

## Handling ValueError


Example:

```python
server = {
    "hostname": "server01",
    "cpu": 150,
    "memory": 75,
    "disk": 92
}

cpu = server["cpu"]

if cpu >= 90:
    print("CRITICAL")
elif cpu >= 80:
    print("WARNING")
else:
    print("OK")


```
Python sees:
```
150
```
That's a valid integer.

So this doesn't cause a Python exception:
```
cpu = 150
```
But it is invalid business/application data.

CPU usage cannot normally be:
```
150%
```
This is an important distinction.

Python-valid ≠ application-valid
```
150
```
is valid Python.

But:
```
CPU = 150%
```
is invalid according to our application's rules.

So we need validation:
```
if cpu < 0 or cpu > 100:
    raise ValueError("CPU must be between 0 and 100")
```
Now:

```
150
 ↓
outside 0–100
 ↓
ValueError
```

This is why `raise` is important.


----

## Handling KeyError

Example:

```
server = {
    "hostname": "server01",
    "memory": 75,
    "disk": 92
}



```

Notice:

- CPU is missing

If we do:
```
cpu = server["cpu"]
```

Python raises:

```
KeyError: 'cpu'
```

Why?

Because you're effectively saying:

- "Give me the value associated with the cpu key."

But there is no such key.

Refer: [01-foundations/week-03-python/day-16-python-exception-error-handling/troubleshooting/key_error.py]

### Why not simply use .get()?

Another approach is:

```
cpu = server.get("cpu")
```

If CPU doesn't exist:
```
cpu
```

will become:

```
None
```

So:

```
server = {
    "hostname": "server01",
    "memory": 75,
    "disk": 92
}

cpu = server.get("cpu")

print(cpu)
```

Output:

```
None
```

You can then validate:

```
if cpu is None:
    print("ERROR: CPU information is missing")
```

This is often convenient for optional data.

But you need to understand the difference:

```
server["cpu"]
```

means:

```
CPU is expected to exist.
```

Whereas:

```
server.get("cpu")
```

means:

```
CPU might not exist.
```

That distinction becomes useful when working with APIs and configuration.