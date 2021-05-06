import array 

numbers = [11,22,33,44,9,50,2]
arr = array.array('i', numbers)
even=0
odd=0

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        even += 1
    else:
        odd +=1

print(f"There are {even} EVEN no.s  \n There are {odd} ODD no.s  ")
