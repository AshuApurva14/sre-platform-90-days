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