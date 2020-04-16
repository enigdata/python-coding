class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return 'Car({self.color}, {self.mileage})'.format(self = self)

    def __str__(self):
        return 'a {self.color} car'.format(self = self)


#__str__ vs __repr__
# __str__ easy to read, for human consumption
# __repr__ unambiguous
my_car = Car('red', 30000)
print(repr(my_car))
print(str(my_car))