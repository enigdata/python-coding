#! /usr/bin/env python
# helloworld.py
__version__ = '0.1.0'

import re 
import requests

URL = "https://en.wikipedia.org/wiki/%22Hello,_World!%22_program"

def do_hello():
    res = requests.get(URL)
    print(re.findall('<title>(.*?)</title>', res.text)[0])

if __name__ == '__main__':
    do_hello()