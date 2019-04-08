#date:20190226
# Author:Kai Wang
import os
import re
import sys
import time
import matplotlib.pyplot as plt
from pylab import *

Path = './record/data'
tlist = []
files = os.listdir(Path)

X = np.linspace(1,15,15)
Y = np.linspace(0,29,30)
data = [[] for i in range(15)]  #17行
data0 = [[] for i in range(15)]  #17行
f1 = files[1]


with open(Path+'/0.csv','r') as f1:
    data1=f1.readlines()
for num,line in enumerate(data1):
    data2=line.split(",")
    data0[num-5]=[int(data2[i]) for i in range(30)]

for filename in files:
    (t,tmp) = os.path.splitext(filename)
    with open(Path+'/'+filename,'r') as f1:
        data1=f1.readlines()

    for num,line in enumerate(data1):
        data2=line.split(",")
        data[num-5]=[int(data2[i])-data0[num-5][i] for i in range(30)]

    #8表示密集程度
    #figure(1)
    C = contourf(Y, X, data, 20, alpha=.75, cmap='jet' )
    #C = contour(Y, X, data, 20,colors='black', linewidth=.5)
    plt.clabel(C,inline=1,fontsize=10)
    plt.colorbar()
    #cd.set_label('meters')
    T = time.strftime('%H%M%S',time.localtime(time.time()))
    plt.savefig('./record/fig/'+t+'.png')
    plt.close()

Path = './record/fig'
tlist = []
files = os.listdir(Path)
for filename in files:
    (t,tmp) = os.path.splitext(filename)
    tlist.append(int(t))

#print(tlist)
tlist = sorted(tlist)

plt.ion()
for t in tlist:
    im = plt.imread(Path+'/'+str(t)+'.png')
    plt.figure(1)  
    plt.imshow(im)
    plt.pause(0.1)


plt.ioff()
plt.show()
plt.close()






