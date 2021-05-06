def largest(a,b,c):
    if a > b:
        if a > c:
            print(f"{a} is the Greatest number.")
        else:
            print(f"{c} is the Greatest number.")
    else:
        if b > c:
            print(f"{b} is the Greatest number.")
        else:
            print(f"{c} is the Greatest number.")

largest(10,20,30)