class Methods:
    name="IBM"                                              #Static Variables
    year=1911 

    def display_name(self):                                   #Instance method
        print(f"The name of company is {self.name}")
    
company = Methods()
company.display_name()