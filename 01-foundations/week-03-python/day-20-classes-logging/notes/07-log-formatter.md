# Formatter

Let's make the logs useful.

```python
import logging

logging.basicConfig(    
    level=logging.INFO,    
    format="%(asctime)s %(levelname)s %(name)s %(message)s")

logger = logging.getLogger(__name__)
logger.info("Health checker started")
```


You may see something similar to:

```
2026-10-18 17:25:10,512 INFO __main__ Health checker started
```

Important fields:

```
%(asctime)s
     ↓
timestamp

%(levelname)s
     ↓
INFO / ERROR / etc.

%(name)s
     ↓
logger/module name

%(message)s
     ↓
your message
```

## Why %s instead of an f-string?

You might wonder why I wrote:

```python
logger.info(    "Executing command: %s",    command)
```

instead of:

```python
logger.info(    f"Executing command: {command}")
```

Both can work.

But Python logging supports deferred/interpolated arguments:

```python
logger.debug(    "Server=%s CPU=%s",    hostname,    cpu)
```

This is a good habit for logging calls.

For now:

```python
logger.info("Server: %s", hostname)
```

is the pattern I'd like you to practice