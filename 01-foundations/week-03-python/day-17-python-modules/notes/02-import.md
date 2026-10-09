# Import a module

## What actually happened?

This:
```python
import calculator
```
means:

- Python, find `calculator.py` and load it so I can use its functions.

Then:
```
calculator.add(10, 5)
```
means:

```
calculator module
       ↓
     add()
       ↓
   10 + 5
```

Think of it like a toolbox.

```
calculator.py
┌─────────────────────┐
│ add()               │
│ subtract()          │
└─────────────────────┘
          ↑
          │ import
          │
       main.py
```

---