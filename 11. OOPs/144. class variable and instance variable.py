class Employee:
    company = "TechCorp" # Class variable

    def __init__(self, name):
        self.name = name # Instance variable

emp1 = Employee("John")
emp2 = Employee("Jane")
print(emp1.company, emp2.company) 