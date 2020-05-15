s = "computers are useless.  They can only give you answers."
a = [100, 200, 300]

def printy(arg):
    print(f'arg = {arg}')

class Classy:
    pass 

# import sys 
# sys.path 
# sys.path.append(r'/Users/siliwang/github_local/python-coding/Python_Pro/ModulesAndPackages')
# only available in the current session 

# mod.__file__ tell you the location of the module 

##### The import statement
#from mod import s, printy
#avoid name conflicts with local variables
### The dir() function
# When given the name of a module as an argument, dir() lists the names defined in the module

if __name__ == '__main__':
    print(s)
    print(a)
    printy('Good Day Sir!')
    x = Classy()
    print(x)

####reload
# import importlib
# importlib.reload(mod)

 