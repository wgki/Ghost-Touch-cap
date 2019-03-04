#date:20180226
# Author:Kai Wang
import re
import sys
import time
import matplotlib.pyplot as plt
from pylab import *

with open(r'adb','r') as f1:
	data1=f1.readlines()
'''
data = [[] for i in range(17)]  #17行
for num,line in enumerate(data1):
    if num>3 and num<21:        #4-20
        data2=line.split(",")
        data[num-4]=[int(data2[i]) for i in range(30)]

X = np.linspace(0,16,17)
Y = np.linspace(0,29,30)
'''

data = [[] for i in range(15)]  #17行
for num,line in enumerate(data1):
    if num>4 and num<20:        #4-20
        data2=line.split(",")
        data[num-5]=[int(data2[i]) for i in range(30)]

X = np.linspace(1,15,15)
Y = np.linspace(0,29,30)

#8表示密集程度

figure(1)
C = contourf(Y, X, data, 20, alpha=.75, cmap='jet' )
#C = contour(Y, X, data, 20,colors='black', linewidth=.5)
plt.clabel(C,inline=1,fontsize=10)
plt.colorbar()
#cd.set_label('meters')

#plt.savefig('/home/k/adb/fig/'+str(sys.argv[1])+'.png')
T = time.strftime('%H%M%S',time.localtime(time.time()))
plt.savefig('/home/k/adb/fig/'+T+'.png')

'''
plt.ion()
plt.ioff()
plt.show()


time.sleep(2)
print(1)

plt.close()
'''



