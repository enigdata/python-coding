class Dog:

    #class attribute; default value of the class
    species = 'mammal'

    #Initializer
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def birthday(self):
        self.age += 1

    

philo = Dog('philo', 5)
mikey = Dog('mikey', 6)

#reset values 
mikey.age += 1
philo.species = "mouse"

print("{} is {} and {} is {}".format(philo.name, philo.age, mikey.name, mikey.age))

#if philo.species == "mammal":
#    print("{} is a {}".format(philo.name, philo.species))

#Test on the methods
print(mikey.description())
print(mikey.speak("Gruff! Gruff!"))

mikey.birthday()
print(mikey.description())