python -m this #The Zen of Python 

#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#bad practice
if value == True:
    print('true')

if value2 == None:
    print(None)

#good practice
if value:
    print('true')

if not value:
    print('false')

if value2 is None:
    print(None)

#concat strings 
words = ['cat', 'dog', 'horse', 'human']
' '.join(words)

#swapping variables in place
a, b = b, a 

#dictionaries
dict_ = {'Maddi': 5, "Lion": 6}

his_apples = dict_.get('Maddi', 0)
her_apples = dict_.get('Jimmy', 0)

