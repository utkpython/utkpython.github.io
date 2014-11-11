import pandas
from collections import Counter

words = """The series was set in Memphis at a fictional mansion called Toad Hall, which was owned by one Big Guy Beck (Slim Pickens; Forrest Tucker), a very wealthy land baron. He had recently died of an undisclosed illness, and before he was cryogenically frozen, he had made out a videotaped will, a piece of which was played every week, by his lawyer, George Wilhoit (David Healy; Vernon Weddle).

The will's terms were harshest on Big Guy's oldest son, the snobbish Marshall Beck (Michael Lombard) and his equally snobbish wife Carlotta (Dixie Carter). Also aghast at the will's terms was Big Guy's wily younger wife, Kathleen (Delta Burke). The terms stated that the family wouldn't be able to collect a dime of their inheritance until they accepted Big Guy's illegitimate son, Wild Bill Westchester (Jerry Hardin) and his good-natured but ditzy wife Bootsie (Ann Wedgeworth) into their family.

Many of the situations stemmed from the conniving Kathleen, Marshall and Carlotta's schemes to declare the terms and constraints of the will invalid and also to rid themselves of Wild Bill and Bootsie, for to their minds, with them; not to mention the rest of the family, out of their lives, the snobs could live it up on the money. Their wildly outlandish schemes usually and inevitably ended up failing.

Also appearing were Nedra Volz, who played Big Guy's senile first wife, Winona Beck, called Mother B., who had escaped from her nursing home; and Charles Frank, who played Big Guy's younger son Stanley.

Stanley, independently wealthy because he invested his money wisely, and thus not concerned about his inheritance from his father, was the nicest of the whole lot. Usually, it was Stanley who was able to protect Wild Bill and Bootsie (whom he and Mother B. accepted outright) from the devious scheming of his stepmother, who lusted after him; and his conniving brother and sister in-law."""

words = '''I
like
pie'''

words = words.replace('\n', ' ')
words = words.replace('.', ' .')
words = words.replace('?', ' ?')
words = words.replace(')', ' )')
words = words.replace('(', '( ')
words = words.replace(';', ' ;')
words = words.replace(':', ' ;')
wordlist = words.split(" ")


unique = list(set(wordlist))

unique.sort()
sameunique = unique

combo = []
for i in range(len(wordlist)):
    if i == 0:
        combo.append( wordlist[i])
    else:
        combo.append( wordlist[i] + wordlist[i-1])

count = {}
for i in unique:
    count[i] = []
    for j in sameunique:
        count[i].append(combo.count( j+i))

 
b = Counter(wordlist)
counts = {}
for i in count:
    counts[i] = array(count[i])/float(b[i])

chain = pandas.DataFrame(counts, index = unique)




import numpy 
import random

i = random.sample(unique,1)[0]
print i
a = []
a.append(i)
while i != '.':
    i = (unique[list(numpy.random.multinomial(1, chain[i])).index(1)])
    a.append(i)
    print i
