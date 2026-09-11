class Reverse:
    def rev(self,n):
        self.no=n
    def method(self):
        b=0
        while self.no!=0:
            a=self.no%10
            b=b*10+a
            self.no=self.no//10
        print("the reverse is:",b)
reverse=Reverse()
a=int(input("Enter value:"))
reverse.rev(a) 
reverse.method()