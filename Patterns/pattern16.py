class Pattern16:
    def pat16(self,n):
        self.no=n
    def method(self):
        for i in range(1,self.no+1):
            for j in range(i):
                print(chr(65+i-1),end="")
            print()
pat=Pattern16()
a=int(input("Enter value:"))
pat.pat16(a) 
pat.method()   