# A basic wikipedia scraper
# it graphs the frequencies of words in a given wikipedia article
import wikipedia
import string
import re
import pylab as pl
import numpy as np

a = wikipedia.page("Python (programming language)")

ua = string.upper(a.content)

ua = re.sub(r'[^\w\s]','',ua)

lista = string.split(ua)
########
jim = []
for i in lista:
    if i == "THE" or i == "A" or i == "OF" or i == "IS" or i == "OR" or i == "AND" or i == "TO" or i == "IN" or i == "FOR" or i == "AS" or i == "ARE" or i == "BY" or i == "BE" or i == "HAS" or i == "THAT" or i == "IT" or i == "WITH" or i == "WHICH" or i == "AN" or i == "ALSO" or i == "THAN"or i == "ON" or i == "THAT" or i == "THAT" or i == "USE" or i == "FROM"or i == "THIS"or i == "SUCH" or i == "3" or i == "SUCH" or i == "WAS" or i == "CAN" or i == "ITS" or i == "USED":
        jim = jim
    else:
        jim = jim + [i]
lista = jim
#########
uua = {}

for word in lista:
	if word not in uua:
		uua[word] = 1
	else:
		uua[word] = uua[word] + 1

uuas = sorted(uua)

for word in uuas:
	print word, uua[word]
	
##########
b = []
a = uua.values()

lennnn = 10

a.sort(reverse  = True)
k = list(unique(a[:lennnn]))
k.sort(reverse = True)

for i in k:
    for j in uua:
        if uua[j] == i:
            b = b + [j]
            if len(b) == len(a[0:lennnn]):
                break



uuaa = b

X = np.arange(len(uuaa))
pl.bar(X, a[:lennnn], align='center', width=0.5)
pl.xticks(X, b)
ymax = max(a) + 1
pl.ylim(0, ymax)
pl.show()

########	
	
'''
X = np.arange(len(uua))
pl.bar(X, uua.values(), align='center', width=0.5)
pl.xticks(X, uua.keys())
ymax = max(uua.values()) + 1
pl.ylim(0, ymax)
pl.show()	

