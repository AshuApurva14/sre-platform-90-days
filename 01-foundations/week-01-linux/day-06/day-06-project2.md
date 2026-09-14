# Build your process health-check

This is where Day 3 and Day 6 come together.

Create:

nano scripts/process-check.sh

Use:

#!/bin/bash

PROCESS="$1"

if [ -z "$PROCESS" ]; then
    echo "Usage: $0 <process-name>"
    exit 1
fi

PID=$(pgrep -o "$PROCESS")

if [ -n "$PID" ]; then
    echo "Process: $PROCESS"
    echo "PID: $PID"

    ps -p "$PID" \
       -o pid,ppid,user,%cpu,%mem,stat,comm
else
    echo "Process '$PROCESS' is not running"
    exit 1
fi

Make executable:

chmod 755 scripts/process-check.sh

Test:

sleep 300 &

Then:

./scripts/process-check.sh sleep

Terminate:

kill "$(pgrep -o sleep)"

Then:

./scripts/process-check.sh sleep

This is your first real example of Python/Bash-style DevOps automation thinking, even though you're currently using Bash.