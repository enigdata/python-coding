### Commonly used methods
s = 'hello world'
s.count('l')
s.find('l')
s.split(' ')
s.replace(' ', '*')
s.partition(' ')

### string formating
name = 'Dusty'
activity = 'writing'
formatted_string = f"Hello {name}, you are currently {activity}."

## Escaping braces
##{{ }}
classname = "MyClass"
python_code = "print('hello world')"
template = f"""
public class {classname} {{
    public static void main(String[] args) {{
        System.out.println("{python_code}");
    }}
}}
"""

#### f strings can contain python code

#### Making it look right
##Technically, we should never use floating-point numbers in currency calculations like this; 
# we should construct decimal.Decimal() objects instead. 
# Floats are dangerous because their calculations are inherently inaccurate beyond a specific level of precision. 
# But we're looking at strings, not floats, and currency is a great example for formatting!

subtotal = 12.32
tax = subtotal * 0.07 
total = subtotal + tax 

print(
    'Sub: ${0:0.2f} Tax: ${1:0.2f}' 
    'Total: ${total: 0.2f}'.format(subtotal, tax, total = total)
)

### Strings are unicode
chars = 'cliche'
print(chars.encode('UTF-8'))
print(chars.encode('latin-1'))
print(chars.encode('CP437'))
print(chars.encode('ascii'))

###Regex
import re 
search_string = 'hello world'
pattern = 'hello world'

match = re.match(pattern, search_string)
if match:
    print("regex mathces")

import sys 
import re 

pattern = sys.argv[1]
search_string = sys.argv[2]

match = re.match(pattern, search_string)

## Check documentation for more details


### Pickle 
from threading import Timer 
import datetime
from urllib.request import urlopen

class UpdatedURL:
    def __init__(self, url):
        self.url = url 
        self.contents = ''
        self.last_updated = None 
        self.update()

    def update(self):
        self.contents = urlopen(self.url).read()
        self.last_updated = datetime.datetime.now()
        self.schedule()

    def schedule(self):
        self.timer = Timer(3600, self.update)
        self.timer.setDaemon(True)
        self.timer.start()

    # for pickle to work
    def __getstate__(self):
        new_state = self.__dict__.copy()
        if 'timer' in new_state:
            del new_state['timer']
        return new_state 

    # to customize unpickling
    def __setstate__(self, data):
        self.__dict__ = data
        self.schedule()

### JSON
import json 

class Contact:
    def __init__(self, first, last):
        self.first = first
        self.last = last 

    @property
    def full_name(self):
        return ("{} {}".format(self.first, self.last))

c = Contact('John', 'Smith')
json.dumps(c.__dict__)


