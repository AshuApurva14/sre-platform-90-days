#!/bin/bash

HOSTNAME=$(hostname)
USER=$(whoami)
KERNEL=$(uname -r)

echo "Hostname: $HOSTNAME"
echo "User: $USER"
echo "Kernel: $KERNEL"

