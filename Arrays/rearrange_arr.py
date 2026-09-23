class Solution:
    def rearrangeArray(self, nums):
        pos=[]
        neg=[]
        for i in range(len(nums)):
            if nums[i]>0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        ans=[]
        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])
        print(ans)
sol=Solution()
nums=list(map(int,input("enter values:").split()))
sol.rearrangeArray(nums)