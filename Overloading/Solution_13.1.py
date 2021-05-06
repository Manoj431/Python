# two methods with the same name but different number of parameters of same type
# and call the methods from main method

class House:
    
    def display(self,name):
        print(f"The name of the building is {name} ")

    def display(self,name,address):
        print(f"The name of building is {name} , located in {address}. ")

if __name__ == '__main__':

    flat = House()
    # flat.display("Srivari Nilaya")     This will show error. Because in method overloading the last method is considered.

    flat.display("Supratik Styles", "Balasore")
