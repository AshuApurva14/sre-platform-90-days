# SIGKILL

`SIGKILL` - Signal Kill

Mental Model:

```bash
SIGKILL
   ↓
Immediate forced termination

```
A process cannot catch and handle SIGKILL.

---

**Operational rule**

Use:

```bash
SIGTERM
   ↓
check
   ↓
SIGKILL only when necessary

```

Don't make kill -9 your default response.


<img width="1030" height="484" alt="Image" src="https://github.com/user-attachments/assets/2f4724e4-2a0d-4616-9445-b7b483381235" />