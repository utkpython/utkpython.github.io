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
word = 'ant'
while t == True:
    mids = mids/2
    if word == dic[mid]:
        print mid
        print dic[mid]
        t = False
    if word < dic[mid]:
        mid = mid - mids
        print mid
    else:
        mid = mid + mids
        print mid
        
