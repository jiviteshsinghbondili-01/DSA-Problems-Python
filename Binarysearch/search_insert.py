class Solution:
    def searchInsert(self,nums,target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left
sol=Solution()
nums=list(map(int,input("Enter values:").split()))
target=int(input("Enter no:"))
print(sol.searchInsert(nums,target))