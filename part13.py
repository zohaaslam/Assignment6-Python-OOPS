# 13. Composition
# Assignment: 13 Composition
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

# Solve:

 
class Engine:
    def start(self):
        print("Engine has started.")

class Car:
    def __init__(self):
        self.engine = Engine()   #composition


    def start_car(self):
        self.engine.start() 


if __name__ == "__main__":
    my_Car = Car()
    my_Car.start_car()
