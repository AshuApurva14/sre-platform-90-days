# Understand What a `Service` is?

A `Service` is a program/process that is managed as system service and usually runs in the background.

Think:

```bash
Executable / application
        ↓
Process
        ↓
Service management
        ↓
systemd

```

Example:

```bash
nginx
sshd
cron
docker
```
depedening on the machine.

A Service Manager can:

```bash
start it
stop it
restart it
monitor its state
start it at boot
collect/manage its logs

```
### Understand service states

```bash
active (running)
inactive
failed
activating
deactivating
```

### Active

The service is considered active.

### Inactive

The service is not currently running.

### Failed

The service attempted to start or run and encountered failure.


When you troubleshoot, you care about the state before you take action.

