# Learn `try` and `except`

`try` block and `except` block

```python
try:
    number = int("abc")
except ValueError:
    print("Invalid number")

```

Instead of:
```
program crashes
```

you get:

```
Invalid number
```

The basic pattern is:

```python
try:
    risky_operation()

except SomeException:
    handle_problem()
```

Think:

**"Try this operation. If this specific thing fails, handle it."**

---

## Don't catch everything blindly

Bad:

```python
try:
    number = int("abc")
except:
    print("Something went wrong")
```

Better:

```python
try:
    number = int("abc")
except ValueError:
    print("Invalid number")
```
Why?

- Because different failures mean different things.

### For example:

```
ValueError
    ↓
bad value

FileNotFoundError
    ↓
file missing

PermissionError
    ↓
permission problem

KeyError
    ↓
missing dictionary key

IndexError
    ↓
invalid list index

TypeError
    ↓
wrong data type
```

This distinction becomes extremely important in production troubleshooting.