#date:20180226
# Author:Kai Wang
import os
import re
import sys
import time
import matplotlib.pyplot as plt
import numpy as np
from pylab import *

def show_sub(tl):
    "显示2*2结果图"
    k=331
    for t in tl:
        subplot(str(k))
        im = plt.imread(Path+'/'+str(t)+'.png')
        plt.imshow(im)
        k = k+1
    return



Path = './record/data'
tlist = []
files = os.listdir(Path)

X = np.linspace(14,0,15)
Y = np.linspace(0,29,30)
data = [[] for i in range(15)]  #17行
'''
data0 = [[] for i in range(15)]  #17行

with open(Path+'/0.csv','r') as f1:
    data1=f1.readlines()
for num,line in enumerate(data1):
    data2=line.split(",")
    data0[num-5]=[int(data2[i]) for i in range(30)]
'''

#mea=[]
for filename in files:
    (t,tmp) = os.path.splitext(filename)
    with open(Path+'/'+filename,'r') as f1:
        data1=f1.readlines()
    for num,line in enumerate(data1):
        if num<15:
            data2 = line.strip('\n')
            data2 = data2.split(",")
            data[num] = [int(data2[i])-1573 for i in range(30)]

    data = np.array(data)
    #mea.append(data.mean())
    #滤波
    data[abs(data)<20] = 0
    #8表示密集程度
    #固定colorbar范围
    v = np.linspace(-300, 300, 30)
    C = contourf(Y, X, data, v,alpha=.75, cmap='jet')
    #C = contour(Y, X, data, 20,colors='black', linewidth=.5)
    plt.clabel(C,inline=1,fontsize=10)
    plt.colorbar()
    #T = time.strftime('%H%M%S',time.localtime(time.time()))
    plt.savefig('./record/fig/'+t+'.png')
    print(t)##
    plt.close()

Path = './record/fig'
tlist = []
files = os.listdir(Path)
for filename in files:
    (t,tmp) = os.path.splitext(filename)
    tlist.append(int(t))

#print(tlist)
tlist = sorted(tlist)


L = [tlist[i*9:(i+1)*9] for i in range(int(sys.argv[1]))]
for tl in L:
    if len(tl)>0:
        figure()
        show_sub(tl)
        subplots_adjust(left=0, bottom=0, right=1, top=1,wspace=0, hspace=0)


plt.show()
#plt.close()

#输出平均值
'''
mea = np.array(mea)
print(mea.mean())
'''




