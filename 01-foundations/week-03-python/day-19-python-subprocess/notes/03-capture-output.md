# Capture command output

```python
import subprocess

result = subprocess.run(   
    ["df", "-h"],   
    capture_output=True,  
    text=True)
    
print(result.stdout)
```

Three things matter here.

```python
capture_output=True
```

Instead of directly displaying output, Python captures it.

```python
text=True
```

Return the output as Python strings.

```python
result.stdout

```

Contains normal command output.
So:

```python
df -h
  ↓
subprocess
  ↓
result
  ├── stdout
  ├── stderr
  └── returncode
```

This mental model is extremely important.

## Understand stdout and stderr


Linux programs commonly expose:

```
                 Command
                    │
          ┌─────────┴─────────┐
          ↓                   ↓
       stdout              stderr
          │                   │
    normal output         error output
```

For example:

```bash
ls /tmp
```

may write results to stdout.
But:

```python
ls /directory-that-does-not-exist
```
writes an error to stderr.

Python gives you both:

```python
print(result.stdout)
print(result.stderr)

```