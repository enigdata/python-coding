def my_sum(a,b):
    return a+b

#my_sum(a, b)

def my_sum2(integers):
    res = 0 
    for x in integers:
        res += x 
    return res 

ints = [1,2,3]
print(my_sum2(ints))

def my_sum3(*args):
    res = 0 
    #Iterating over the Python args tuple
    for x in args:
        res += x 
    return res 

print(my_sum3)

def concatenate(**kwargs):
    res = ""
    for arg in kwargs.values():
        res += arg 

    return res 

print(concatenate(a="real", b='Python', c="Is", d='Great', e='!'))

#order matters
def my_function(a,b, *args, **kwargs):
    pass 


#unpacking args 
list1 = [1,2,3]
list2 = [4,5]
list3 = [6,7,8,9]

print(my_sum3(*list1, *list2, *list3))

my_list = [1,2,3,4,5,6]
a, *b, c = my_list
print(a)
print(b)
print(c)

#a is 1 
#b is [2,3,4,5]
#c is 6

list_1 = [1,2,3]
list_2 = [4,5,6]
merged_list = [*list_1, *list_2]

dict1 = {'A': 1, "B": 2}
dict2 = {"C": 3, "D": 4}

merged_dict = {**dict1, **dict2}

a = [*"RealPython"] # a will become a list of characters

#readability count 

