import math
class Shapes:
    def square(self,side):
        area_square = side * side
        return area_square

    def rectangle(self,length,breadth):
        area_rectangle = length * breadth
        return(area_rectangle)

    def circle(self,radius):
        area_circle = math.pi * radius * radius
        return area_circle
