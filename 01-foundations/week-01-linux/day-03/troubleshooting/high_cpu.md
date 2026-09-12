# High CPU Troubleshooting

## Problem

CPU usage increased unexpectedly.

## Detection

Used:

```bash
top

```
## Finding

Identified a high cpu process

```bash
pgrep yes

```

## Investigation

Checked:

```bash
ps -p <PID> -f

```

## Mitigation

Sent SIGTERM:

```bash
kill <PID>

```

## Verification

Confirmed the process stopped

```bash

ps -p <PID>

```

## Lesson Learned

Write what you learned.

This becomes the first entry in your troubleshooting portfolio.

- I learnt process identification.
- Check process and its resource consumption.
- Then ensure either process must be terminated or must be stopped.
- Able to use diff process kill methods for diff usecases.
- Show selected process  information


## Show process information which required or needed

e.g:

```bash

ps -p <PID> -o pid,ppid,user,%cpu,%mem,stat,comm

```
---


You should understand these:

### Process inspection

```bash
ps
ps aux
ps -ef
top
pstree

```

```bash
yes > /dev/null &

```

*"The server CPU is suddenly very high."*

<img width="1153" height="939" alt="Image" src="https://github.com/user-attachments/assets/c4b651ca-682b-479e-bec0-7151b580a034" />

<img width="983" height="1088" alt="Image" src="https://github.com/user-attachments/assets/63fca937-e41b-4836-b1a2-aed7d79ca162" />

