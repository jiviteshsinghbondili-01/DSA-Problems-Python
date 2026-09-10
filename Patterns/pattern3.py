class Pattern3:
    def var3(self,n):
        self.no=n
    def method3(self):
        for i in range(1,self.no+1):
            for j in range(1,i+1):          
                print(j,end=" ")
            print()
pat=Pattern3()
n=int(input("Enter no of stars:"))
pat.var3(n)
pat.method3()