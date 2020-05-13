##Inside this file, define the decorators
import functools

def do_twice(func):
    @functools.wraps(func) #for documentation purpose
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper 

# from decorators import do_twice
@do_twice
def say_whee():
    print("Whee!")

@do_twice
def greet(name):
    print(f'Hello {name}')

say_whee()
greet('World')