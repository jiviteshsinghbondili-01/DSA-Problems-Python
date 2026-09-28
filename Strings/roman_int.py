class Solution:
    def romanToInt(self, s: str) -> int:
        tot=0
        roman={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        };
        i=0
        while i<len(s):
            if i+1<len(s) and roman[s[i]]<roman[s[i+1]]:
                tot=tot-roman[s[i]]
            else:
                tot=tot+roman[s[i]]
            i+=1
        return tot
sol=Solution()
s=input("Enter str:")
print(sol.romanToInt(s))