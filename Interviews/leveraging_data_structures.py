########## Set
def count_unique(s):
    '''
    Count number of unique characters in s
    >>> count_unique('aabb')
    2
    >>> count_unique('abcdef')
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

student_grades = {
    'Jack': [85, 90],
    'Jill': [80, 70]
}

def get_grades_naive(name):
    if name in student_grades:
        return student_grades[name]
    return []

def get_grades_better(name):
    return student_grades.get(name)

def get_grades_with_assignment(name):
    if name not in student_grades:
        student_grades[name] = []
    return student_grades[name]

def get_grades_with_assignment_better(name):
    return student_grades.setdefault(name, [])


def set_grade_naive(name, score):
    if name in student_grades:
        grades = student_grades[name]
    else:
        student_grades[name] = []
        grades = student_grades[name]
    grades.append(score)

def set_grade_better(name, score):
    grades = student_grades.setdefault(name, [])
    grades.append(score)

from collections import defaultdict

#student_grades = defaultdict(list)
student_grades = defaultdict(list, student_grades)

def set_grade_best(name, score):
    student_grades[name].append(score)


student_score = defaultdict(lambda: 70)
student_score['Jack'] + 10 #will return 80

student_score["Jack"] += 10

######## More on the collections module
def top_three_letter(string):
    '''
    >>> top_three_letters('abbccc')
    [('c', 3), ('b', 2), ('a', 1)]
    '''
    counter = defaultdict(int)
    for c in string:
        counter[c] += 1 
    top_three = sorted(counter, 
                    key = lambda k: counter[k], 
                    reverse=True
                    )[:3]
    res = []
    for letter in top_three:
        res.append((letter, counter[letter]))
    return res 


from collections import Counter

Counter(string).most_common(3)

#### deque

class TicketQueue(object):

    def __init__(self):
        self.lst = list()

    def add_person(self, name):
        """
        >>> queue = TicketQueue()
        >>> queue.add_person("Jack")
        Jack has been added to the queue
        """
        self.lst.append(name)
        print(f"{name} has been added to the queue")

    def service_person(self):
        '''
        >>> queue.service_person()
        The first person in the queue has been serviced
        '''
        name = self.lst.pop(0)
        print(f"{name} has been serviced")

    def bypass_queue(self, name): #O(n)
        self.lst.insert(0, name)
        print(f"{name} has bypassed the queue")

from collections import deque
class TicketQueue(object):

    def __init__(self):
        self.deque = deque()

    def add_person(self, name):
        """
        >>> queue = TicketQueue()
        >>> queue.add_person("Jack")
        Jack has been added to the queue
        """
        self.deque.append(name)
        print(f"{name} has been added to the queue")

    def service_person(self):
        '''
        >>> queue.service_person()
        The first person in the queue has been serviced
        '''
        name = self.deque.popleft()
        print(f"{name} has been serviced")

    def bypass_queue(self, name): #O(n)
        self.deque.appendleft(name)
        print(f"{name} has bypassed the queue")
    
###### namedtuple

## namedtuple is immutable
from collections import  namedtuple
Car = namedtuple("Car", "color make model milleage")

Car = namedtuple("Car", ["color", "make", "model", "mileage"])

my_car = Car("silver", "Tesla", "Model Y", 5)

my_car.color 
my_car.model

## You cannot mutate the attributes




