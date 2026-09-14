# Use `if`

Basic pattern:

```bash
if [ condition ]; then
    ...
else
    ...
fi
```

Example:

```bash
#!/bin/bash

if [ -f /etc/passwd ]; then
    echo "passwd exists"
else
    echo "passwd does not exist"
fi
```

Now test a directory:

```bash
if [ -d /tmp ]; then
    echo "/tmp exists"
fi
```

Common tests for today:

```bash
-f → file exists
-d → directory exists
-z → string is empty
-n → string is not empty

```
Don't try to memorize every Bash test.


<img width="1368" height="505" alt="Image" src="https://github.com/user-attachments/assets/b2600491-958b-446f-845e-54ad4ad77781" />