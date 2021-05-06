#Splitting strings with split().....

cars = "Mustang,Buggati,Porsche,Maserati,BMW"

print(cars.split(','))              #splits the whole string

print(cars.split(',',2))            #splits upto only 2 elements

#rsplit(). It separates from right side....

print(cars.rsplit(',',2))