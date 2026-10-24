# Understand log levels

Python logging provides several levels.

From least severe to most severe:

```
DEBUG
  ↓
INFO
  ↓
WARNING
  ↓
ERROR
  ↓
CRITICAL
```

Think about them operationally:

| Level | Meaning | Example |
|---|---|---|
| DEBUG | Diagnostic detail | Command arguments |
| INFO | Normal event | Health check started |
| WARNING | Potential problem | CPU 85% |
| ERROR | Operation failed | Command failed |
| CRITICAL | Severe failure | Monitoring system unavailable |


Examples:

```python
logging.debug("Executing command")
logging.info("Health check started")
logging.warning("CPU usage above 80%")
logging.error("kubectl command failed")
logging.critical("Unable to monitor production cluster")
```

## Why doesn't DEBUG appear?

Try:

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.debug("Debug message")
logging.info("Info message")
```


You should see:
```
INFO...
```

but not `DEBUG.`

Why?

Because:
```
level=logging.INFO
```

means:

```
DEBUG      ❌
INFO       ✅
WARNING    ✅
ERROR      ✅
CRITICAL   ✅
```

Change:
```
level=logging.DEBUG
```

and `DEBUG` becomes visible.

This is useful because production might run at:

```
INFO
```

while troubleshooting might temporarily use:

```
DEBUG
```

## Use a named logger

Instead of repeatedly using:

```python
logging.info(...)
```

real projects commonly create a module logger:

```python
import logging
logger = logging.getLogger(__name__)
```

Then:

```python
logger.info("Application started")
logger.warning("CPU usage high")
logger.error("Command failed")
```

You'll use this pattern frequently:
```
logger = logging.getLogger(__name__)
```

`__name__` identifies the Python module generating the message.

That becomes especially useful in your modular application.