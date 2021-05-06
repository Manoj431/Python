# Write two methods with the same name and same number of parameters of different
# type and call from main method


class Employee:
    def details(self,name,company):
        print(f"The name of Employee is {name}. ")
        print(f"{name} works at {company}.")
        print(f"The {company} is located in {location} ")

    def details(self,id,salary):
        print(f"The ID  is {id}")
        print(f"The salary is {salary}")
        

if __name__ == '__main__':
    emp = Employee()
    emp.details("Manoj Barik","Jala Tech")
    emp.details(1013,25000)