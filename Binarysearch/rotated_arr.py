class Solution:
    def search(self,nums,k):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==k:
                return mid
            elif nums[left]<=nums[mid]:
                if nums[left]<=k<=nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<=k<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1
sol=Solution()
nums=list(map(int,input("Enter values:").split()))
k=int(input("Enter no:"))
print(sol.search(nums,k))

