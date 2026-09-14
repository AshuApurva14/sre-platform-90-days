#!/bin/bash

FILE="$1"

if [ -z "$FILE" ]; then
    echo "Usage: $0 <file>"
    exit 1
fi

if [ -f "$FILE" ]; then
    echo "File exists: $FILE"
else
    echo "File does not exist: $FILE"
    exit 1
fi