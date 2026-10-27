class Solution:
    def findKRotation(self,nums):
         left=0
         right=len(nums)-1
         while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
         return left
sol=Solution()
nums=list(map(int,input("Enter values:").split()))
print(sol.findKRotation(nums))