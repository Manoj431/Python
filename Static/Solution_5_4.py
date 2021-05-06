# Call instance methods in static method

class Methods:
    
    def display_name(name_1):                                   #Instance method
        print(f"The name of company is {name_1}")


    @staticmethod
    def company_name(name):                                       #Static method
        
        Methods.display_name(name)

m = Methods()
m.company_name("IBM")