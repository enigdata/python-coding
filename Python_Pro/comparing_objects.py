###is compares identity, not equality
#Identity refers to the memory address at which an object is stored
#This is different from the variable name which points to an object
#Use is to compare with None
#The id() function is useful for inspecting and comparing these memory addresses

a = "This is a string"
b = "This is a string"

a == b # True 
a is b #False
id(a)
id(b)
#The IDs are different
x = 20
y = 20
x == y 
x is y # True why? because -5 to 256, each number has a distinct memory location

#### == and != operators
### == compares equality, which relies on the __eq__() method of objects
a = "This is a string"
b = "This is a string"
a == b #True

a = [1,2,3]
b = a.copy()
a == b #True

#imagine two boxes with same content

class SillyString(str):
    def __eq__(self, other):
        print("Comparing length")
        return len(self) == len(other)

    def __ne__(self, other):
        return not self.__eq__(other)

##Use == if you want to compare the contents of two objects
##Use 'is' to compare the memory addresses of objects, or to compare with None
