# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

# Solve:

class Counter:
    counter = 0
    def __init__ (self):
        Counter.counter += 1
       
    @classmethod
    def display_counter(cls):
        print(f"Number of objects created: {cls.counter}")   



obj1= Counter()
obj2= Counter()
obj3= Counter()
obj4= Counter()
obj5= Counter()
obj6= Counter()
    




Counter.display_counter()