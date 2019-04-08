#!/bin/bash
#Loop script

source 11_env/bin/activate
echo Run times: $1
for a in `seq $1`
do
sh get.sh $a
echo $a
done


for a in `seq $1`
do
adb pull /mnt/sdcard/log/log$a adb
python3 get.py
echo $a
done

