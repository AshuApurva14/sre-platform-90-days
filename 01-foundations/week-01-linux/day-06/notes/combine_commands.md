# Combine commands

This is where Linux automation starts becoming powerful.

Count errors:
```bash

grep ERROR labs/app.log | wc -l
```
Show only error lines:
```bash
grep ERROR labs/app.log
```
Extract dates from error lines:
```bash
grep ERROR labs/app.log | cut -d' ' -f1
```
Use AWK:
```bash
awk '$2 == "ERROR" {print $0}' labs/app.log
```
Now you're building pipelines:
```bash
log
 ↓
filter
 ↓
transform
 ↓
count

```


<img width="1510" height="560" alt="Image" src="https://github.com/user-attachments/assets/2fda983e-ff3c-4abd-9a39-2c2d4de4055d" />