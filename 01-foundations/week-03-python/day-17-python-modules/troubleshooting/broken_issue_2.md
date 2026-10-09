# Broken #2

Suppose:
```

from health import check_cpu
```
but health.py contains:

```
def check_memory(memory):
    ...
```
You'll get:

```
ImportError
```
Think:

Python found the module, but the thing I'm trying to import isn't available.

That's an important distinction.

```
ModuleNotFoundError
        ↓
Can't find module

ImportError
        ↓
Found module
```

but can't import requested thing