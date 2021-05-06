def pallin(num):
    temp = num
    rev=0
    while temp != 0:
        a = temp % 10
        rev = rev * 10 + a
        temp = temp // 10
    
    if num == rev:
        print(f"{num} is pallindrome.")
    else:
        print(f"{num} is not pallindrome.")

pallin(5325)
    

