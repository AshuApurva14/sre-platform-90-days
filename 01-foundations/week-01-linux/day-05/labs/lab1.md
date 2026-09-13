# Check whether your system uses `systemd` or not?

Run below commands:

```bash
ps -p 1 -f
```

On a normal system using systemd, PID 1 will typically be:

```bash
systemd
```

Also:

```bash
systemctl --version

```
Important for WSL

Your WSL environment may or may not be running systemd depending on its configuration.

Check:

```bash
ps -p 1 -o pid,comm,args

```

Hands on Solution:

<img width="1989" height="351" alt="Image" src="https://github.com/user-attachments/assets/ca3a4cd7-46dd-4658-9496-f4cd95a6c781" />

