#Hash Map.. It is same as Dictionary in map...

student = {"Manoj"    : 101,
            "Asir"    : 102,
            "Swadesh" : 103,
            "Rajat"   : 104,
            "Arijit"  : 105,
            "Sen"     : 106,
            "Aniket"  : 107,
            "Bhalu"   : 108,
            "Asis"    : 109,
            "Ayush"   : 110 }

#Value of a key..
print(student["Asir"])

#clone/copy of HashMap..
another_student = student.copy()
print(another_student)

#Check if the given Key is in the Map..
for key in student:
  if key == "Asis":
    print(f"{key} is in the Map.")

#Check if the given Key is in the Map..
for value in student:
  if student[value] == 102:
    print(f"{student[value]} is present in the Map..")

#Check if the map is empty..
if student != None:
  print("The Map is not empty.")


#Print the size of the Map to the console..
print("The size of tha Map is",len(student),"..")


#Print all the Keys of the map to the console..
for key in student:
  print(key)


#Print all the Values of the map to the console..
for values in student:
  print(student[values])

#Remove a specific Key-value pair..
print("Deleted key pair value is",student.pop("Asir"))
print(student)


#Copy all the elements of the Map to another Map...
new_student = student
print(new_student)