class Solution:
    def beautySum(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            words={}
            for j in range(i,len(s)):
                if s[j] in words:
                    words[s[j]]+=1
                else: 
                    words[s[j]]=1
                max_words=max(words.values())
                min_words=min(words.values())
                beauty=max_words-min_words
                res+=beauty
        return res
sol=Solution()
s=input("Enter String:")
print(sol.beautySum(s))