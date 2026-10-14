class Solution:
    def getFloorAndCeil(self,nums,x):
        left=0
        right=len(nums)-1
        floor=-1
        ceil=-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==x:
                return [x,x]
            elif nums[mid]<x:
                floor=nums[mid]
                left=mid+1
            else:
                ceil=nums[mid]
                right=mid-1
        return [floor,ceil]
sol=Solution()
nums=list(map(int,input("Enter values:").split()))
x=int(input("Enter no:"))
print(sol.getFloorAndCeil(nums,x))

