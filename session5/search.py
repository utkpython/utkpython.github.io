#binary search

words = open('words.txt')

dictionary = []
for line in words:
    word = line.replace('\n','')
    dictionary.append(word)
    
'ant' in dictionary  
'bug' in dictionary   ##how does this work? How is it so fast?

#search
word = 'ant'
def slowsearch(word, dic):
    index = 0
    for i in dic:
        index += 1
        if word == i:
            return index
        


#smarter search
dic = dictionary
t = True
mid = len(dic)/2
mids = mid
word = 'big'
index = 0
while t == True:
    if mids%2 == 0:
        mids = mids/2
    else:
        mids = mids/2 + 1
    index += 1
    if mid < 0:
        mid = 0
    if word == dic[mid]:
        print mid
        print dic[mid]
        t = False
    elif word < dic[mid]:
        mid = mid - mids
        print mid
    else:
        mid = mid + mids
        print mid
        

dic = dictionary

def search(word, dic):
    t = True
    mid = len(dic)/2
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
        if word == dic[mid]:
            return mid , dic[mid]
            t = False
        elif word < dic[mid]:
            mid = mid - mids
        else:
            mid = mid + mids
        if index > log(len(dic))/log(2) + 1:
            return "your word is not contained in this dictionary"
            
#comparing          

import time

start = time.time()
slowsearch("zymurgy", dic)
end = time.time()
print end - start

start = time.time()
search("zymurgy", dic)
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
