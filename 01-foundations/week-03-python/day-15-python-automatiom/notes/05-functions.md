# Python Functions

Functions allow us to organize reusable logic.

---

# Basic Function

```python
def greet():
    print("Hello")
```

Call it:

```
greet()
```

## Function parameter

```python
def greet(name):
    print(f"Your name:{name}")


```

Call it:

```python
greet(Ashutosh)

```

## Return Value

```python

def check_cpu(cpu):

    if cpu >= 90:
        return "CRITICAL"
    elif cpu >= 80:
        return "WARNING"
    else:
        return "OK"

```

Call it:

```python
status = check_cpu(80)
print(status)
```

## Why Functions matters in SRE

Without functions:

```
large script
large script
large script
```

With functions:

```
check_cpu()
check_memory()
check_disk()
check_service()
```

Each function has one responsibility.

## Function design principle

```python
def check_cpu(cpu):
     ____
     
```

over huge function with below functionality:

```
CPU
Memory
Disk
Network
Logs
Database


```

## Understand if __name__ == "__main__":

```python
def check_server():
    print("Checking server...")
```
```
def main():
    print("Starting server health check")

    check_server()

    print("Health check completed")


if __name__ == "__main__":
    main()
```
Understand this carefully.
```
if __name__ == "__main__":
    main()
```
means the main() function executes when this file is run directly.