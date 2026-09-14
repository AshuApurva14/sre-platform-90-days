#!/bin/bash

echo "===== SYSTEM ====="
echo "Hostname: $(hostname)"
echo "User: $(whoami)"
echo "Kernel: $(uname -r)"

echo 
echo "===== UPTIME ====="
uptime

echo 
echo "===== MEMORY ====="
free -h

echo
echo "===== DISK ====="
df -h /

echo 
echo "===== PROCESSES ====="
ps aux | head -10