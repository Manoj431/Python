# Handle the Arithmetic exception using try-catch block..

class Error:
    def operation(self,number):
        try:
            print(int(number))
        except ValueError:
            print("ValueError: Value must be an integer.")
        
e=Error()
e.operation("Manoj")
    