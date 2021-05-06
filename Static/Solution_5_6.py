class Methods:
    name_1="IBM"                                              #Static Variables
    year_1=1911 

    def __init__(self,name,year):                
        self.name=name                                        #Instance Variable..
        self.year=year  

if __name__ == '__main__':
    m = Methods("Jala",2017)
    print(m.name_1)
    print(m.year_1)
    print(m.name)
    print(m.year)