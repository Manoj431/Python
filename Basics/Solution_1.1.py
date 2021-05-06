#Defining a Class, Object, Method and its Signature

class Solution:
    def area(self,side):
        calc = side**2
        print(f"The area of a square field is {calc} sq.metre")

sol = Solution()   #Object creation of class Solution
sol.area(8)      #Calling the method through object