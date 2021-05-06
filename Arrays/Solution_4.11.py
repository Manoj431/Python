import array

arr1 = array.array( 'i' , [40,11,26,23,10,22] )
arr2 = array.array( 'i' , [11,9,26,12,48])

for i in range(0,len(arr1)):
    for j in range(0,len(arr2)):
        if arr2[j] == arr1[i]:
            print(f"The duplicate number is: {arr2[j]}")            #{arr1[i]} can also be used..