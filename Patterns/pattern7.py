class Pattern7:
    def pat7(self,n):
        self.no=n
    def method(self):
        for i in range(0,self.no):
            for j in range(self.no-i-1):
                print(" ",end="")
            for k in range(2*i+1):
                print("*",end="")
            print()
pat=Pattern7()
a=int(input("Enter value:"))
pat.pat7(a) 
pat.method() 