#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        current=0
        for i in range(len(nums)):
            if nums[i]==val:
                continue
            nums[current]=nums[i]
            current+=1
        return current   
# @lc code=end

