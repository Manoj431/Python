#Call the constructors(both default and argument constructors) of super class from a child class

class Flats:
    def __init__(self):                                                          
        print("We have varities of flats like 1BHK, 2HK, 3BHK, 4BHK, 5BHK.")

    @classmethod
    def building_no(self,number):                                                   
        print(f"The number of  building is {number} ")
        

    @classmethod                    
    def building_details(self,name,area):                                                               
        print(f"The name of building is {name} ,located in {area}. ")

class One_Bhk(Flats):
    def __init__(self):
        super().__init__()
    
    def flat_no(self,number):
        super().building_no(number)
    
    def flat_details(self,name,area):
        super().building_details(name,area)

if __name__ == '__main__':
    one = One_Bhk()
    one.flat_no("#18/220")
    one.flat_details("GRR Residency","Munnekolala")