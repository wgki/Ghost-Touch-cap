#!/bin/sh
#init script

source 11_env/bin/activate
for f in record/*;do
    echo $f
    echo start
    python3 result_sub.py $f
done

