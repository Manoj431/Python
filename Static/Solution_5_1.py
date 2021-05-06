class Methods:
    name="IBM"                                              #Static Variables
    year=1911                                               #Static Variables

    def __init__(self,name,year):                
        self.name=name                                        #Instance Variable..
        self.year=year                                        #Instance Variable...

    def display_name(self):                                   #Instance method
        print(f"The name of company is {self.name}")
    
    def display_year(self):
        print(f"It was created in the year {self.year}")             #Instance method

    @staticmethod
    def company_name():                                       #Static method
        print(f"The name of company is {Methods.name}")

    @staticmethod
    def company_year():                                       #Static method
        print(f"It was invented in {Methods.year}.")

    
    
if __name__ == "__main__":
    company = Methods("Jala",2017)
    company.display_name()
    company.display_year()
    company.company_name()
    company.company_year()


