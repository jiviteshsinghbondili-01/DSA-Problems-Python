class Solution:
    def rotateArray(self, nums, k: int) -> None:
        k=k%len(nums)
        first=[]
        rem=[]
        for i in range(k):
            first.append(nums[i])
        for j in range(k, len(nums)):
            rem.append(nums[j])
        res=rem+first
        nums[:]=res
sol=Solution()
nums=[1, 2, 3, 4, 5, 6]
k=2
sol.rotateArray(nums, k)
print(nums) 