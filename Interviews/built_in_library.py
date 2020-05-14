####### String module
import string 

string.ascii_uppercase

string.ascii_lowercase

string.letters

string.digits

string.hexdigits

string.octdigits

string.punctuation

string.printable

string.whitespace

uppercase_set = set(string.ascii_uppercase)
#use set to check membership to save time

whitespace_set = set(string.whitespace)

###remove white space 
s = "Hello World"
''.join(e for e in s if e not in whitespace_set)

####### Itertools module

import itertools as it 

it.repeat

repeat_one = it.repeat(1)

next(repeat_one)
next(repeat_one)

list(repeat_one) # this will go on forever

map(pow, range(10), it.repeat(2))

all_ones = it.repeat(1, times=5)
list(all_ones)

it.cycle 

alternating_ones = it.cycle([1, -1])

it.permutations #order matters
friends = ['A', 'B', "C"]
it.permutations(friends, r=2)
list(it.permutations(friends, r=2))

#when order does not matter
list(it.combinations(friends, r=3))


########## Functools module
from functools import reduce

reduce(lambda x,y: x+y, [1,2,3,4])
#returns 10

reduce(lambda x,y:x*y, [1,2,3,4], 10)
#returns 240

from functools import cached_property, lru_cache

class Data:
    def __init__(self, n):
        self.n = n 

    @cached_property
    def f(self):
        total = 0 
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    total += i + j + k
        return total

@lru_cache
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

###### Doctest module and assert
class A:
    def f(self):
        '''
        >>> a = A()
        >>> a.f()
        Hello World
        'Hello World'
        '''
        print('Hello World')
        return 'Hello World'

    @property
    def error(self):
        '''
        >>> A().error
        Traceback (most recent call last):
        ...
        Exception: I am an error
        '''
        raise Exception("I am an error")


#python3 -m doctest ...py

#### assert
def g(x):
    assert x>0, "Invalid Input"

def lst_one_more(lst1, lst2):
    assert len(lst1) == len(lst2), "List Length not the same"
    for i in range(len(lst1)):
        lst1[i] = lst2[i] + 1 

lst1 = [1,1,1]
lst2 = [1,2,3]
lst_one_more(lst1, lst2)
for idx, value in enumerate(lst1):
    assert x == lst2[i] + 1 

