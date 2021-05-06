# Write a program with multiple catch blocks

class Multiple_Errors:
    def operation(self,number):
        try:
            print(int(number) + 5)
            print(sum_number)
            print(number/0)

        except:
            ValueError()
        except:
            NameError()
        except:
            ZeroDivisionError(number)
        
m = Multiple_Errors()
m.operation(8)