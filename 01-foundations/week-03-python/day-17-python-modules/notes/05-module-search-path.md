## if __name__ == "__main__"

You already encountered this on Day 15.

Now you'll understand why it matters.

Consider:
```python
# health.py

def check_cpu(cpu):
    if cpu >= 90:
        return "CRITICAL"
    elif cpu >= 80:
        return "WARNING"
    return "OK"


print(check_cpu(95))
```

Now:

```python
import health
```

What happens?

- The function is defined.

But also:
```
CRITICAL
```
gets printed.

- That's because Python executes top-level code when importing a module.

---

## The solution

Change it to:

```python
def check_cpu(cpu):
    if cpu >= 90:
        return "CRITICAL"
    elif cpu >= 80:
        return "WARNING"
    return "OK"


if __name__ == "__main__":
    print(check_cpu(95))
```

Now there are two possible situations.

Running directly
```
python health.py
```

Python sees:

```python
__name__ == "__main__"
```

So:

```python
print(check_cpu(95))
```
runs.

Output:
```
CRITICAL
```
Importing
```
import health
```

Now:
```python
__name__
```

is:

```
health
```

Therefore:

```python
if __name__ == "__main__":
```

is false.

The test code doesn't execute.

This is extremely important for reusable automation code.