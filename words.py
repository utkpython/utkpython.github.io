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

uua = {}

for word in lista:
	if word not in uua:
		uua[word] = 1
	else:
		uua[word] = uua[word] + 1

uuas = sorted(uua)

for word in uuas:
	print word, uua[word]
	
"""
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
a = invert_dict(uua)

b = a.keys()

b.sort(reverse = True)

c = {}
for x in b[:15]:
    d = str(a[x]).strip('[]')
    c[d] = x
    
uua = c
	
"""	
	
	

X = np.arange(len(uua))
pl.bar(X, uua.values(), align='center', width=0.5)
pl.xticks(X, uua.keys())
ymax = max(uua.values()) + 1
pl.ylim(0, ymax)
pl.show()
