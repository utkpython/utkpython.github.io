#!/usr/bin/env python

from itertools import permutations



f = open("dict.txt")
i = 1
l = list()
for line in f:
    stripped = line.rstrip("\r\n\t").lower()
    if ('\'' in stripped or len(stripped) not in range(1,7)):
        continue
    else:
        l.append(stripped)
        #print "Adding item " + str(i)
        i += 1

print "Done, processed " + str(i-1) + " items."

f.close()
l.sort()

while True:
    i = raw_input("Search for: ")
    if (i.lower() == "exit" or i.lower() == "quit"):
        break
    if (len(i) > 6):
        print "Length must be equal to or less than 6."
        continue
    perms = []
    for m in range(1,len(i)+1):    
        perm = [''.join(p) for p in permutations(i,m)]
        perms = perms + perm
    perms = list(set(perms))
    perms.sort(key=len)
    unique = []
    for p in perms:
        if (nsearch(p, l)) and p not in unique:
            print "Possilbe string: " + p
            unique.append(p)


while True:
    i = raw_input("Search for: ")
    if (i.lower() == "exit" or i.lower() == "quit"):
        break
    if (len(i) > 6):
        print "Length must be equal to or less than 6."
        continue
    perms = []
    for m in range(1,len(i)+1):    
        perm = [''.join(p) for p in permutations(i,m)]
        perms = perms + perm
    perms = list(set(perms))
    perms.sort(key=len)
    unique = []
    for p in perms:
        if (bisearch(p, l)) and p not in unique:
            print "Possilbe string: " + p
            unique.append(p)
