# learn `subprocess.run()`

- `subprocess.run()` starts another program as a child process and waits for it to finish. 
- It returns a CompletedProcess object with information about the result, such as the exit code.
- If you use capture_output=True, the object also contains the program’s output in .stdout and .stderr.


for example:

```python
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "-c", "print('hello')"],
    capture_output=True,
    text=True,
    check=True,
)
print(result.stdout)



```

In the earlier example, it runs a second Python process, captures the word hello, then 
```python
print(result.stdout) 
```

displays it.


## Why is the command a list?

This:

```python
subprocess.run(["df", "-h"])
```

represents:

```python
df -h
```

Break it down:

```python
["df", "-h"]
   │     │
   │     └── argument
   │
   └── executable
```

Another example:

```python
subprocess.run(["ls", "-l", "/tmp"])
```

represents:

```python
ls -l /tmp
```

For your learning, prefer the list form.