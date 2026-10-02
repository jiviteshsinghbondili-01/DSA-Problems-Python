class Solution:
    def longestPalindrome(self,s:str)->str:
        final=""
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                res1=s[i:j]
                res2=res1[::-1]
                if res1==res2:
                    if len(res1)>len(final):
                        final=res1
        return final
sol=Solution()
s=input("Enter String:")
print(sol.longestPalindrome(s))