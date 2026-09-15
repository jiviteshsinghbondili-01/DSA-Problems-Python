class Solution:
    def largestElement(self,nums):
        largest=nums[0]
        for i in range(len(nums)):
            if nums[i]>largest:
                largest=nums[i]
        print(largest)
sol=Solution()
nums=list(map(int,input("Enter no:").split()))
sol.largestElement(nums)