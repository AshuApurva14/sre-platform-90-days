#!/bin/bash

# This script checks the health of a web server by sending an HTTP request and checking the response code.

echo "============================="
echo " Week 1 Linux Health Check"
echo "============================="

echo 
echo "========== SYSTEM ==========="
echo "Hostname: $(hostname)"
echo "User: $(whoami)"
echo "Uptime: "
uptime


echo 
echo "========= Memory ============"
free -h

echo 
echo "=========== Disk ============"
df -h \

echo 
echo "======== PORT 8080 ========="


if ss -lntp | grep -q ':8080'; then
    echo "Port 8080: LISTENING"
else 
    echo "Port 8080: NOT LISTENING"
fi

echo 
echo "========= HTTP CHECK ========"

if curl -s --max-time 5 http://localhost:8080 > /dev/null; then
    echo "HTTP service: HEALTHY"
else
    echo "HTTP service: NOT HEALTHY"
fi


echo 
echo "========= PYTHON SERVER ========"

if pgrep -f "http.server 8080" > /dev/null; then
    echo "Python HTTP process: RUNNING"
else
    echo "Python HTTP process: RUNNING"
fi





 
