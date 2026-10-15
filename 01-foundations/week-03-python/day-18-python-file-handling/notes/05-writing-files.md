# Writing files

Suppose your health checker produces:

```
Server: web01
CPU: 82%
Memory: 65%
Overall: WARNING
```

You want to save it.
```
report = """Server: web01
CPU: 82%
Memory: 65%
Overall: WARNING
"""
```

```python
with open("health-report.txt", "w") as file:   
     file.write(report)
```

After running:
```
health-report.txt
```

will contain the report.


## Understand the danger of w

Run:

```python
with open("important.txt", "w") as file:  
       file.write("First report")
```


Then:

```python
with open("important.txt", "w") as file:   
      file.write("Second report")
```

The file doesn't contain both.

It contains:
```
Second report
```

because `"w"` **truncates/replaces** existing contents.

This is why blindly using w against production files can be dangerous.