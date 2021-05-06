from abc import ABC, abstractmethod

class Company(ABC):                 #Abstract Class
    @abstractmethod
    def company_name(self):         #Abstract Method
        pass

    def employee(self,name):
        print(f"The name of employee is {name} ")   

class Employee(Company):
    def company_name(self,name):
        print(f"The company name is {name} ")
    
    def emp(self,name):
        super().employee(name)

e = Employee()
e.company_name("JALA")
e.emp("Manoj")
e.employee("Rahul")
