# Connect service + PID + logs

This is the most important Day 5 exercise.

Run:
```bash
systemctl status cron
```
Identify:
```bash
Main PID
```
Then:
```bash
ps -p <MAIN_PID> -f
```
Then:
```bash
journalctl -u cron -n 20
```
You have now built:
```bash
SERVICE
   │
   ├── systemctl → state
   │
   ├── Main PID → process
   │
   └── journalctl → logs
```
That is the core Day 5 model.

<img width="1632" height="1144" alt="Image" src="https://github.com/user-attachments/assets/841a386d-ab7b-4917-9390-6ccd3ba31d22" />
