# Conditions in python

1. if
2. if/ elif
3. if / elif/ else
4. comparision operator - >, <, >=, <= etc.
5. Logical operator - and, or , not



Example 1:

```
cpu = 85

if cpu >= 90:
    print("CRITICAL")
elif cpu >= 80:
    print("WARNING")
else:
    print("OK")
```

Example 2:

```
cpu = 90
memory = 85

if cpu >= 80 and memory >= 80:
   print(f"Multiple resources are high!")

```





Example 3:

```
disk = 95

if disk >= 90:
    print("CRITICAL: Disk usage is high")
elif disk >= 80:
    print("WARNING: Disk usage is high")
else:
    print("Disk usage is normal")

```