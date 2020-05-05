class CapitalIterable:
    def __init__(self, string):
        self.string = string 

    def __iter__(self):
        return CapitalIterator(self.string)

class CapitalIterator:
    def __init__(self, string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0 

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()

        word = self.words[self.index]
        self.index += 1 
        return word 

#### List Comprehension
input_strings = ['1', '5', '234']
output_integers = [int(num) for num in input_strings]

output_2 = [int(num) for num in input_strings if len(num)<3]

from collections import namedtuple

Book = namedtuple('Book', "author title genre")
books = [
    Book("Pratchett", "Nightwatch", "fantasy"),
    Book("Pratchett", "Thief Of Time", "fantasy"),
    Book("Le Guin", "The Dispossessed", "scifi"),
    Book("Le Guin", "A Wizard Of Earthsea", "fantasy"),
    Book("Turner", "The Thief", "fantasy"),
    Book("Phillips", "Preston Diamond", "western"),
    Book("Phillips", "Twice Upon A Time", "scifi")
]

fantasy_authors = {b.author for b in books if b.genre=='fantasy'}

fantacy_titles = {b.title: b for b in books if b.genre == 'fantasy'}

#### The Iterator Pattern
import sys
inname, outname = sys.argv[1:3]

with open(inname) as infile:
    with open(outname, "w") as outfile:
        warnings_lines = (
            l.replace("\tWARNING", "") for l in infile if "WARNING" in l
        )
        for l in warnings_lines:
            outfile.write(l)

