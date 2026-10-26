class Solution:
    def countOccurrences(self,arr,target):
        left=0
        right=len(arr)-1
        count=0
        while left<=right:
            mid=(left+right)//2
            if arr[mid]==target:
                count+=1
                arr=arr[:mid]+arr[mid+1:]
                right=len(arr)-1
            elif arr[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return count
sol=Solution()
arr=list(map(int,input("Enter values:").split()))
target=int(input("Enter num:"))
print(sol.countOccurrences(arr,target))