########## Set
def count_unique(s):
    '''
    Count number of unique characters in s
    >>>> count_unique('aabb')
    2
    >>>> count_unique('abcdef')
    6
    '''
    seen_c = [] 
    for c in s: #O(n)
        if c not in seen_c: #O(n) as seen_c grows
            seen_c.append(c)

    return len(seen_c) #O(n^2)

def count_unique_2(s):
    seen_c = set()
    for c in s: #O(n)
        if c not in seen_c: #O(1) as sets use hash
            seen_c.add(c)
    return len(seen_c)

lst = [1,2,3,3,4]
len(set(lst))


########### Generators 

# Only evaluate values when you need them
g = (i for i in range(6))

next(g)
next(g)
next(g)

sum((i for i in range(10000)))

#as list grows large, it will consume lots of memory 
#generators will always take 128 bytes of memory
##any function can be a generator function with the word yield

def f():
    yield 1 
    yield 2
    yield 3

g = f()
next(g)
next(g)

next(f()) #will create a new generator each time

####### Dictionaries and defaultdict

