# # 7. Access Modifiers: Public, Private, and Protected
# # Assignment: 7. Access Modifiers: Public, Private, and Protected
# # Create a class Employee with:


# solve:



class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary   # use _salary instead of salary
        self.__ssn = ssn        # private

    def get_ssn(self):
        return self.__ssn

    def set_salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("Salary must be positive in number")

    def display(self):
        print(f"Name: {self.name}")            # public
        print(f"Salary: {self._salary}")       # protected
        print(f"SSN: {self.__ssn}")            # private


class Manager(Employee):
    def __init__(self, name, salary, sn, department):
        super().__init__(name, salary, sn)
        self.department = department

    def show_manager_info(self):
        print(f"Manager: {self.name}")  
        print(f"Department: {self.department}")
        print(f"Protected Salary: {self._salary}")  # protected variable
        print(f"Accessing SSN via getter: {self.get_ssn()}") 


# Test the classes
m = Manager("Alice", 80000, "123-45-6789", "HR")
m.show_manager_info()
m.set_salary(32000)
print("Updated salary:", m._salary)


print("Private SSN via getter:", m.get_ssn())
