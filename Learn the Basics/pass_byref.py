class Reverse:
    def value(self,a):
        self.arr=a
    def method(self):
        left=0
        right=len(self.arr)-1
        while(left<right):
            self.arr[left],self.arr[right]=self.arr[right],self.arr[left]
            left+=1
            right-=1
        return self.arr    
a=Reverse()
a.value([1,2,4,5,6])
print(a.method())