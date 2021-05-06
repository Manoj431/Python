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

    @abstractmethod
    def emp_id(self):
        pass

class Details(Employee):
    def emp_id(self):
        print(f"The employee id is 105")

    def emp_car(self,model):
        print(f"The employee has {model} car. ")

    
d = Details()
d.emp_id()                                  #calling Abstract method class of Employee in Details child class
d.company_name("JALA TECH")                 #calling Abstract method of Company in Employee child class 
                                            #through Details child class object.

