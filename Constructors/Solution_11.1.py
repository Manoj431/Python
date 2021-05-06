#Write a class with a default constructor, one argument constructor and two argument
#constructors. Instantiate the class to call all the constructors of that class from a main class


class Flats:
    def __init__(self):                                                          #default constructor..
        print("We have varities of flats like 1BHK, 2HK, 3BHK, 4BHK, 5BHK.")

    @classmethod
    def building_no(self,number):                                                    #one argument constructor
        print(f"The number of  building is {number} ")
        

    @classmethod                    
    def building_details(self,name,area):                                               #two argument constructor                
        print(f"The name of building is {name} ,located in {area}. ")
if __name__=='__main__':

    f = Flats()
    bn = Flats.building_no("#18/226")
    b = Flats.building_details("Srivari Nilaya","Munnekolala")
    