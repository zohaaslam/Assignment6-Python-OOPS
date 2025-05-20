# 10. Instance Methods
# Assignment: 10 Instance Methods
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

# Solve:

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof Woof!") 


dog1 = Dog("Buddy", "Aidi")
dog1.bark()
        
