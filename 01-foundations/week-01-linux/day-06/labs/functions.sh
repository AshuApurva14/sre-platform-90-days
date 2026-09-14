#!/bin/bash

check_file() {

    if [ -f "$1" ]; then
        echo "File exists: $1"
    else
        echo "File missing: $1"
    fi

}

