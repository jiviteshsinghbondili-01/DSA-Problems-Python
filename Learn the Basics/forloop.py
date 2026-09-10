class Loop:
    def forloop(self,low,high):
        self.low=low
        self.high=high
    def loop(self):
        tot=0
        for i in range(self.low,self.high+1):
            tot=tot+i
        return tot
ans=Loop()
a=int(input("enter a:"))
b=int(input("enter b:"))
ans.forloop(a,b)
print(ans.loop())