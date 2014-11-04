from random import randint
import matplotlib.pyplot as plt

#"""simple example to get us started"""
#num_heads = 0
#num_tails = 0
#for i in range(1, 10001):
#    if randint(0,1):
#        num_heads = num_heads + 1
#    else:
#        num_tails = num_tails + 1
#num_heads/float(num_heads + num_tails)


position = 0

walk = [position]

numSteps = 100000

for i in xrange(numSteps):
    if randint(0,1):
        step = 1         #take a step forward
    else:
        step = -1        #take a step backward
  
    position = position + step
  
    walk.append(position)

plt.plot(walk)
plt.show()
#########length to 20 sim

import matplotlib.pyplot as plt
from random import randint
position = 0

walk = [position]
lengths = []
numSteps = 1000

for i in xrange(numSteps):
    
    position = 0
    walk = [position]
    while abs(position) < 20:
        if randint(0,1)==1:
            step = 1         #take a step forward
        else:
            step = -1        #take a step backward    
        position = position + step    
        walk.append(position)
    lengths.append(len(walk))

plt.plot(lengths)
plt.show()
mean(lengths)


########2d
positionx = 0
positiony = 0

walkx = [positionx]
walky = [positiony]

numSteps = 10000
plt.show(block=False)

for i in xrange(numSteps):
    if randint(0,1)==1:
        stepx = 1         #take a step forward
    else:
        stepx = -1        #take a step backward
    if randint(0,1)==1:
        stepy = 1         #take a step forward
    else:
        stepy = -1        #take a step backward  
    positionx = positionx + stepx
    positiony = positiony + stepy
    walkx.append(positionx)
    walky.append(positiony)
    


plt.plot(walkx,walky,marker='',color='b')

##########3d
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

positionx = 0
positiony = 0
positionz = 0
xs = [positionx]
ys = [positiony]
zs = [positionz]
numSteps = 100
plt.show(block=False)

for i in xrange(numSteps):
    if randint(0,1)==1:
        stepx = 1         #take a step forward
    else:
        stepx = -1        #take a step backward
    if randint(0,1)==1:
        stepy = 1         #take a step forward
    else:
        stepy = -1        #take a step backward 
    if randint(0,1)==1:
        stepz = 1         #take a step forward
    else:
        stepz = -1        #take a step backward  
    positionx = positionx + stepx
    positiony = positiony + stepy
    positionz = positionz + stepz
    xs.append(positionx)
    ys.append(positiony)
    zs.append(positionz)
    
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 100
for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:

    ax.plot(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
