#bionary search

'''words = open('words.txt')

wordlist = []
for line in words:
    word = line.replace('\n','')
    wordlist.append(word)
    
'ant' in wordlist  
'bug' in wordlist   ##how does this work? 

#search
#word = 'ant'

def slowsearch(word, wordlist):
    index = 0
    for i in wordlist:
        index += 1
        if word == i:
            return index
        


#smarter search

t = True
mid = len(wordlist)/2
mids = mid
word = 'zymurgies'
index = 0
while t == True:
    if mids%2 == 0:
        mids = mids/2
    else:
        mids = mids/2 + 1
    index += 1
    if mid < 0:
        mid = 0
    if mid > len(wordlist):
        mid = len(wordlist)-1
    if word == wordlist[mid]:
        print mid
        print wordlist[mid]
        t = False
    elif word < wordlist[mid]:
        mid = mid - mids
        print mid
    else:
        mid = mid + mids
        print mid


def fastsearch(word, wordlist):
    t = True
    mid = len(wordlist)/2
    mids = mid
    index = 0
    while t == True:
        if mids%2 == 0:
            mids = mids/2
        else:
            mids = mids/2 +1
        index += 1
        if mid < 0:
            mid = 0
        if mid > len(wordlist):
            mid = len(wordlist)-1
        if word == wordlist[mid]:
            return mid , wordlist[mid]
            t = False
        elif word < wordlist[mid]:
            mid = mid - mids
        else:
            mid = mid + mids
        if index > log(len(wordlist))/log(2) + 1:
            return "your word is not contained in this wordlist"
            
#comparing          

import time

start = time.time()
slowsearch("zymurgy", wordlist)
end = time.time()
print end - start

start = time.time()
fastsearch("zymurgy", wordlist)
end = time.time()
print end - start

####real test

f = open("dict.txt")
i = 1
l = list()
for line in f:
    stripped = line.rstrip("\r\n\t").lower()
    if ('\'' in stripped):
        continue
    else:
        l.append(stripped)
        #print "Adding item " + str(i)
        i += 1

print "Done, processed " + str(i-1) + " items."

l.sort()

start = time.time()
slowsearch("zzz", l)
end = time.time()
print end - start

start = time.time()
search("zzz", l)
end = time.time()
print end - start
'''
#########

def bisearch(word, wordlist):
    t = True
    mid = len(wordlist)/2
    mids = mid
    index = 0
    while t == True:
        if mids%2 == 0:
            mids = mids/2
        else:
            mids = mids/2 +1
        index += 1
        if mid < 0:
            mid = 0
        if mid > len(wordlist):
            mid = len(wordlist)-1
        if word == wordlist[mid]:
            return True
            t = False
        elif word < wordlist[mid]:
            mid = mid - mids
        else:
            mid = mid + mids
        if index > log(len(wordlist))/log(2) + 1:
            return False
            
def nsearch(word, wordlist):
    index = 0
    for i in wordlist:
        index += 1
        if word == i:
            return True
    if index > len(wordlist):
        return False
        
