Learn functions

Create:
```bash
nano labs/functions.sh
```
Use:
```bash
#!/bin/bash

check_file() {
    if [ -f "$1" ]; then
        echo "File exists: $1"
    else
        echo "File missing: $1"
    fi
}

check_file /etc/passwd
check_file /tmp/test.txt

```
Run:
```bash
chmod 755 labs/functions.sh
./labs/functions.sh
```
The benefit of functions:
```bash
Repeated logic
     ↓
Function
     ↓
Call whenever needed
```

This becomes especially useful in larger automation scripts.