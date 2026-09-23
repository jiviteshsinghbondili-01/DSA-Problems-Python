class Solution:
    def maxSubArray(self, nums):
        tot=0
        max_sum=nums[0]
        for i in range(len(nums)):
            tot=tot+nums[i]
            if tot>max_sum:
                max_sum=tot    
            if tot<0:
                tot=0
        print(max_sum)
sol=Solution()
nums=list(map(int,input("Enter values:").split()))
sol.maxSubArray(nums)