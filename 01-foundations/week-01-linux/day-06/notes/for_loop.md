# Learn for loops

Create:
```bash
nano labs/loop.sh
```
Use:
```bash
#!/bin/bash

for file in /etc/*.conf
do
    echo "Found: $file"
done
```
Run:
```bash
chmod 755 labs/loop.sh
./labs/loop.sh
```

Mental model:
```bash
files
 ↓
for each file
 ↓
perform operation
```
This becomes useful when you're working with:
```bash
logs
configuration files
servers
backups
deployments
```

<img width="1330" height="878" alt="Image" src="https://github.com/user-attachments/assets/6f813daa-5acf-457d-afc0-f4e15d904efe" />