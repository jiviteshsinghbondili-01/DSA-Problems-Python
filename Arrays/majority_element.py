class Solution:
    def majorityElement(self,nums):
        for i in range(len(nums)):
            task=nums[i]
            count=0
            for j in range(len(nums)):
                if task==nums[j]:
                    count += 1
            if count>len(nums) // 2:
                return task
sol=Solution()
nums=list(map(int,input("Enter values:").split()))
print(sol.majorityElement(nums))