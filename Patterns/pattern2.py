class Pattern2:
    def var2(self, n):
        self.no=n
    def method2(self):
        for i in range(1,self.no+1):
            for j in range(i):          
                print("*",end=" ")
            print()
pat=Pattern2()
n=int(input("Enter no of stars:"))
pat.var2(n)
pat.method2()
