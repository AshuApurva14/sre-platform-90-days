# Recovery incident lab

**Scenario**

A process running but needs to be stopped safely.

Start:

```bash
sleep 300 &

PID=$!

echo "PID=$PID"

```

Inspect:

```bash
ps -p $PID -o pid,ppid,user,%cpu,%mem,stat,comm
```

<img width="1300" height="864" alt="Image" src="https://github.com/user-attachments/assets/46a347b9-e092-48cf-b115-7da02b2d76e7" />

---

Your decision making becomes:

```bash
Need to terminate process
        ↓
SIGTERM
        ↓
Wait/check
        ↓
Still running?
        ↓
SIGKILL if justified
        ↓
Verify

```