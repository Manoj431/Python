import array

arr = array.array( 'i' , [45,62,23,80,12])

specific_number = 80
flag = False
for i in range(len(arr)):
    if arr[i] == specific_number:
        flag = True
        print("Item is available in the array.")
if flag == False:
    print("Item is NOT available in the array.")
    