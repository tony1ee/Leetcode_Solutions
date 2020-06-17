#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        prefix=""
        test_prefix=""
        if strs:
            if len(strs)==1:
                return strs[0]
            else:
                strs.sort()
                for i in range(len(strs[0])):
                    test_prefix+=strs[0][i]
                    for item in strs:
                        if not item.startswith(test_prefix):
                            return prefix
                    prefix=test_prefix
            return prefix 
        else:
            return ""    
# @lc code=end
s=Solution()
print(s.longestCommonPrefix(["c","c"]))
