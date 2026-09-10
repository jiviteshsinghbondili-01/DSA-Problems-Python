class Pattern4:
    def pat4(self,n):
        self.no=n
    def method(self):
        for i in range(1,self.no+1):
            for j in range(i):
                print(i,end=" ")
            print()
pat=Pattern4()
a=int(input("Enter value:"))
pat.pat4(a) 
pat.method()  