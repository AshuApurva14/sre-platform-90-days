# Learn pipes

You've already seen:
```bash
ps aux | head -10
```
The pipe:
```bash
|
```
takes the output of one command and sends it to another.

Think:
```bash
Command A
   ↓ output
   |
   ↓
Command B
```
Example:
```bash
ps aux | grep python
```
means:

Get the process list and search it for Python.

Another:
```bash
systemctl list-units --type=service | grep running
```