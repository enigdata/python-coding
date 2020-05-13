import math
from decorators import *

@timer 
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

@debug
def make_greeting(name, age = None):
    if age is None:
        return f"Howdy {name}!"

    else:
        return f"Howdy {name} {age}!"

math.factorial = debug(math.factorial)

def approximate_e(terms = 18):
    return sum(1/math.factorial(n) for n in range(terms))

@slow_down 
def count_down(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        count_down(from_number - 1)

@register
def say_hello(name):
    return f'Hello {name}'

@register
def be_awesome(name):
    return f'Hello {name} we are awesome!'

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)

if __name__ == '__main__':
    waste_some_time(2)       
    make_greeting('Ben', 25)
    approximate_e(5)
    count_down(5)
    randomly_greet('Alice!')
