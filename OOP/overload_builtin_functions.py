#len()
class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __len__(self):
        return len(self.cart)

    def __bool__(self):
        return len(self.cart) > 0

    #"+"
    def __add__(self, other):
        new_cart = self.cart.copy()
        new_cart.append(other)
        return Order(new_cart, self.customer)

    #"+="
    def __iadd__(self, other):
        self.cart.append(other)
        return self

    # indexing and slicing with []
    def __getitem__(self, key):
        return self.cart[key]

    # reverse operators
    def __radd__(self, other):
        new_cart = self.cart.copy()
        new_cart.insert(0, other)
        return Order(new_cart, self.customer)

order = Order(['banana', 'apple', 'orange'], 'Cheng')
print(len(order))
print(bool(order))

order += "grape"
print(order.cart)
print(order[-1])

order = "grapefruit" + order 
print(order.cart)

order2 = Order([], 'Python')

for order in [order, order2]:
    if order:
        print(f"{order.customer}'s order is processing..." )
    else:
        print(f"Empty order for customer {order.customer}")

print((order + "grapes").customer)
order = order + 'mango'
print(order.cart)

#abs()
class Vector:
    def __init__(self, x_comp, y_comp):
        self.x_comp = x_comp 
        self.y_comp = y_comp

    def __abs__(self):
        return (self.x_comp ** 2 + self.y_comp ** 2) ** 0.5

vector = Vector(3,4)
print(abs(vector))

#str()
class Vector2:
    def __init__(self, x_comp, y_comp):
        self.x_comp = x_comp
        self.y_comp = y_comp

    def __str__(self):
        return f'{self.x_comp}i{self.y_comp:+}j'

    def __repr__(self):
        return f'Vector({self.x_comp}, {self.y_comp})'


v = Vector2(3, 4)
print(str(v))
print(repr(v))


#### A Complete Example
from math import hypot, atan, sin, cos 

class CustomComplex:
    def __init__(self, real, imag):
        self.real = real 
        self.imag = imag 

    def __repr__(self):
        return f"{self.__class__.__name__}({self.real}, {self.imag})"

    def __str__(self):
        return f"({self.real}{self.imag:+}j)"

    def __add__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            real_part = self.real + other 
            imag_part = self.imag

        if isinstance(other, CustomComplex):
            real_part = self.real + other.real 
            imag_part = self.imag + other.imag

        return self.__class__(real_part, imag_part)

    def __sub__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            real_part = self.real - other 
            imag_part = self.imag 

        if isinstance(other, CustomComplex):
            real_part = self.real - other.real 
            imag_part = self.imag - other.imag

        return self.__class__(real_part, imag_part)

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            real_part = self.real * other 
            imag_part = self.imag * other  

        if isinstance(other, CustomComplex):
            real_part = (self.real * other.real) - (self.imag * other.imag)
            imag_part = (self.real * other.imag) + (self.imag * other.real)

        return self.__class__(real_part, imag_part)

    def __radd__(self, other):
        return self.__add__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rsub__(self, other):
        #x - y != y - x 
        if isinstance(other, float) or isinstance(other, int):
            real_part = other - self.real 
            imag_part = -self.imag

        return self.__class__(real_part, imag_part)

    def __eq__(self, other):
        return (self.real == other.real) and (self.imag == other.imag)

    def __ne__(self, other):
        return (self.real != other.real) or (self.imag != other.imag)
   


