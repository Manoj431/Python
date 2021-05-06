import array

arr1 = array.array( 'i' , [60,55,58,42,11,23,10,22,54,59] )

first = second = arr1[0]
for j in range(1, len(arr1)):
    if(arr1[j] > first):
        second = first
        first = arr1[j]
    elif(arr1[j] > second and arr1[j] < first):
        second = arr1[j]

print(second)