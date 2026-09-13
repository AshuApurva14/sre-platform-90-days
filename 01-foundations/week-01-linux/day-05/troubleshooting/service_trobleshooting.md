# Your first service troubleshooting workflow

Suppose someone says:
```bash
"The service isn't working."
```
Don't do:
```bash
sudo systemctl restart <service>
```
immediately.

Use:
```bash
systemctl status <service>
```
Then:
```bash
journalctl -u <service> -n 50
```
Then:
```bash
ps -p <MAIN_PID> -f
```
Then investigate what the error is telling you.

Only after understanding the likely problem should you consider:
```bash
sudo systemctl restart <service>
```
Then verify:
```bash
systemctl status <service>
```

<img width="1585" height="1716" alt="Image" src="https://github.com/user-attachments/assets/a5ccd1b8-1562-44d6-87e9-41a1cd080ed2" />