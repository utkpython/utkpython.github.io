#bionary search

words = open('words.txt')

dictionary = []
for line in words:
    word = line.replace('\n','')
    dictionary.append(word)
    
'ant' in dictionary
'bug' in dictionary

#search
dic = dictionary
t = True
mid = len(dic)/2
mids = mid
word = 'fat'
index = 0
while t == True:
    if mids%2 == 0:
        mids = mids/2
    else:
        mids = mids/2 + 1
    index += 1
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

def search(word, list):
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
        if word == dic[mid]:
            return mid , dic[mid]
            t = False
        elif word < dic[mid]:
            mid = mid - mids
        else:
            mid = mid + mids
        if index > log(len(dic))/log(2) + 1:
            return "your word is not contained in this dictionary"
            
            
