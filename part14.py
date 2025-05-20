# 14. Aggregation
# Assignment: 14 Aggregation
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

# Solve:  

class Employee:
    def __init__(self, name):
        self.name = name


class Department:
    def __init__(self , employee):
        self.employee = employee


    def show_employee(self):
        print(f"Employee in department: {self.employee.name}")  



if __name__ == "__main__":
    emp = Employee("Zoha")
    dept = Department(emp)
    dept.show_employee()



del dept 
print(emp)

