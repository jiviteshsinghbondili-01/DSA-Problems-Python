class Solution:
    def linearSearch(self, nums, target):
        for i in range(len(nums)):
            if nums[i]==target:
                print("the index is:",i)
                break
        else:
            print(-1)
sol=Solution()
nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter number: "))
sol.linearSearch(nums,target)