# Classes and Objects in Python

# Class definition
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

# Creating an object
my_dog = Dog("Buddy", 3)

# Accessing object properties and methods
print("Dog's name:", my_dog.name)
print("Dog's age:", my_dog.age)
print(my_dog.bark())
