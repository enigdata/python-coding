### Reversed 
normal_list = [1,2,3,4,5]

class CustomSequence:
    def __len__(self):
        return 5 

    def __getitem__(self, index):
        return f"x{index}"

class FunkyBackwards:
    def __reversed__(self):
        return "Backwards!"

#### Enumerate 
import sys 
filename = sys.argv[1]

with open(filename) as file:
    for index, line in enumerate(file):
        print(f"{index+1}: {line}", end="")

#### File I/O
contents = "Some file contents"
file = open("filename", "w")
file.write(contents)
file.close()

###### Method Overloading

def no_args():
    pass 

def mandatory_args(x, y, z):
    pass 

def default_arguments(x, y, z, a = 'Some string', b = False):
    pass 

def kw_only(x, y='defaultkw', *, a, b='only'):
    pass 

## Don't do this
def hello(b=[]):
    b.append('a')
    print(b)

hello() #returns ['a']
hello() #returns ['a', 'a']

#instead:
def hello(b = None):
    if b:
        b.append('a')
    else:
        b = []
        b.append('a')

#### variable argument lists
def get_pages(*links):
    for link in links:
        print(link)

### kwargs
class Options:
    default_options = { 
            'port': 21, 
            'host': 'localhost', 
            'username': None, 
            'password': None, 
            'debug': False, 
            } 
    def __init__(self, **kwargs):
        self.options = dict(Options.default_options)
        self.options.update(kwargs)

    def __getitem__(self, key):
        return self.options[key]

#### unpacking arguments 

def show_args(arg1, agr2, agr3 = "Three"):
    print(arg1, agr2, agr3)

some_args = range(3)
more_args = {
    'arg1': 'ONE',
    'arg2': 'TWO'
}
show_args(*some_args) #use * to unpack a list
show_args(**more_args) # use ** to unpack a dict


#### Succinct way for class Options
class Options:
    default_options = { 
            'port': 21, 
            'host': 'localhost', 
            'username': None, 
            'password': None, 
            'debug': False, 
            }

    def __init__(self, **kwargs):
        self.options = {**Options.default_options, **kwargs}

x = {'a': 1, 'b': 2}
y = {'b': 11, 'c': 3}

z = {**x, **y}

#z will return {'a': 1, 'b': 11, 'c': 3}


#### Functions are objects
import datetime
import time 

class TimedEvent:
    def __init__(self, endtime, callback):
        self.endtime = endtime
        self.callback = callback

    def ready(self):
        return self.endtime <= datetime.datetime.now() 

class Timer:
    def __init__(self):
        self.events = []

    def call_after(self, delay, callback):
        end_time = datetime.datetime.now() + datetime.timedelta(seconds = delay)
        self.events.append(TimedEvent(end_time, callback))

    def run(self):
        while True:
            ready_events = (e for e in self.events if e.ready())
            for e in ready_events:
                event.callback(self)
                self.events.remove(event)
            time.sleep(0.5)

##### Using functions as attributes 

class A:
    def print(self):
        print("my class is A")

    def fake_print():
        print("my class is not A")

a = A()
a.print()
a.print = fake_print #set the print method to point at a new function
a.print()



