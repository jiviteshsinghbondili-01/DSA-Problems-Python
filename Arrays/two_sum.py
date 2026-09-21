class Solution:
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i):
                res=nums[i]+nums[j]
                if target==res:
                    return [j, i]
                    break
sol=Solution()
nums=list(map(int,input("Enter values:").split()))
target=int(input("Enter target:"))
print(sol.twoSum(nums,target))