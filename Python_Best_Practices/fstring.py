#f-strings: a new and improved way to format strings 
name = "Eric"
age = 74
f"Hello, {name}, you are {age}"

f"{2 * 37}" #the result is a string 

f"{name * 5}"

def to_lowercase(input):
    return input.lower() 

name = "Eric Idle"
f"{to_lowercase(name)} is funny."

f"{name.upper()} is funny."

class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name 
        self.age = age 

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}"

    def __repr__(self):
        retrn f"Comedian({self.first_name}, {self.last_name}, {self.age})"

new_comedian = Comedian("Eric", "Idle", "74")
print(f"{new_comedian}")
print(new_comedian)

#multiline fstring
name = "Eric"
profession = "comedian"
affiliation = "Monty Python"

message = (
    f"Hi {name}."
    f"You are a {profession}"
    f"You were in {affiliation}."
    )

#f string is faster than old-school string formatting

f"The \" comedian \" is {name}, {age}"""

comedian = {"name": "Eric", "age": 76}
f"the comedian is {comedian['name']}, age {comedian['age']}."

#the following will throw an error:
# f'the comedian is {comedian['name]}, age {comedian['age']}'

f "{{74}}" # this will print out {74}


