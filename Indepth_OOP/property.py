class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name 

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name 

    def _get_name(self):
        return self._name 

    name = property(_set_name, _get_name)

## Decorators - another way to create properties
class Foo:
    @property
    def foo(self):
        return 'bar'

from urllib.request import urlopen

class WebPage:
    def __init__(self, url):
        self.url = url 
        self._content = None 

    @property
    def content(self):
        if not self._content:
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
        return self._content

class AverageList(list):
    @property
    def average(self):
        return sum(self)/len(self)

#a = AverageList([1,2,3,4])
# a.average 

   