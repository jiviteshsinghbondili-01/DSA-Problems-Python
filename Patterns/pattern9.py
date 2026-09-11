class Pattern9:
    def pat9(self,n):
        self.no=n
    def method(self):
         for i in range(0,self.no):
            for j in range(self.no-i-1):
                print(" ",end="")
            for k in range(2*i+1):
                print("*",end="")
            print()
            for i in range(1,self.no):
                for j in range(i):
                    print(" ",end="")
                for k in range(2*(self.no-i)-1):
                    print("*",end="")
                print()
pat=Pattern9()
a=int(input("Enter value:"))
pat.pat9(a) 
pat.method()