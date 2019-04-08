#!/bin/bash
#get tp_capacitance_data

adb shell cp /proc/touchscreen/tp_capacitance_data /mnt/sdcard/log/log$1
wait
