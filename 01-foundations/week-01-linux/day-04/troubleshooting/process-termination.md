# Process Termination Troubleshooting

## Scenario

A process needs to be stopped.

## Process

Name: `sleep `

PID: `12585`

## Initial Inspection

```bash
ps -p <PID> -o pid,ppid,user,%cpu,%mem,stat,comm

```

```bash
ps -p 12585 -o pid,ppid,user,%cpu,%mem,stat,comm

```

## First Action

Sent `SIGTERM.`





```bash
kill -TERM <PID>

```
Execute:

```bash
kill -TERM 12585

```

## Verification:

```bash
ps -p <PID>

```
Execute:

```bash
ps -p 12585
```

## Escalation

`SIGKILL` would only be used if the process remained running
and forceful termination was justified.

## Final Result

## Lesson Learned

- `SIGTERM` requests graceful termination.
- `SIGKILL` forces termination.
- Always verify after taking action.

