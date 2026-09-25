class Solution:
    def rotateArrayByOne(self, nums):
        res=[]
        arr=nums[0]
        for i in range(1, len(nums)):
            res.append(nums[i])
        res.append(arr)
        nums[:]=res
        print(nums)
sol=Solution()
nums=list(map(int,input("Enter values:").split()))
sol.rotateArrayByOne(nums)