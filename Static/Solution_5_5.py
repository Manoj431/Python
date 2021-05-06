#Call static methods in instance methods...

class Methods:

    @staticmethod
    def company_name(name):                                       
        print(f"The name of company is {name}")

    def display_name(name_1):                                  
        Methods.company_name(name_1)

Methods.display_name("JALA Tech")               