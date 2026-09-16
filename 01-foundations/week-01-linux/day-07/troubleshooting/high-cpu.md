# Incident 3 — High CPU

Create the problem:
```bash
yes > /dev/null &
```
Now:
```bash
top
```
Find the process:
```bash
pgrep yes
```
Inspect it:
```bash
ps -p <PID> -o pid,ppid,user,%cpu,%mem,stat,comm
```
You should see the CPU impact.

Stop it:

```bash
kill <PID>
```
Verify:
```bash
ps -p <PID>
```
Then check top again.

Your incident workflow:
```bash
High CPU
   ↓
top
   ↓
find PID
   ↓
inspect process
   ↓
terminate
   ↓
verify
```

<img width="1629" height="1774" alt="Image" src="https://github.com/user-attachments/assets/a9cbe2fc-96a5-4b6e-8911-59e0cb9bc7a5" />

