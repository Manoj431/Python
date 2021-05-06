import array

arr1 = array.array( 'i' , [40,12,23,10,22] )
arr2 = array.array('i')


for i in range(len(arr1)-1,-1,-1):
    arr2.append(arr1[i])

print(arr2)