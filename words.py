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

common_words = ["THE"  ,"A"  ,"OF"  ,"OR"  ,"IS"  ,"AND"  ,"TO"  ,"IN"  ,"FOR"  ,"AS"  ,"ARE"  ,"BY"  ,"BE"  ,"HAS"  ,"THAT"  ,"IT"  ,"WITH"  ,"WHICH"  ,"AN"  ,"ALSO"  ,"THAN" ,"ON"  ,"THAT"  ,"THAT"  ,"USE"  ,"FROM" ,"THIS" ,"SUCH"  ,"3"  ,"SUCH"  ,"WAS"  ,"CAN"  ,"ITS"  ,"USED"]
unique_words = []
for i in lista:
    if i not in common_words:
        unique_words = unique_words + [i]
lista = unique_words


uua = {}

for word in lista:
	if word not in uua:
		uua[word] = 1
	else:
		uua[word] = uua[word] + 1

uuas = sorted(uua)

for word in uuas:
	print word, uua[word]
	



sorted_words = []
sorted_count = []
for key, value in sorted(uua.iteritems(), key = lambda (k,v): (v,k)):
    sorted_words = sorted_words + [key] 
    sorted_count = sorted_count + [value]
sorted_words[::-1][:10]
sorted_count[::-1][:10]

   
    
b = sorted_words[::-1][:10]
a = sorted_count[::-1][:10]


X = np.arange(len(b))
pl.bar(X, a, align='center', width=0.5)
pl.xticks(X, b)
ymax = max(a) + 1
pl.ylim(0, ymax)
pl.show()

