# modeling the idea that "students getting ahead in life"
# some start off in a higher spot
# some have more skill, some less

from random import randint
import matplotlib.pyplot as plt

def rand_walk(numSteps, position, skill):
    '''returns a random walk list of size numSteps
       position is the starting position
       skill is a measure of how far forward you are
            able to walk'''
    walk = [position]
    numSteps = numSteps
    for i in xrange(numSteps):
        if randint(0,1):
            step = 1 * skill       #take a step forward
        else:
            step = -1        #take a step backward
  
        position = position + step
  
        walk.append(position)
    
    return walk
