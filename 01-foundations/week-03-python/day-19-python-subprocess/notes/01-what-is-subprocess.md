# Learn `subprocess`

A `subprocess` is python standard-library module for starting and interacting with other programs. It is useful when python needs to run an existing command-line tool such as Git or Cloud CLI rather than do that tool's job itself.

For example:

```python
import subprocess
import sys

result = subprocess.run(
    [sys.executable, "-c", "print('hello')"],
    capture_output=True,
    text=True,
    check=True,
)
print(result.stdout)

```

## understand the problem subprocess solves

You already know Linux commands such as:

```bash
df -h
free -m
uptime
uname -a
```

And Kubernetes commands:

```kubectl
kubectl get pods
kubectl get nodes
kubectl describe pod ...
```

Git:

```git
git status
git log
```

Normally:

```
You
 ↓
Shell
 ↓
Command
 ↓
Output
```

With Python:

```
Python automation
      ↓
 subprocess
      ↓
OS command
      ↓
stdout / stderr / return code
      ↓
Python makes a decision
```

For example, later you could build:

```
Python
  ↓
kubectl get pods
  ↓
Find unhealthy pods
  ↓
Create report
  ↓
Send alert
```

That's why subprocess matters to SRE.