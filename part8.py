# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

# Solve:

class Person:
    def __init__(self , name):
        self.name = name
        print(f"Person created with the name: {self.name}")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        print(f"Teacher teaches: {self.subject}")


t = Teacher("Sir Asharib Ali And Sir Hamza" , "GIAIC Python Course ")

        