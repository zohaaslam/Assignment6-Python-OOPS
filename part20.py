# # 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except. 

# Solve:

class InvalidageError(Exception):
    def __init__(self , message="Age must be 18 or older."):
        self.message = message
        super().__init__(self.message)


def check_age(age):
    if age < 18:
        raise InvalidageError() 
    else:
        print("Access granted! You are eligible.")   


try:
    user_agge = int(input("Enter your age:"))
    check_age(user_agge)
except InvalidageError as e:
    print("Custom Exception Caught:", e) 
except ValueError:
    print("please enter a valid number!")       

    