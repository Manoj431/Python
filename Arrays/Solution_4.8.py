import array

arr1 = array.array( 'i' , [40,120,2,10,54,1000])
max = 22
min = 12


for i in range(0,len(arr1)):
    if arr1[i] >= max:
        max = arr1[i]
    
    elif arr1[i] <= min:
        min = arr1[i]

print(min)
print(max)



