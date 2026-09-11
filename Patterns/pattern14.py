class Pattern14:
    def pat14(self,n):
        self.no=n
    def method(self):
        for i in range(1,self.no+1):
            for j in range(i):
                print(chr(65+j),end="")
            print()
pat=Pattern14()
a=int(input("Enter value:"))
pat.pat14(a) 
pat.method()           