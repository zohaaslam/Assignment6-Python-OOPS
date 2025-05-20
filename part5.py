# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.


# Solve:

class MathUtils:
    @staticmethod
    def add(a,b):
        return a + b 
    
result = MathUtils.add(10,5)  
print(f"The sum is: {result}")  # Output: The sum is: 15  