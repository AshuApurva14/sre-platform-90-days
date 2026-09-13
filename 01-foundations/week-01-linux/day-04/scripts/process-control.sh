#!/bin/bash

echo "Starting process..."
sleep 300 &
PID=$!

echo "PID: $PID"

echo
echo "1. Stopping process with SIGSTOP..."
kill -STOP "$PID"

sleep 2

echo "Process state:"
ps -p "$PID" -o pid,stat,comm

echo
echo "2. Continuing process with SIGCONT..."
kill -CONT "$PID"

sleep 2

echo "Process state:"
ps -p "$PID" -o pid,stat,comm

echo
echo "3. Terminating process with SIGTERM..."
kill -TERM "$PID"

sleep 1

if ps -p "$PID" > /dev/null; then
    echo "Process still exists"
else
    echo "Process terminated"
fi