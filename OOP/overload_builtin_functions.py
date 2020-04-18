#len()
class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __len__(self):
        return len(self.cart)

    def __bool__(self):
        return len(self.cart) > 0

order = Order(['banana', 'apple', 'orange'], 'Cheng')
print(len(order))
print(bool(order))

order2 = Order([], 'Python')

for order in [order, order2]:
    if order:
        print(f"{order.customer}'s order is processing..." )
    else:
        print(f"Empty order for customer {order.customer}")

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
