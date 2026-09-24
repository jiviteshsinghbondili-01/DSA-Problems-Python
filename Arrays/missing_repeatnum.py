class Solution:
    def findMissingAndRepeatedNumbers(self,nums):
        n=len(nums)
        duplicate=0
        missing=0
        for i in range(1,n+1):
            count=0
            for j in range(n):
                if nums[j]==i:
                    count+=1
            if count==2:
                duplicate=i
            if count==0:
                missing=i
        return [duplicate,missing]
sol=Solution()
nums=list(map(int,input("Enter values:").split()))
print(sol.findMissingAndRepeatedNumbers(nums))