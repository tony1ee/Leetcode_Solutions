#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lenth=0
        for i in range(len(nums)):
            if nums[lenth]<nums[i]:
                lenth+=1
                nums[lenth]=nums[i]
        return lenth+1
# @lc code=end

