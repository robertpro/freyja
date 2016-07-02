#!/bin/bash
USER="$1"
PYTHON="/home/$USER/venvs/camera/bin/python"
BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd .. ; pwd )"

if test -z $USER; then 
    echo "No user given"
    exit 1
fi

cd $BASEDIR

$PYTHON main.py -i
$PYTHON main.py -u

