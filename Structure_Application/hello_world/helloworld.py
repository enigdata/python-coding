#! /usr/bin/env python
# helloworld.py
__version__ = '0.1.0'

import re 
import requests
from utils import show_message

URL = "https://en.wikipedia.org/wiki/%22Hello,_World!%22_program"

def do_hello():
    res = requests.get(URL)
    show_message(re.findall('<title>(.*?)</title>', res.text)[0])

if __name__ == '__main__':
    do_hello()