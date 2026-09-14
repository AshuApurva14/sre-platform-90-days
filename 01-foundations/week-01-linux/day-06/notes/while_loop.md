# Learn while

Create:

nano labs/while.sh

Use:
```bash
#!/bin/bash

COUNT=1

while [ "$COUNT" -le 5 ]
do
    echo "Count: $COUNT"
    COUNT=$((COUNT + 1))
done
```
Run:
```bash
chmod 755 labs/while.sh
./labs/while.sh
```

You should get:
```bash
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
```
Mental model:
```bash
condition true?
      ↓
run
      ↓
change condition
      ↓
repeat
```