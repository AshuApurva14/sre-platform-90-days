#!/bin/bash

echo "Starting test process..."

sleep 300 &
PID=$!

echo "Process PID: $PID"

echo
echo "Current process:"
ps -p "$PID" -o pid,ppid,user,stat,comm

echo
echo "Sending SIGTERM..."
kill -TERM "$PID"

sleep 1

if ps -p "$PID" > /dev/null; then
    echo "Process is still running"
else
    echo "Process terminated gracefully"
fi