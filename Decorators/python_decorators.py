#### Simple decorators
def my_decorator(func):
    def wrapper():
        print('something is happening before the function is called')
        func()
        print('something is happeing after the function is called')

    return wrapper

def say_whee():
    print('Whee!')

say_whee = my_decorator(say_whee)

say_whee()

#Another example
from datetime import datetime

#wrap around another function
def not_during_the_night(func):
    def wrapper():
        if 7<= datetime.now().hour < 22:
            func()
        else:
            pass #Hush, the neighbors are asleep

    return wrapper

say_whee()

say_whee = not_during_the_night(say_whee)

###snytax sugar

def my_decorator(func):
    def wrapper():
        print('before the function is called')
        func()
        print('after the function is called')

    return wrapper

@my_decorator
def say_whee():
    print('Whee!')

print('styling decorator----')
say_whee()
