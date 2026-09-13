class Armstrong:
    def arm(self,n):
        self.no=n
    def method(self):
        original=self.no
        res=0
        x=len(str(self.no))
        while self.no!=0:
            a=self.no%10
            res+=a**x
            self.no=self.no//10
        return original==res
c=Armstrong()
a=int(input("Enter value:"))
c.arm(a)
print(c.method())
