class Solution:
    def unionArray(self,nums1,nums2):
        res=set(nums1).union(set(nums2))  
        return sorted(res)
sol=Solution()
nums1=list(map(int,input("Enter values:").split()))
nums2=list(map(int,input("Enter values:").split()))
print(sol.unionArray(nums1,nums2))



