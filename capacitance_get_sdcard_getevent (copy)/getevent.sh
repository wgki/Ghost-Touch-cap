#!/bin/bash
#get tp_position

rm ts.txt
adb shell getevent|grep -e "0035" -e "0036">ts.txt

