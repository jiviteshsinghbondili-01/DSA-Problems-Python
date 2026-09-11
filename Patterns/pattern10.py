class Pattern10:
    def pat10(self,n):
        self.no=n
    def method(self):
        for i in range(1,self.no+1):
            for j in range(i):
                print("*",end="")
            print()
        for i in range(1,self.no+1):
            for j in range(self.no-i):
                print("*",end="")
            print()
pat=Pattern10()
a=int(input("Enter value:"))
pat.pat10(a) 
pat.method()    