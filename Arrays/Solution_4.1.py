import array
number_array = array.array( 'i' , [10,20,3,54] )    # Array with integer values..

sum=0
for i in range(len(number_array)):
    sum = sum + number_array[i]

print(f"After adding the integer values of array, the value is : {sum} ")

