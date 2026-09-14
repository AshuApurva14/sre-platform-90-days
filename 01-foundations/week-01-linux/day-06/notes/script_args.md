# Script arguments

This is very important for DevOps scripts.

Create:

```bash
nano labs/greet.sh
```
Use:

```bash
#!/bin/bash

echo "Hello $1"
```

Make executable:

```bash
chmod 755 labs/greet.sh
```

Run:
```bash
./labs/greet.sh Ashutosh
```

## Understand $1

```bash
$1 → first argument
$2 → second argument
$3 → third argument
```
And:
```bash
$0
```
is typically the script name.

Example:
```bash
#!/bin/bash

echo "Script: $0"
echo "First argument: $1"
echo "Second argument: $2"
```

Run:
```bash
./labs/greet.sh Ashutosh DevOps

```

<img width="1347" height="633" alt="Image" src="https://github.com/user-attachments/assets/6fe148dc-0833-4873-ad4d-73645108bcf4" />