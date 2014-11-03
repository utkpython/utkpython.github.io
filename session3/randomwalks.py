from random import randint
import matplotlib.pyplot as plt

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

