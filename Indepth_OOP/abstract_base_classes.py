### Most of the abstract base classes that exist in the Python standard library live in the collections module 
from collections.abc import Container 
Container.__abstractmethods__

## silly container that tells us whether a given value is in the set of odd integers
class oddContainer:
    def __contains__(self, x):
        if not isinstance(x, int) or not x%2:
            return False
        return True 

odd_container = oddContainer()
isinstance(odd_container, Container) # this returns true 

1 in odd_container 
2 in odd_container

import abc 

class MediaLoader(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass 

    @abc.abstractproperty
    def ext(self):
        pass 

    @classmethod # the method can be called on a class instead of an instantiated object
    def __subclasshook__(cls, C): # Is the cals C a subclass of this class?
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True 
        return NotImplemented

    

    
