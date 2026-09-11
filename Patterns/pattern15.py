class Pattern15:
    def pat15(self,n):
        self.no=n
    def method(self):
        for i in range(1,self.no+1):
            for j in range(self.no-i+1):
                print(chr(65+j),end="")
            print()
pat=Pattern15()
a=int(input("Enter value:"))
pat.pat15(a) 
pat.method()