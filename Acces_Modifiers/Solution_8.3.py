#Accessing the protected fields or methods of a class in same package...

import sys
from Mathematics.Operations import Operation


o=Operation()

print(o._sum(4,5))
print(o._sub(4,3))
print(o._mult(5,6))

