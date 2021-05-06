#In Python , we use double underscore(__) to represent it as PRIVATE...

class Student:
    __school = "Dav Public Scool"       #private field
    
    def __details(self,name,roll):
        self.__name = name              #private fields
        self.__roll = roll

    def __print(self):                      #private method
        print(f"The name of student is {self.__name}")

   
s=Student()
def main():
    s._Student__details("Manoj Barik", 16)  
    print(s._Student__school)
    print(s._Student__name)
    print(s._Student__roll)
    s._Student__print()    
    
if __name__ == "__main__":
    main()

class Student1(Student):
    def print_details(self,name,age):
        self._Student__details(name,age)
        self._Student__print()
c=Student1()
c.print_details("Ravi",45)
c._Student__print()

