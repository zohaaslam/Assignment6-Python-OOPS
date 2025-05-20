# 9. Abstract Classes and Methods
# Assignment: 9 Abstract Classes and Methods
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

# Solve:

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self , length , width):
       self.length = length
       self.width = width


    def area(self):
        return self.length * self.width



rect = Rectangle(5,8)
print("Area of Rectangle:", rect.area())