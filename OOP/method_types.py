#@classmethod vs @staticmethod vs "plain" method

#Instance Method:
#Can modify object instance state
#Can modify class state

#Class Method:
#Cannot modify object instance state
#Can modify class state

#Static Method:
#Cannot modify object instance state
#Cannot modify class state
import math 

class MyClass:
    def method(self):
        return 'instance method called', self 

    @classmethod 
    def classmethod(cls):
        return 'class method called', cls  

    @staticmethod
    def staticmethod():
        return 'static method called'

obj = MyClass()
print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())

#A better Pizza Interface with Class Methods
class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius 
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients})'

    @classmethod
    def margherita(cls):
        return cls(4.5, ['cheese', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(4.5, ['cheese', 'tomatoes', 'ham', 'mushrooms'])

    def area(self):
        return self._circle_area(self.radius)

    @staticmethod
    def _circle_area(r):
        return r**2 * math.pi


#print(Pizza(['cheese', 'tomatoes']))
#print(Pizza.margherita())
#print(Pizza.prosciutto())

#when to use staticmethods? It is very independent from everything else

print(Pizza(4.5, ['cheese']).area())
print(Pizza._circle_area(12))