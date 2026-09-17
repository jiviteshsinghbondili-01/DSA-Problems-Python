class Solution:
    def singleNumber(self, nums):
        count=0
        for i in range(len(nums)):
            count=nums[i]^count
        return count
sol=Solution()
nums=list(map(int,input("Enter values:").split()))
print(sol.singleNumber(nums))