# Understand `systemctl`

`systemctl` is your primary command to manage system-managed services.

Start with:

```bash
systemctl

```

Then:

```bash
systemctl list-units --type=service

```

This shows currently loaded service units.

<img width="1340" height="941" alt="Image" src="https://github.com/user-attachments/assets/57a23640-3602-4a98-b220-31f4e9ad9890" />

Then:

```bash
systemctl list-unit-files --type=service

```

This shows service unit files and their enablement state.

<img width="938" height="1849" alt="Image" src="https://github.com/user-attachments/assets/bb5fde1c-dabb-416c-9149-2e4f929dd495" />

---

### Find a safe service to practice with

Look at:

```bash
systemctl list-units --type=service | head -20

```
Find a service you recognize and can safely inspect.

For example, if `cron` exists:

```bash
systemctl status cron
```

<img width="1613" height="476" alt="Image" src="https://github.com/user-attachments/assets/0c2350c8-8472-4b9c-9ad0-77dfb94abeeb" />

### Do not randomly stop system-critical services.

Today your focus is learning the commands and investigation flow, not breaking your machine.

