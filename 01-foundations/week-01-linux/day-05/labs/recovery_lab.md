# Recovery lab: stop/start a service

Choose a safe lab service.

For example, if cron is present:
```bash
systemctl status cron
```
Then:
```bash
sudo systemctl stop cron
```
Check:
```bash
systemctl status cron
```
Then:
```bash
sudo systemctl start cron
```
Check:
```bash
systemctl status cron
```
Then inspect recent logs:
```bash
journalctl -u cron -n 20
```

What did you learn?
```bash
stop
 ↓
service inactive

start
 ↓
service active

logs
 ↓
evidence
```

<img width="1585" height="1716" alt="Image" src="https://github.com/user-attachments/assets/a5ccd1b8-1562-44d6-87e9-41a1cd080ed2" />
