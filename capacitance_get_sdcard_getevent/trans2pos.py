#date:20190226
# Author:Kai Wang
import matplotlib.pyplot as plt
import numpy as np

Path = 'ts.txt'
track = []
X = []
Y = []

with open(Path,'r') as f1:
    data1=f1.readlines()
for num,line in enumerate(data1):
    if len(line)==38:
        if num%2 == 0:
            x = line[29:37]
            pos_x = int(x,16)*0.75 
        if num%2 == 1:
            y = line[29:37]
            pos_y = 1920-int(y,16)*0.75 
            track.append((pos_x,pos_y))
            X.append(pos_x)
            Y.append(pos_y)


f = plt.figure(figsize=(4.5, 8))
fig = f.add_subplot(1,1,1)
fig.set_title("track")
fig.set_xlabel("x")
fig.set_ylabel("y")
fig.plot(X,Y,c='r',ls='-')
plt.xlim(xmax=1080,xmin=0)
plt.ylim(ymax=1920,ymin=0)
plt.show()

