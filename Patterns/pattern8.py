
 class Pattern8:
    def pat8(self,n):
        self.no=n
    def method(self):
        for i in range(self.no):
            for j in range(i):
                print(" ",end="")
            for k in range(2*(self.no-i)-1):
                print("*",end="")
            print()
pat=Pattern8()
a=int(input("Enter value:"))
pat.pat8(a) 
pat.method()           