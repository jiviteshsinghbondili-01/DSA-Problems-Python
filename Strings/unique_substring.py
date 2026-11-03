class Solution:
    def Uniquesubstring(self,s):
        max_count=0
        for i in range(len(s)):
            count=0
            res=""
            for j in range(i,len(s)):
                if s[j] not in res:
                    res+=s[j]
                    count+=1
                else:
                    break
            if count>max_count:
                max_count=count
        return max_count
sol=Solution()
a=str(input("Enter word:"))
print(sol.Uniquesubstring(a))