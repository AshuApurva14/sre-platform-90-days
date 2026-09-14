# Understand what a shell script is

You've already been running commands:

```bash
whoami
uptime
df -h
free -h
ps
```

A shell script is simply a file containing commands that the shell can execute in sequence.

```bash
Think:

Manual work
   ↓
Repeated commands
   ↓
Script
   ↓
Automation
```

This is one of the fundamental DevOps skills.

---

## Understand the shebang

This line:
```bash
#!/bin/bash
```
is called the shebang.

It tells the system which interpreter should execute the script.

Conceptually:

```bash
script.sh
   ↓
#!/bin/bash
   ↓
Bash
   ↓
execute commands
```

For today, remember:
```bash
#!/bin/bash
```

means:
```bash
Run this script using Bash
```
