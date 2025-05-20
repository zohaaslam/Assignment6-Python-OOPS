# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

# Solve:


def add_greeting(cls):
    def greet(self):
        return "Hello from Decoator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__ (self , name):
        self.name = name


p = Person("Zoha")   
print(p.greet())


