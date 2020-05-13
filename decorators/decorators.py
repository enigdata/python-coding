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

# say_whee()
# greet('World')

###Template
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorators(*args, **kwargs):
        #do something before
        value = func(*args, **kwargs)
        #do something after
        return value 
    return wrapper_decorators

##### Timing functions
import time 

def timer(func):
    '''
    Print the runtime of the decorated function
    '''
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        #do something before
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        run_time = end - start
        print(f"Finished {func.__name__!r} in {run_time: .4f} secs")
        #do something after
        return value 
    return wrapper_timer 

####### Debugging Code 
def debug(func):
    '''
    Print the function signature and return value
    '''
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        #do something before
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k} = {v!r}" for k, v in kwargs.items()]
        signature = ",".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        #do something after
        print(f"{func.__name__!r} returned {value!r}")
        return value 
    return wrapper_debug

##### Slowing code down
def slow_down(func):
    '''
    Sleep 1 second before calling the function
    '''
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        #do something before
        time.sleep(1)
        value = func(*args, **kwargs)
        #do something after
        return value 
    return wrapper_slow_down 

###### Registering Plugins

import random 

PLUGINS = dict()
def register(func):
    '''
    Register a function as a plug-in
    '''
    PLUGINS[func.__name__] = func 
    return func 
    