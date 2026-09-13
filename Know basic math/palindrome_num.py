class Palindrome:
    def pal(self,n):
        self.no=n
    def method(self):
        res=self.no
        b=0
        while self.no!=0:
            a=self.no%10
            b=b*10+a
            self.no=self.no//10
        return res==b
palin=Palindrome()
a=int(input("Enter value:"))
palin.pal(a) 
print(palin.method())