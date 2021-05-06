import array

arr1 = array.array( 'i' , [40,12,12,23,10,10,22] )

for i in range(0,len(arr1)):
    for j in range(i+1,len(arr1)):
        if arr1[i] == arr1[j]:
            print(arr1[j])