#Write two methods with the same name and same number of parameters of same type
# and call from main method

class Cars:
    def model(self,type_car,speed):
        print(f"The {type_cars} cars goes up to {speed} ")
    
    def model(self,name,top_speed):
        print(f"The {name} goes up to {top_speed} ")

if __name__ == '__main__':
    stylish = Cars()
    stylish.model("Sports","250 MPH") 
    stylish.model("Hennessey Venom F5","301 MPH")

#Only the last method is always considered.