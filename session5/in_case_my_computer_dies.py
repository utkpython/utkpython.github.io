import urllib2
import json

my_url = "http://www.reddit.com/r/babyelephantgifs.json"

request = urllib2.urlopen(my_url).read()

js = json.loads(request)

print type(js)
print "<!DOCTYPE HTML>"
for i in range(20):

    if str(js['data']['children'][i]['data']['url'])[-3:] == "gif":
        print "<img src=\"", js['data']['children'][i]['data']['url'],"\"> </img>"
        
print "</html>"


##generalized fibonacci

from random import randint
from pylab import *

fun = []
fun.append(randint(0,9999));
fun.append(randint(9,9999));


for i in range(2,100):
    fun.append(fun[i-1] + fun[i-2]);
    
print fun[0],fun[1]    
print len(fun)

dist = []

for i in range(len(fun)-1):
    dist.append(float(fun[i+1])/fun[i])
    
plot(dist)
show()

print float(fun[-1])/ float(fun[-2])
