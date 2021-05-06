#Try to call the constructor multiple times with the same object

class Flats:
    def __init__(self):                                                              
        print("We have varities of flats like 1BHK, 2HK, 3BHK, 4BHK, 5BHK.")

    @classmethod
    def building_no(self,number):                                                 
        print(f"The number of  building is {number} ")
        

    @classmethod                    
    def building_details(self,name,area):                                                            
        print(f"The name of building is {name} ,located in {area}. ")

if __name__=='__main__':

    f = Flats()
    f.building_no("#18/226")
    f.building_details("Srivari Nilaya","Munnekolala")