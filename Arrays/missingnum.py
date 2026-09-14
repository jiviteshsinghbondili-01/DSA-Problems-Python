class Solution:
    def missingNumber(self, nums):
        n=len(nums)
        total=0
        for i in range(n):
            total=total+nums[i]
        val=n*(n+1)//2
        result=val-total
        print("missing num:",result)
sol=Solution()
nums=list(map(int,input("enter no:").split()))
sol.missingNumber(nums)