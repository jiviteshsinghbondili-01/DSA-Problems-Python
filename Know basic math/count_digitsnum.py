class Counter:
    def counting(self,n):
        self.no=n
    def method(self):
        count=0
        value=0
        while self.no!=0:
            a=self.no%10
            count=count*10+a
            if count!=0:
                value+=1
            self.no=self.no//10
        print(value)
c=Counter()
a=int(input("Enter value:"))
c.counting(a) 
c.method()