# Troubleshooting exercise 1 — Forgot self
Broken:

```python
class Server:    
    def __init__(hostname):        
        self.hostname = hostname
```

Run it.

Don't immediately fix it.

Read the traceback and determine:

- What exception?
- Which line?
- What argument did Python expect?
- What is missing