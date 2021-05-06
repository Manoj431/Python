#Write a program with finally block

class Car:
    def sports_car(self,speed):
        try:
            if float(speed) > 200:
                print(f"The speed of car is {speed} MPH.")
        
        except ValueError:
            print("Value should be integer")

        finally:
            print("All sports car have an average speed of 250 MPH.")

c = Car()
c.sports_car(230)
