# Employee salary manager
#add method to increase salary by a percentage

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)
        return self.salary

# Example
emp1 = Employee("Sarah", 50000)
print(emp1.increase_salary(10))  # Output: 55000
