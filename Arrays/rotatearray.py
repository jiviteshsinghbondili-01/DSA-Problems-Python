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
nums=list(map(int,input("Enter values:").split()))
k=int(input("Enter num:"))
sol.rotateArray(nums, k)
print(nums) 