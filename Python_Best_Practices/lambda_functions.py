def myfunc(x, y, z):
    res = x + y + z
    return res 

lambda x, y, z: x + y + z

lambda x, y, z: x**2 + y + (z%2)

lambda x: x%2 == 0

#intended for single use
#defined in a single line
#named or anonymous 
#none or more inputs

#comparison
def second(x):
    return x[1]

a = [(1, 2), (2, 5), (3, 1), (4, 15)]
a.sort(key = second)

a.sort(key=lambda x:x[1])

#squaring a number 
squared = lambda x: x**2
squared(5)

add = lambda x, y: x + y 
add(3, 5)

mult = lambda x, y, z: x*y*z
mult(3, 5, 7)

#SORT 
#lambda functions allow key to become much more versatile 
names = ['Alf Zed', 'Mike Mo', 'Steve Aardark']
names.sort(key = lambda x: x.split()[-1].lower())
print(names)

people = [('Steve', 23), ('Karen', 45), ('Gerald', 32), ('Jo', 75)]
people.sort(key = lambda x: x[1])

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def __repr__(self):
        return f'{self.name}:{self.age}'
    
alex = Person('alex', 17)
mabel = Person('mabel', 13)
addy = Person('addy', 25)

p = [alex, mabel, addy]

p.sort(key = lambda x: x.age)
p.sort(key = lambda x: x.name)

#FILTER
nums = [1, 2, 3, 4]
even = list(filter(lambda x: x%2==0, nums))

nums = list(range(1, 21)) 
odd = list(filter(lambda x: x%2 != 0, nums))

from statistics import mean 
data = list(range(1, 12))

avg = mean(data)
above_avg = list(filter(lambda x: x > avg, data))

nicknames = ['Diafasdf', 'Braves', 'Brockis', 'asdfaweawf', 'few', 'weafat']
short_names = list(filter(lambda x: len(x) < 6, nicknames))

#MAP
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))

nums = list(range(1, 11))
even_bool = list(map(lambda x: x%2 == 0, nums))

#Reduce 
from functools import reduce 
nums = [1, 2, 3, 4]
total = reduce(lambda x, y: x+y, nums)
print(total)

names = ['dan', 'darren', 'joanna', 'jackie', 'chris']
conc = reduce(lambda x, y: x + y[:2], names, '')

#Test lambda functions
#open a test.py
import unittest 

squared = lambda x: x**2

class LambdaTest(unittest.TestCase): 
    def test_squared(self):
        self.assertEqual(squared(2), 4)

    def test_zero(self):
        self.assertEqual(squared(0), 0)

    def test_negative(self):
        self.assertEqual(squared(-2), 4)

if __name__ = '__main__':
    unittest.main()

    




