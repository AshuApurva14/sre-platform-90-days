# Learn argument validation

Modify your script:
```bash
#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <name>"
    exit 1
fi

echo "Hello $1"
```

Now:
```bash
./labs/greet.sh
```
You'll see:

```bash
Usage: ./labs/greet.sh <name>
```

Then:
```bash
./labs/greet.sh Ashutosh
```
It works.

This is the beginning of writing scripts that don't silently fail.

<img width="1428" height="372" alt="Image" src="https://github.com/user-attachments/assets/4f187a98-676b-4022-b0b2-10eb530efcea" />