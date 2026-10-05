class Solution:
    def bubbleSort(self, nums):
        for num in range(len(nums)):
            i=0
            while i<len(nums)-1-num:
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
                i+=1
        return nums
sol=Solution()
nums=list(map(int,input("Enter values:").split()))
print(sol.bubbleSort(nums))