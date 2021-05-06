class Methods:
    def __init__(self,name,year):                
        self.name=name                                        #Instance Variable..
        self.year=year

    @staticmethod
    def company():   
        super().__init__(self,name,year)                                    
        print(f"The name of company is {Methods.name}")
        print(f"It was invented in {Methods.year}.")

m = Methods("Jala",2017)
m.company()