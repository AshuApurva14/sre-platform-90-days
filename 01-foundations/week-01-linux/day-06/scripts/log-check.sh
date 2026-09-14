#!/bin/bash

LOG_FILE=$1

if [ -z "$LOG_FILE" ]; then
    echo "Usage: $0 <log_file>"
    exit 1
fi

if [ ! -f "$LOG_FILE" ]; then
    echo "File not found: $LOG_FILE"
    exit 1
fi

echo "========= LOG HEALTH CHECK ========="
echo "Total lines: $(wc -l $LOG_FILE)"
echo "ERROR Count: $(grep -c ERROR $LOG_FILE)"
echo "WARN count: $(grep -c WARN $LOG_FILE)"

echo
echo "========== ERRORS ============"

grep "ERROR" "$LOG_FILE" ||  echo "No errors found."

echo
echo "========== WARNINGS ============"

grep "WARN" "$LOG_FILE" || echo "No warnings found."




