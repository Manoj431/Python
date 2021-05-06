def armstrong(num):
    copy=num
    sum=0
    while num > 0:
        a=num % 10
        sum=sum + a*a*a
        num=num // 10
    if copy == sum:
        print("It is an Armstrong number. ")
    else:
        print("It is not an Armstrong number.")

armstrong(153)