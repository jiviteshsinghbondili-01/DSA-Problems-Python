class Solution:
    def mySqrt(self,n):
         low=0
         high=n
         ans=0
         while low<=high:
            mid=(low+high)//2
            if mid*mid==n:
                return mid
            elif mid*mid<n:
                ans=mid
                low=mid+1
            else:
                high=mid-1
         return ans
sol=Solution()
n=int(input("Enter num:"))
print(sol.mySqrt(n))