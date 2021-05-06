friends = [ "Manoj", 'Swadesh', 'Rajat', 'Sen', 'Bhalu', 'Asis', 'Aniket', 'Asir', 'Ayush', 'Omm']

#append
friends.append("Arijit")
print(friends)

#iterator
itr = iter(friends)
for i in range(len(friends)-1):
    print(next(itr))

#adding at specific index
friends.insert(4,"Abhisek")
print(friends)

#removing element
friends.remove("Abhisek")
print(friends)

#removing from particular index..
friends.pop(5)
print(friends)

#updating..
friends[4] = "Abhisek"
print(friends)

#Check the element is present at a particular index...
if "Rajat" in friends[2]:
    print("It is present")
else:
    print("Not present")

#Get an element at a particular index..
print(friends[1])

#Find out the size of the ArrayList..
print(len(friends))

#Check the given element is present in the ArrayList...
for i in range(len(friends)):
    if friends[i] == "Omm":
        print("Element is present in the Friend List.")
        
#Remove all elements of the ArrayList..
friends.clear()
print(f"friends = {friends}")
    