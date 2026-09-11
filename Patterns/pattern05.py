class Pattern5:
    def pat5(self,n):
        self.no=n
    def method(self):
        for i in range(0,self.no+1):
            for j in range(self.no-i):
                print("*",end=" ")
            print()
pat=Pattern5()
a=int(input("Enter value:"))
pat.pat5(a) 
pat.method() 