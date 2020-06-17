#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        left=['(','{','[']
        right=[')','}',']']
        parenthesesDict=dict(zip(right,left))
        for letter in s:
            if letter in left:
                stack.append(letter)
            elif letter in right:
                if not stack:
                    return False
                if not parenthesesDict[letter]==stack.pop():
                    return False
        return stack==[]
                    

        
# @lc code=end

