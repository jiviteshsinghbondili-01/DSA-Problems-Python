class Solution:
    def sorting(self, nums):
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                print(False)
                break
        else:
            print(True)
sol=Solution()
nums=list(map(int,input("Enter no:").split()))
sol.sorting(nums)