# Broken #3 — NameError

```
import health

print(check_cpu(90))
```

You imported:

```
health
```

but you're trying to directly call:
```
check_cpu()
```
You should use:

```
health.check_cpu(90)
```
Or:

```
from health import check_cpu

print(check_cpu(90))
```