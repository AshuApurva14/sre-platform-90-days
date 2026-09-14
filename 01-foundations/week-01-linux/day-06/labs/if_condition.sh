#!/bin/bash

if [ -f /etc/passwd ]; then
    echo "passwd exists"
else
    echo "passwd does not exist"
fi

if [ -d /tmp ]; then
    echo "/tmp exists"
fi


