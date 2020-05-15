numbers = [6,9,3,1]
sorted(numbers)

#numbers not changed 

numbers_tuple = (6,9,3,1)
numbers_set = {5,10,1,0}

sorted(numbers_tuple)

sorted(numbers_set)

#will return list
# 

### Sorting strings 

s = '34521'
s2 = 'I like to sort'
sorted(s) #['1', '2', '3', '4', '5']
sorted(s2)
sorted(s2.split())

names = ['harry', 'suzzy', 'al', 'mark']

sorted(names)

sorted(names, reverse=True)

#### Passing in a key argument 

words = ['banana', 'pie', 'book', 'pie']
sorted(words)
sorted(words, key=len)

def reverse_word(word):
    return word[::-1]

sorted(words, key = reverse_word)

sorted(words, key=lambda x: x[::-1])

values_to_sort = [5,2,6,1]
values_to_sort.sort() #sort in place
#cannot do string.sort()

#sort() returns None

phrases = [
    'when in rome',
    'what goes around comes around',
    'all is fair in love and war'
]

phrases.sort(key=lambda x: x.split()[2][1], reverse=True)

print(phrases)

###### Common issues
##mixed type
#upper/lower cases 

### When to use sorted() and sort()
from collections import namedtuple 
Runner = namedtuple('Runner', 'bibnumber duration')
runners = []
runners.append(Runner('27345','1500'))
runners.append(Runner('27346','1400'))
runners.append(Runner('27347','1450'))
runners.append(Runner('27357','1650'))
runners.append(Runner('27327','1750'))

runners.sort(key=lambda x: getattr(x, 'duration'))
top_five_runners = runners[:5]

#runners has been mutated; sorted() can be a better choice


