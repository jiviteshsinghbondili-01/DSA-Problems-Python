class Solution:
    def sortZeroOneTwo(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
sol=Solution()
nums=list(map(int,input("Enter values:").split()))    
sol.sortZeroOneTwo(nums)
print(nums)