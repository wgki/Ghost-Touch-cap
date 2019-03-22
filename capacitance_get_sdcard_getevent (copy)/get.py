#date:20190226
# Author:Kai Wang
import re
import sys
import time
import matplotlib.pyplot as plt
from pylab import *

with open(r'adb','r') as f1:
	data1=f1.readlines()

results=[]

data = [[] for i in range(15)]  #17行
for num,line in enumerate(data1):
    if num>4 and num<20:        #4-20
        results.append(line)
        data2=line.split(",")
        data[num-5]=[int(data2[i]) for i in range(30)]

T = time.strftime('%M%S',time.localtime(time.time()))
ct = time.time()
secm = str(round(ct * 100 % 100))
with open('./record/data/'+T+secm+'.csv','w') as f2:
	f2.writelines(results)

