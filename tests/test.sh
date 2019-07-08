#!/bin/bash
exit_code=0
for f in *.py
do
    python3 $f
    if [[ $? > 0 ]]; then
	exit_code=1
    fi
done
exit $exit_code
