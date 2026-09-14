# Command substitution

Now combine Bash with the Linux commands you learned during Days 1–5.

Create:

```bash
nano labs/system-info.sh
```

Use:

```bash
#!/bin/bash

HOSTNAME=$(hostname)
USER=$(whoami)
KERNEL=$(uname -r)

echo "Hostname: $HOSTNAME"
echo "User: $USER"
echo "Kernel: $KERNEL"
```

Run:

```bash
chmod 755 labs/system-info.sh
./labs/system-info.sh
```

This:

```bash
$(hostname)
```

means:
```bash
Execute hostname and use its output

```

This is extremely useful in automation.

<img width="1380" height="416" alt="Image" src="https://github.com/user-attachments/assets/ae955626-a7ba-4d8d-b11b-3aabaf9b4f87" />

