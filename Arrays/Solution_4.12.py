import array

arr1 = array.array( 'i' , [40,11,11,23,10,22] )


for i in range(0,len(arr1)):
    for j in range(i+1,len(arr1)):
        if arr1[j] == arr1[i]:
            dup=arr1[i]
arr1.remove(dup)


print(arr1)
