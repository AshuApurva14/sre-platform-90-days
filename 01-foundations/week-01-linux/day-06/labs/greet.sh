#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <name>"
    exit 1
fi
echo "Script: $0"
echo "First argument: $1"
echo "Second argument: $2"