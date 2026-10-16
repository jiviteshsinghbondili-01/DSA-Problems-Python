class Solution:
    def searchInARotatedSortedArrayII(self,nums,k):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==k:
                return True
            elif nums[left]==nums[mid]==nums[right]:
                left+=1
                right-=1
                continue
            elif nums[left]<=nums[mid]:
                if nums[left]<=k<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<k<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return False
sol=Solution()
nums=list(map(int,input("Enter values:").split()))
k=int(input("Enter no:"))
print(sol.searchInARotatedSortedArrayII(nums,k))

