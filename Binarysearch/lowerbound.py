class Solution:
    def lowerBound(self, nums, x):
        low=0
        high=len(nums)
        while low<high:
            mid=(low+high)//2
            if nums[mid]>=x:
                high=mid
            else:
                low=mid+1
        return low
sol=Solution()
nums=list(map(int,input("Enter values:").split()))
x=int(input("Enter no:"))
print(sol.lowerBound(nums,x))