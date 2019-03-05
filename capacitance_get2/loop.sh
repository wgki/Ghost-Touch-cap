#!/bin/bash
#Loop script

source 11_env/bin/activate
echo Run times: $1
for a in `seq $1`
do
sh get.sh
echo OK
done

