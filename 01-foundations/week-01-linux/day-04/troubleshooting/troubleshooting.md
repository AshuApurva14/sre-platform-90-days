# Process Termination Troubleshooting

## Scenario

A process needs to be stopped.

## Process

Name:

PID:

## Initial Inspection

```bash
ps -p <PID> -o pid,ppid,user,%cpu,%mem,stat,comm