# Write a program to create your own exception.....

class RangeError(Exception):
    def __init__(self,message):
        super().__init__(message)
      
class Employee:
    def __init__(self,amount):
        self.salary=amount

    def display(self):
        if self.salary < 21000:
            raise RangeError("The salary is not desirable.")
        else:
            print("The salary is OK.")

sal = Employee(20000)
sal.display()
