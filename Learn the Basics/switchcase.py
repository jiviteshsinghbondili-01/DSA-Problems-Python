class Solution:
    def weekdays(self,day):
        self.day=int(day)
    def method(self):
       match self.day:
             case 1:
                print("Monday")
             case 2:
                print("tuesday")
             case 3:
                print("Wednesday")
             case 4:
                print("thursday")
             case 5:
                print("friday")
             case 6:
                print("saturday")
             case 7:
                print("sunday")
             case _:
                print("invalid")
sol=Solution()
n=int(input("Enter week:"))
sol.weekdays(n)
sol.method()