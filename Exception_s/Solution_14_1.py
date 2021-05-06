#Write a program to generate Arithmetic Exception without exception handling...

class Maths:
    def operation(self,a):
        div = a / 0
        if div:
            raise ZeroDivisionError(f"{a} cannot be divisible by Zero.")
    
        

division = Maths()
division.operation(15) 
