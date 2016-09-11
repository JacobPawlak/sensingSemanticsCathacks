#!/bin/bash

if [ "$#" -ne 2 ]; then
	echo "Usage: autoScript.sh dataFile outPutFileName"
	exit -1
fi

python proj1.py "$1" > "$2"
python dataToLight.py "$2"
