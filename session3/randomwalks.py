from random import randint
import matplotlib.pyplot as plt

"""simple example to get us started"""
#heads = 0
#tails = 0
#for i in range(1, 10001):
#    if randint(0,1):
#        heads = heads + 1
#    else:
#        tails = tails + 1
#heads/float(heads+tails)


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

