# Write a program to generate Arithmetic Exception

class Solution:
    def display(self,a,b):
        try:
            print(a)
            print(b)
            print(a / b)
        
        except ZeroDivisionError :
            print("Zero Division Error: Number cannot be divisible by 0.")
        
        finally:
            print(a + b)
        

if __name__ == "__main__":
    s = Solution()
    s.display(4,0)

