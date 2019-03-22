#date:20180226
# Author:Kai Wang
import os
import re
import sys
import math
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
        plt.axis('off')
    return


Width = 30
Height = 15
Name = sys.argv[1]
Name = Name[Name.rfind('/')+1:]
#print(Name)##
Path = './record/'+Name+'/'
fig_Path='./fig/'+Name

if not os.path.exists('fig'):
    os.mkdir('fig')
if not os.path.exists(fig_Path):
    os.mkdir(fig_Path)
##print(Path)##
tlist = []
files = os.listdir(Path)
##print(files)##

X = np.linspace(Height-1,0,Height)
Y = np.linspace(0,Width-1,Width)
data = [[] for i in range(Height)]  #17行
'''
data0 = [[] for i in range(15)]  #17行

with open(Path+'/0.csv','r') as f1:
    data1=f1.readlines()
for num,line in enumerate(data1):
    data2=line.split(",")
    data0[num-5]=[int(data2[i]) for i in range(30)]
'''

#mea=[]

######################################################################
##获取数据作等高线图
for filename in files:
    (t,tmp) = os.path.splitext(filename)
    ##print(t)##
    with open(Path+'/'+filename,'r') as f1:
        data1=f1.readlines()
    for num,line in enumerate(data1):
        if num<7+Height/2 and num>=7-Height/2:
            data2 = line.strip('\n')
            data2 = data2.split(",")
            data[num-math.ceil(7-Height/2)] = [int(data2[i])-1573 for i in range(int(15-Width/2),int(15+Width/2))]

    data = np.array(data)
    #mea.append(data.mean())
    #滤波
    data[abs(data)<30] = 0
  
    ##print(data)##
    #固定colorbar范围
    plt.figure(figsize=(36, 18))
    v = np.linspace(-150, 150, 30)
    C1 = contourf(Y, X, data, v,alpha=1, cmap='jet')
    plt.colorbar()
    C = contour(Y, X, data, 30,colors='black')  #20表示密集程度
    plt.clabel(C,inline=1,fontsize=16)
    #T = time.strftime('%H%M%S',time.localtime(time.time()))
    plt.savefig(fig_Path+'/'+t+'.png')
    print(t)##
    plt.close()



######################################################################
##作子图
Path = './fig/'+Name
tlist = []
files = os.listdir(Path)
for filename in files:
    (t,tmp) = os.path.splitext(filename)
    tlist.append(int(t))

#print(tlist)
tlist = sorted(tlist)


L = [tlist[i*9:(i+1)*9] for i in range(10)]
cnt_L = 0
for tl in L:
    cnt_L = cnt_L+1
    if len(tl)>0:
        figure()
        show_sub(tl)
        subplots_adjust(left=0, bottom=0, right=1, top=1,wspace=0, hspace=0)
        plt.savefig(fig_Path+'/'+str(cnt_L)+'.png')
#plt.show()


#plt.close()

#输出平均值
'''
mea = np.array(mea)
print(mea.mean())
'''




