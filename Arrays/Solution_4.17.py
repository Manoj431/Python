import array
numbers=[4,5,68,13,12,40,23]
arr = array.array('i',numbers)
s=[12,23]

flag1 = False
flag2 = False

for i in range(len(arr)):
    if s[0] == arr[i]:
        flag1= True  
    
    if s[1] == arr[i]:
        flag2=True

if flag1 == True and flag2 == True:
    print("Both elements are present")
else:
    print("Both elements not present..")


    
