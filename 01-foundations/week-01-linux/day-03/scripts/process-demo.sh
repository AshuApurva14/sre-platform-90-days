#!/bin/bash

# ```bash
# start process
#    ↓
# capture PID
#    ↓
# inspect process
#    ↓
# send signal
#    ↓
# verify termination

# ```

echo "Starting demo process..."

sleep 300 &

PID=$!

echo "Process started"
echo "PID: $PID"

echo "Process details:"
ps -p "$PID" -f

echo "Waiting 5 seconds..."
sleep 5

echo "Stopping process..."
kill "$PID"

sleep 1

echo "Verifying process..."
ps -p "$PID" || echo "Process stopped successfully"