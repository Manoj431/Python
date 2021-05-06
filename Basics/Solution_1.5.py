company = "Jala Tech"      #Global Variable

def name():
    company = "IBM"      '''Local Variable and it is accessable only within this function.
                                 No other function cannot access it.'''
    print(company)       

def global_name():
    print(company)        #It will print the global variable.
 
name()
global_name()

print(company)


