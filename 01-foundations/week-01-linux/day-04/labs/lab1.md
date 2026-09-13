# Learn `SIGINT` with `Ctrl+C`

`SIGIINT` - Signal Interrupted

Start:

```bash
sleep 300

```

The command is running in foreground.

```bash
press `ctrl+c`
```

Conceptually:

```bash
Ctrl+C
   ↓
SIGINT
   ↓
foreground process
   ↓
process interrupted

```

What you need to remember

`Ctrl+C` is normally used to interrupt the foreground command you're currently running.