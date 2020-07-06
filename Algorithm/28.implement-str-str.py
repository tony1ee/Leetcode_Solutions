#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        output=-1
        if needle==haystack:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:].startswith(needle):
                output=i
                return output
        return output


# @lc code=end

