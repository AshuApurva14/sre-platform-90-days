# awk

Now:
```bash
awk '{print $2}' labs/app.log
```
This prints the second whitespace-separated field.

Try:
```bash
awk '{print $2, $3}' labs/app.log
```
And:
```bash
awk '$2 == "ERROR" {print $0}' labs/app.log
```
Now you're doing basic log filtering.

Don't go deeper into AWK syntax today.

Your mental model:
```bash
awk
 ↓
read records
 ↓
split into fields
 ↓
filter/process
 ↓
print result

```

<img width="1571" height="584" alt="Image" src="https://github.com/user-attachments/assets/581f48f4-f0bd-4cda-97c2-163881dce39e" />