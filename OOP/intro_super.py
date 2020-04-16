class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length

#Use dir() to examine the object
square = Square(3)
print(dir(square))

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return self.length * self.width

rectangle = Rectangle(2,4)
print(rectangle.area())

## Square with Inheritance
class Square2(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

print(dir(Square2))


