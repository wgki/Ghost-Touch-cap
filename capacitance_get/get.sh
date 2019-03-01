#!/bin/bash
adb shell cp /proc/touchscreen/tp_capacitance_data /mnt/sdcard/log/log
adb pull /mnt/sdcard/log/log adb
python3 get.py
wait
