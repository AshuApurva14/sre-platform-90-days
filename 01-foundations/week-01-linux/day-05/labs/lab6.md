# Learn `journalctl`

Think:

```bash
systemctl
   ↓
What is the service state?

journalctl
   ↓
What happened inside/around the service?

```
You'll probably see a lot of messages.

Don't read everything.


<img width="2367" height="1835" alt="Image" src="https://github.com/user-attachments/assets/254c66bf-19e6-44c3-abec-2a49d8fb7c1e" />



Filter by service:


```bash
journalctl -u cron
```

Here:
```bash
-u
 ↓
unit
```

So:
```bash
journalctl -u cron
```
means:

Show logs associated with the `cron` unit.

<img width="1982" height="1834" alt="Image" src="https://github.com/user-attachments/assets/61e00559-59c4-4dee-99eb-6b540449c98a" />

---

## Limts logs

Don't dump thousands of lines.

Use:
```bash
journalctl -u cron -n 20
```
This shows recent entries.

Or:
```bash
journalctl -u cron --since "1 hour ago"
```
This is useful when troubleshooting a recent failure.


<img width="1736" height="757" alt="Image" src="https://github.com/user-attachments/assets/863013da-4244-4738-bf80-45ac9f9ecd9b" />

## Follow logs live

Use:
```bash
journalctl -u cron -f
```
The -f behavior is similar to:
```bash
tail -f
```
It follows new log entries as they arrive.

This is a useful operational pattern:
```bash
start/restart service
        ↓
journalctl -f
        ↓
watch what happens
```
Exit with:
```bash
Ctrl+C
```
<img width="1702" height="313" alt="Image" src="https://github.com/user-attachments/assets/dc81aaec-7a13-40a5-b680-c883addc6145" />