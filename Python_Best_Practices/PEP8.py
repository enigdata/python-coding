#write beautiful Python codes

#Naming Conventions
def my_function():
    pass 

x = 2
my_variable = 'two'

#constant 
GRAVITY_ACCEL = 9.8 

class CoolCat:
    def meow():
        pass 

#module 
#my_module.py

#package 
#mypackage 

name = 'John Smith'
first_name, last_name = name.split()

def multiply_by_two(x):
    return x*2

#Code Layout 

class MyFirstClass():
    pass 


class MySecondClass():
    pass 


class MyThirdClass():
    def first_function():
        pass 

    def second_function():
        pass 

    def third_function():
        pass 

    def calculate_variance(number_list):
        sum_list = 0
        for number in number_list:
            sum_list = sum_list + number 
        mean = sum_list / len(number_list)

        sum_squares = 0
        for number in number_list:
            sum_squares = sum_squares + number**2 
        mean_squares = sum_squares / len(number_list)

        return mean_squares - mean**2 

# Max Line Length 

def function(arg_one, arg_two,\
            arg_three, arg_four):
    return arg_one

total = (first_variable
        + second_variable
        - third_variable)

#Indentation 
def function(arg_one, arg_two,
            arg_three, arg_four):
    return arg_one 

def function(
        arg_one, arg_two,
        arg_three, arg_four):
    return arg_four

if (x > 3 and 
        x < 10):
    print(x)

list_of_numbers = [
    1, 2, 3,
    4, 5, 6
    ]

#Be consistent!  

#Whitespace in Expressions and Statements 
def function(default_param=5):
    pass 

x = 5 
x += 1 

x == y 
z != y

x is None 
y not in lst 

True or False 

#Multiple Operators 
y = x**2 + 5 
z = (x+y) * (x-y)

if x>5 and x%2==0":
    print('something')

my_list[x+1 : x+2 : -1]

my_list = [1, 2, 3]

print(x, y)
my_tuple = (3,)

var1 = 5
var2 = 6
some_extra_long_var = 7

#Programming Recommendations
my_bool = 6>5
if my_bool:
    return '6 is greater than 5'

my_list = []
if not my_list:
    print('List is empty!')

if x is not None:
    return 'x is set to a value!'

def function(param=None):
    if param is not None:
        #do something 

if word.startswith('cat'):
    return 'starts with cat'

#Conclusions 
#flake8