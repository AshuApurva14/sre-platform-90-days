## from module import function

Instead of:

```python
import calculator

calculator.add(10, 5)
```

you can write:

```python
from calculator import add

print(add(10, 5))
```

This means:

- From the calculator module, import the add function.

---

## Import multiple functions

```python
from calculator import add, subtract

print(add(10, 5))
print(subtract(10, 5))
```

You can also import everything:

```python
from calculator import *
```

But don't use this in production code.

Why?

- Because it becomes difficult to know where a function came from.

Prefer:

```python
from calculator import add
```