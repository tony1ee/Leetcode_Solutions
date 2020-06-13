#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start

class Solution:
    def romanToInt(self, s: str) -> int:
        result=0
        # romanDict={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        # use zip() to zip keys and values
        num=[1000,500,100,50,10,5,1]
        RomanExpression=['M','D','C','L','X','V','I']
        romanDict=dict(zip(RomanExpression,num))
        while(s):
            letter=s[0]
            num=romanDict[letter]
            sign= -1 if len(s)>1 and romanDict[s[1]]>num else 1
            result+=(num*sign)
            s=s[1:]
        return result
            


class Solution1:
    def romanToInt(self, s: str) -> int:
    #    Symbol       Value
    #     I             1
    #     V             5
    #     X             10
    #     L             50
    #     C             100
    #     D             500
    #     M             1000 
        num=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        RomanExpression=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        result=0
        for i in range(len(num)):
            while(s.startswith(RomanExpression[i])):
                result+=num[i]
                s=s[len(RomanExpression[i]):]
        print(result)
        return result
# @lc code=end

s=Solution()
print(s.romanToInt('MCMXCIV'))