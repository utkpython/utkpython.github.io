import wikipedia
import string
import re

a = wikipedia.page("Python (programming language)")
b = wikipedia.page("R (programming language)")

ua = string.upper(a.content)
ub = string.upper(b.content)

ua = re.sub(r'[^\w\s]','',ua)

lista = string.split(ua)
listb = string.split(ub)

uua = {}
uub = []

for word in lista:
	if word not in uua:
		uua[word] = 1
	else:
		uua[word] = uua[word] + 1

uuas = sorted(uua)

for word in uuas:
	print word, uua[word]

import pylab as pl
import numpy as np

X = np.arange(len(uua))
pl.bar(X, uua.values(), align='center', width=0.5)
pl.xticks(X, uua.keys())
ymax = max(uua.values()) + 1
pl.ylim(0, ymax)
pl.show()
