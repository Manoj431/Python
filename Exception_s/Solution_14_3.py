class Errors:
    def fruits(self,name):
        if not type(name) is str:
            raise TypeError
        else:
            print(f"{name} is a fruit ")

if __name__ == "__main__":
    e=Errors()
    e.fruits(12.4)