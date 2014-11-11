# "God does not play dice" -Einstein
# well we play dice here at UTK.py
# goal... simulate dice rolling
from random import randint

die_rolls = []

print randint(1,6)

# review functions
def func(x,y):
    if type(x) != int or type(y) != int:
        return "fail"
    else:
        return 1

# what does the following code do? 
# print type(func) 

#what about this?
# print type(func(1,100))

#what about this?
# print type(func(1.0,1))


# review dict,list,tuple
