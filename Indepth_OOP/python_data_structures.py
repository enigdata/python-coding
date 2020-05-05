### Names Tuples
from collections import namedtuple

Stock = namedtuple('Stock', ['symbol', 'current', 'high', 'low'])
stock = Stock('FB', 177.46, high = 178.67, low = 175.79)

#stock.high 
#symbol, current, high, low = stock
# print(current)

from dataclasses import make_dataclass

Stock = make_dataclass("Stock", "symbol", "current", "high", "low")
stock = Stock("FB", 177.46, high=178.67, low=175.79)

#The benefit is that with make_dataclass you get to define the class in one line instead of six

#Another way of writing
@dataclass 
class StockDefaults:
    name: str 
    current: float = 0.0 
    high: float = 0.0 
    low: float = 0.0 

stocks = {
    'GOOG': (1235.0, 1242.54, 1231.06),
    'MSFT': (110.41, 110.45, 109.84)
}

stocks.get('RIM') # This returns None 
stocks.get("RIM", 'Not Found') # This returns 'Not Found'

stocks.setdefault('BBRY', (10.87, 10.76, 10.90))

##### Using default dictionary
def letter_frequency(sentence):
    frequencies = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1 
    return frequencies 

from collections import defaultdict
def letter_frequency(sentence):
    frequencies = defaultdict(int) # return 0 if key not found
    for letter in sentence:
        frequencies[letter] += 1 
    return frequencies

num_items = 0 

def tuple_counter():
    global num_items
    num_items += 1 
    return (num_items, [])

d = defaultdict(tuple_counter)

d['a'][1].append("hello")
d['b'][1].append("world")

##### Lists 

import string 
chars = list(string.ascii_letters) + [" "]

def letter_frequency(sentence):
    frequencies = [(c, 0) for c in chars]
    for letter in sentence:
        index = chars.index(letter)
        frequencies[index] = (letter, frequencies[index][1]+1)
    return frequencies

### Frequently used list methods
l = [1, 2, 3, 4]
l.append(5)
l.insert(2, 2.5)
l.count(4)
l.index(1)
l.find(4)
l.find(6) # returns -1
l.reverse()
l.sort() 

##### More on Sort 
class WeirdSortee:
    def __init__(self, string, number, sort_num):
        self.string = string 
        self.number = number 
        self.sort_num = sort_num

    def __lt__(self, object):
        if self.sort_num:
            return self.sort_num < object.sort_num 
        return self.string < object.string 

    def __eq__(self, object):
        return all(
            self.string == object.string 
            self.number = object.number 
            self.sort_num = object.sort_num
        )

    def __repr__(self):
        return f"{self.string}: {self.number}"
    
from operator import itemgetter
l =  [('h', 4), ('n', 6), ('o', 5), ('p', 1), ('t', 3), ('y', 2)]
l.sort(key = itemgetter(1))
l #Sorted by numbers 

#### Sets 
song_library = [
    ("Phantom Of The Opera", "Sarah Brightman"),
    ("Knocking On Heaven's Door", "Guns N' Roses"),
    ("Captain Nemo", "Sarah Brightman"),
    ("Patterns In The Ivy", "Opeth"),
    ("November Rain", "Guns N' Roses"),
    ("Beautiful", "Sarah Brightman"),
    ("Mal's Song", "Vixy and Tony"),
]

artists = set()
for song, artist in song_library:
    artists.add(artist)

    
