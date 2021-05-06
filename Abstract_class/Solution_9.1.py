#Python by default do not abstract classes. But we have an abc(Abstract Base Classes) module to achieve abstrct class.
from abc import ABC, abstractmethod

class Company(ABC):                 #Abstract Class
    @abstractmethod
    def company_name(self):         #Abstract Method
        pass

    def employee(name):
        print(f"The name of employee is {name} ")   


#We cannot create object for abstract class...
# We can call the abstract methods in the child class whose object can be created..    