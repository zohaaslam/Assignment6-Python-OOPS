



# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

# Solve





class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Object banao
m = Multiplier(5)

# Check if object is callable
print("Is m callable?", callable(m))  # Output: True

# Object ko function ki tarah call karo
result = m(10)  # 10 * 5 = 50
print("Result of m(10):", result)
