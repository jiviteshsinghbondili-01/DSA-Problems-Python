class Pattern1:
    def var(self, n):
        self.no=n
    def method(self):
        for i in range(1,self.no+1):
            for j in range(1,self.no+1):
                print("*",end=" ")
            print()
pat=Pattern1()
n=int(input("Enter no of stars:"))
pat.var(n)
pat.method()
