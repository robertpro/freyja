#!/bin/bash
USER="$1"
PYTHON="/home/$USER/venvs/camera/bin/python"

if test -z $USER; then 
    echo "No user given"
    exit 1
fi

if [ "$USER" == "pi" ]; then
    cd /home/$USER/camera/
else
    cd ..
fi

$PYTHON main.py -i
$PYTHON main.py -u

