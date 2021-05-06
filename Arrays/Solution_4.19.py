#Write a function to find the missing number of sorted array of 1 to 100
def search(ar, size):
    a = 0
    b = size - 1
    mid = 0
    while b > a + 1:
        mid = (a + b) // 2
        if (ar[a] - a) != (ar[mid] - mid):
            b = mid
        elif (ar[b] - b) != (ar[mid] - mid):
            a = mid
    return ar[a] + 1
a = []
for i in range(1,101):
    a.append(i)
del a[22]
n = len(a)

print("Missing number:", search(a, n))