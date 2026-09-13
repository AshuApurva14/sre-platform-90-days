# Learn the basic commands

```bash
systemctl status <service>
systemctl start <service>
systemctl stop <service>
systemctl restart <service>
systemctl enable <service>
systemctl disable <service>
```

Undertand them as:

```bash
status
  → What is happening?

start
  → Start it now.

stop
  → Stop it now.

restart
  → Stop and start again.

enable
  → Start automatically at boot.

disable
  → Don't automatically start at boot.
```

A common beginner mistake is thinking:

`enable` means start now.

It doesn't.

Conceptually:

```bash
start  → now
enable → future boot/startup behavior

```

