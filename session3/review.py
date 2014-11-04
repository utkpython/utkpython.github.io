####################
####################
# what does the 
# following block of
# code do?

def kablam(yourList):
    '''this is called a docstring.
    Ideally, it would tell you what this
    function does'''
    if type(yourList) != list:
        print "can't kablam"
    else:
        for i in yourList:
            print i

####################
####################
# now what does this 
# block of code do?

def kazam(yourList):
  '''this is another magical function'''
    if type(yourList) != list:
        print "can't kazam"
    else:
        LList = len(yourList)
        for i in range(1,LList):
            if yourList[i] > yourList[i-1]:
                kazam = yourList[i]
        return kazam
