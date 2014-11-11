# "God does not play dice" -Einstein
# well we play dice here at UTK.py

from random import randint

die_rolls = []

print randint(1,6)
# simulate 10000 die being rolled
# can you do it?
# can you plot the results?



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

superpowers = { "Spiderman": ["smarts","web-spinning","pizza-cooking"],
                "Superman": ["strength", "flight", "being-handsome"],
                "Michelle Obama": ["smiling","world-domination"],
                "Ken Thompson": ["programming"]
             }

# write some code to show all of the people in the database             
# write some code to show how many powers each person has

myList = ["bro", "broski", "dude", "man", "dawg" ]

# what is the length of the list?
# what is the last element?
# what does this do?
for i in myList:
    print i
    
for i in reversed(myList):
    print i
    
    
# what is the difference between a tuple and a list?



