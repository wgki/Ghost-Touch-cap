#!/bin/bash
#init script

adb devices
source 11_env/bin/activate
python3 init.py

