#super() returns a delegate object to a parent class, so you call the method you want directly on it: super().method()


class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length

#Use dir() to examine the object
square = Square(3)
#print(dir(square))

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return self.length * self.width

    def what_am_i(self):
        return 'R'

rectangle = Rectangle(2,4)
print(rectangle.area())

## Square with Inheritance
class Square2(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def what_am_i(self):
        return 'S'

print(dir(Square2))
square = Square2(2)
print(square.area())
print(square.__class__.__base__) #this tells you the parent class


class Cube(Square2):

    #same parameters as Square, no need to redefine __init__

    def surface_area(self):
        face_area = self.area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

    def what_am_i(self):
        return 'C'

    def family_tree(self):
        # super() is a shortcut for super(Cube, self)
        return self.what_am_i() + " is child of " + super().what_am_i()

cube = Cube(3)
print(cube.what_am_i())

print(super(Cube, cube).what_am_i())
print(super(Square2, square).what_am_i())
print(cube.family_tree())

#Multiple Inheritance
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5*self.base*self.height 

    def what_am_i(self):
        return "Triangle"

#Mixins

class SurfaceAreaMixin:
    # the mixin does not need to understand what is the shape of the surface
    def surface_area(self):
        surface_area = 0
        for surface in self.surfaces: #define self.surfaces for different classes
            surface_area += surface.area(self)

        return surface_area

class RightPyramid(Triangle, Square2, SurfaceAreaMixin):
    def __init__(self, base, slant_height):
        self.base = base 
        self.slant_height = slant_height

        self.height = slant_height
        self.length = base 

        self.surfaces = [Square2, Triangle, Triangle, Triangle, Triangle]

    def what_am_i(self):
        return "RightPyramid"

rp = RightPyramid(2, 4)
print(super(RightPyramid, rp).what_am_i()) #print the first inheritance
print(rp.__class__.__bases__)
print(RightPyramid.__mro__) # method resolution order

# #Mixins

# class SurfaceAreaMixin:
#     # the mixin does not need to understand what is the shape of the surface
#     def surface_area(self):
#         surface_area = 0
#         for surface in self.surfaces: #define self.surfaces for different classes
#             surface_area += surface.area(self)

#         return surface_area

class Cube2(Square2, SurfaceAreaMixin):
    def __init__(self, length):
        super().__init__(length)
        self.surfaces = [Square2] * 6

another_cube = Cube2(4)
print(another_cube.surface_area())


