 class Pattern6:
    def pat6(self,n):
        self.no=n
    def method(self):
        for i in range(0,self.no):
            for j in range(1,self.no-i+1):
                print(j,end=" ")
            print()
pat=Pattern6()
a=int(input("Enter value:"))
pat.pat6(a) 
pat.method()   