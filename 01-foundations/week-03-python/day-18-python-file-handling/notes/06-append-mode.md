# Append mode

For logs, you usually don't want:
```
"w"
```


Imagine:

```
10:00 ERROR database unavailable
10:01 ERROR API timeout
```

A new error shouldn't delete previous errors.

Use:
```
"a"
```

Example:

```python
with open("errors.log", "a") as file:
    file.write("ERROR: Database unavailable\n")
```


Run again with another message:

```python
with open("errors.log", "a") as file:  
     file.write("ERROR: API timeout\n")
```


Now:
```
ERROR: Database unavailable
ERROR: API timeout`
```