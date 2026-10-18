# Exercise B — command exists but fails

Try something like:

```python
subprocess.run(   
    ["ls", "/missing-directory"],   
    check=True
    )
```

Identify why this differs from Exercise A.