class A:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.txt="This is 1st class"
       
    def sum(self):
         s = self.num1 + self.num2
         return s

    def sub(self):
        if self.num1 > self.num2:
            d = self.num1 - self.num2
            return d
        elif self.num1 < self.num2:
            d = self.num2 - self.num1
            return d
        
    def display(self):
        print(self.txt)


class B(A):
    def __init__(self,num1,num2):
        super().__init__(num1,num2)
        

    def mult(self):
        m = self.num1 * self.num2
        return m

    def divi(self):
        di = self.num1 / self.num2
        return di

    def display(self,txt):
        print(txt)

class C(B):
    def __init__(self,num1,num2):
        super().__init__(num1,num2)
        
    
    def mod(self):
        remainder = self.num1 % self.num2
        return remainder

    def power(self):
        p = self.num1 ** self.num2
        return p

    def display(self,txt):
        print(txt)



if __name__=='__main__':
    a = A(6,4)
    b = B(5,10)
    c = C(8,2)
    
    print(a.sum())
    print(a.sub())
    a.display()
    
    print(b.mult())
    print(b.divi())
    b.display("This is 2nd class.")

    print(c.mod())
    print(c.power())
    c.display("This is 3rd class.")
    
