# Write a program to generate ArrayIndexOutOfBoundException..

def cricketers(li):
    try:
        for i in range(len(li)+1):
            print(li[i])

    except IndexError:
        print(f"Index Error : The list range is {len(li)}. Upto {len(li)}th element can be accessed. ")
    
cricketers(["Dhoni", "Yuvraj", "Virat", "MacCullum"])