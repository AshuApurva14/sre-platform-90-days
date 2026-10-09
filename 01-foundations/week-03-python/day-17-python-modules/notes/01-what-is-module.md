# Python module

A python module is simply a `.py` file containing python code that can be imported and reused.

## Why modules matter to an SRE

Imagine your company has:

```
server_health.py
backup_check.py
deployment_check.py
kubernetes_check.py
aws_check.py
```

All of them need:

```python
send_alert()
```

Instead of copying the function everywhere:

```python
def send_alert(message):
```

you create:
```
notifications.py
```
and put it there.

Then:
```python
from notifications import send_alert
```
Now every script can reuse it.

This gives you:
```
Reuse
   ↓
Less duplicate code
   ↓
Easier maintenance
   ↓
Easier testing
   ↓
Better automation
```

---



