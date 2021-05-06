def prime(a):
    if a > 0:
        for i in range(2,a):
            if a % i == 0:
                print(f"{a} is not a prime number. ")
                break
        else:
            print(f"{a} is a prime number.")
    else:
        print(f"{a} is a negative integer. Cannot find out prime or not")    

prime(97)
    