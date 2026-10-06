class Solution:
    def insertionSort(self, nums):
            i=1
            while i<len(nums):
                j=i
                while j>0 and nums[j]<nums[j-1]:
                    nums[j],nums[j-1]=nums[j-1],nums[j]
                    j-=1
                i+=1
            return nums
sol=Solution()
nums=list(map(int,input("Enter values:").split()))
print(sol.insertionSort(nums))