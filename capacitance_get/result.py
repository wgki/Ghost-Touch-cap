import os
import time
import matplotlib.pyplot as plt

Path = '/home/k/adb/fig'
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

