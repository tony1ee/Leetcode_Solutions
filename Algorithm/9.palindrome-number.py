#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negative integers cannot be palindrome
        # Also if the last digit of the number is 0, in order to be a palindrome,
        # the first digit of the number also needs to be 0.
        if x<0 or x%10==0:
            return False
        if x==0:
            return True
        original=x
        reverse=0
        while(x//10!=0):
            reverse=reverse*10+x%10
            x=x//10
        reverse=reverse*10+x%10
        # print("reverse=",reverse,"original=",original)
        if reverse==original:
            return True
        else:
            return False
        
# @lc code=end
