def my_function(argument):
    """docstring"""
    my_var = argument*5
    return my_var

def add_one(number):
    """
    a function that adds one to the number given and returns it
    """
    return number + 1 

add_one_also = add_one

### Functions are first-class objects and can be passed in as arguments

def say_hello(name):
    return f"Hellow {name}"

def be_awesome(name):
    return f'Yo {name}, together we aer the awesomest!'

my_list = [say_hello, be_awesome]

my_list[0]('Thomas')

def greet_bob(greeter_func):
    return greeter_func('Bob')

greet_bob(say_hello)

greet_bob(be_awesome)

####Inner functions
def parent():
    print('Printing from the parent() function')

    def first():
        print('Printing from the first function')

    def second():
        print('Printing from the second function')

    second()
    first()

##### Returning functions from functions

def parent(num):
    def first_child():
        return 'Hi I am Emma'

    def second_child():
        return 'Call me Anna'

    if num == 1:
        return first_child

    else:
        return second_child

first = parent(1)
second = parent(2)

print(first())
print(second())
