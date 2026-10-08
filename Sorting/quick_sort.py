class Solution:
    def quickSort(self,nums):
        if len(nums)<=1:
            return nums
        pivot=nums[len(nums)//2]
        left=[]
        middle=[]
        right=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                left.append(nums[i])
            elif nums[i]==pivot:
                middle.append(nums[i])
            else:
                right.append(nums[i])
            res=left+[pivot]+right
        return self.quickSort(left)+middle+self.quickSort(right)
sol=Solution()
nums=list(map(int,input("Enter values:").split()))
print(sol.quickSort(nums))