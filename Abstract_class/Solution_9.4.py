from abc import ABC, abstractmethod

class Company(ABC):                 #Abstract Class
    @abstractmethod
    def company_name(self):         #Abstract Method
        pass

    def employee(self,name):
        return name   

class Employee(Company):
    def company_name(self,name):
        print(f"The company name is {name} ")
    
    def emp(self,name1):
        super().employee(name1)
        return name1

    @abstractmethod
    def emp_id(self):
        pass

class Details(Employee):
    def emp_id(self):
        print(f"The employee id is 105")

    def emp_car(self,model):
        print(f"The {Employee.emp} has {model} car. ")

    
d = Details()
d.emp("Manoj")
d.emp_car("Maserati")
                                



