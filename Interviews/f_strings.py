age = 10 
name = "bob"
print(f"My name is {name}.  I am {age} years old.")

print(f"My name is {name}.  I am {age + 10} years old.")

class A(object):
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def __repr__(self):
        return (f"""
            My name is {self.name}.
            I am {self.age + 5} years old.
        """)