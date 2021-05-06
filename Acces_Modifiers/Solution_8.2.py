#Calling methods of other class with in same package...

import sys
from Mathematics.Area import Shapes                       

b=Book()
sq=b.square(5)
rec=b.rectangle(4,8)
cir=b.circle(6)

print(f"The area of square is : {sq}")

print(f"The area of rectangle is : {rec}")

print(f"The area of circle is : {cir} ")
