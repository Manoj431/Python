'''Python does not have a do while loop. But we can approach in similar manner using while loop.'''

number=1
while True:                 #Instead of condition we used TRUE
    print(number)
    number += 1

    if number > 10:         #Condition is placed inside the loop
        break
