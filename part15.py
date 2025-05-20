# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.


# Answer:

class A:
    def show(self):
        print("Show from A")

class B(A):
    def show(self):
        print("Show from B") 

class C(A):
    def show(self):
        print("Show from C")



class D(B, C):
    pass 

obj = D()
obj.show()