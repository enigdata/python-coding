### Abstraction if like an onion 

# Small, focused behaviors that get used again and again sit in the lower layers and need
# to change infrequently. The big concepts, business logic, and complex moving parts
# show up as you go further out; they change more frequently because of changing
# requirements, but they still make use of the smaller behaviors.

# In Python, modules are also a form of encapsulation. Modules are even higher-level
# than classes; they group multiple related classes and functions together. For example,
# a module dealing with HTTP interactions could contain classes for requests and
# responses, as well as utility functions for parsing URLs. Most *.py files you encounter
# would be considered modules.

# The largest encapsulation available
# in Python is a package. Packages encapsulate
# related modules into a directory
# structure. Packages are often distributed
# on the Python Package Index
# (PyPI) for others to install and reuse.

# Encapsulation encourages you to
# reduce the responsibilities of any given portion of
# code, helping you avoid complicated dependencies.

# Python has no true support for private methods or data. Instead, it follows a philosophy
# of trusting developers to do the right thing. A common convention does help in
# this arena, though. Methods and variables intended for use within a class but not from
# outside the class are often prefixed with an underscore. This provides a hint to future
# developers that a particular method or variable isn’t intended as part of the public
# interface of the class. Third-party packages often state loudly in their documentation
# that such methods are likely to change from version to version and should not be
# explicitly relied on.

from datetime import datetime

#class with somewhat unrelated methods
class Greeter:
    def __init__(self, name):
        self.name = name 

    def _day(self):
        return datetime.now().strftime('%A')

    def _part_of_day(self):
        current_hour = datetime.now().hour

        if current_hour < 12:
            part_of_day = 'morning'
        elif 12 <= current_hour <17:
            part_of_day = 'afternoon'
        else:
            part_of_day = 'evening'

        return part_of_day

    def greet(self, store):
        print(f'Hi, my name is {self.name}, and welcome to {store}!')
        print(f'How\'s your {self._day()} {self._part_of_day()} going?')
        print('Here\'s a coupon for 20% off!')

# Methods extracted as functions outside of the class 
def day():
    return datetime.now().strftime('%A')

def part_of_day():
    current_hour = datetime.now().hour

    if current_hour < 12:
        part_of_day = 'morning'
    elif 12 <= current_hour < 17:
        part_of_day = 'afternoon'
    else:
        part_of_day = 'evening'

    return part_of_day

#Referencing extracted functions inside the class
class Greeter:
    def __init__(self, name):
        self.name = name 

    def greet(self, store):
        print(f'Hi, my name is {self.name}, and welcome to {store}!')
        print(f'How\'s your {day()} {part_of_day()} going?')
        print('Here\'s a coupon for 20% off!')

### Functional programming
from functools import reduce

squares = map(lambda x: x*x, [1,2,3,4,5])
should = reduce(lambda x, y: x and y, [True, True, False])
evens = filter(lambda x: x%2 == 0, [1,2,3,4,5])

#The preference in Python would be the following
squares = [x*x for x in [1,2,3,4,5]]
should = all([True, True, False])
evens = [x for x in [1,2,3,4,5] if x%2 == 0]

from functools import partial 

def pow(x, power=1):
    return x**power 

square = partial(pow, power=2)
cube = partial(pow, power=3)

