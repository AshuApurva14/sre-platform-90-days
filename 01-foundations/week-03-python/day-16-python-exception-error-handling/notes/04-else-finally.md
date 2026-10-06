# Else and Finally

Understand:

```python
try:
    number = int("50")

except ValueError:
    print("Invalid number")

else:
    print(f"Valid number: {number}")
```

The flow is:

```python
try
 │
 ├── failure → except
 │
 └── success → else
```

This is useful when you want the successful path separated from error handling.

## Learn finally

Now:

```python
try:
    print("Performing operation")

except Exception:
    print("Operation failed")

finally:
    print("Cleanup")
```

finally runs regardless of success or failure.

Conceptually:

```python
try
 ↓
operation
 ↓
success/failure
 ↓
finally
 ↓
cleanup
```

You'll later encounter this pattern with:

```
files
database connections
network connections
temporary resources
locks
```

## Understand raise

Sometimes your program needs to deliberately reject invalid input.

Example:

```python
cpu = 150

if cpu > 100:
    raise ValueError("CPU usage cannot exceed 100")

```

This is different from Python unexpectedly encountering an error.

Here you deliberately create an exception because the input violates your program's rules.

This is extremely useful for validation.


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

