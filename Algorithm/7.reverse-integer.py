#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    # credit: https://leetcode.com/problems/reverse-integer/discuss/132861/3-lines-Python-Solution
    def reverse(self, x: int) -> int:
        sign = [1,-1][x < 0]
        # [1,-1] is a list which has two elements, [x<0] is as a slice,when false is 0 ,when true is 1,so the express can get the emements
        rst = sign * int(str(abs(x))[::-1])
        return rst if -(2**31)-1 < rst < 2**31 else 0

class Solution1:
    def reverse(self, x: int) -> int:
        result=0
        if x<0:
            negative=True
            x=-x
        else:
            negative=False
        while(x//10!=0):
            result=result*10+x%10
            x=x//10
        result=result*10+x
        if negative:
            result=-result
        if not -2**31-1<result<2**31-1:
            result=0
        return result
        
# @lc code=end

