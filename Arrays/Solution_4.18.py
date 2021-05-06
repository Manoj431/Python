#Write a program to remove the duplicate elements and return the new array..

import array

arr1 = array.array( 'i' , [4,5,13,2,5,6,5,13,9])
new_array = array.array('i')
for i in arr1:
    if not i in new_array:
        new_array.append(i)

print(new_array)