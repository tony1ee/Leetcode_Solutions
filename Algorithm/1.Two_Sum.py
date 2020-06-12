class Solution:
    # 6000 ms
    # 14.9 MB
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j]==target-nums[i]:   
                    return [i,j]

class Solution1:
    # 44 ms
    # 14.9 MB
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict={} # use hash dictionary
        for i,num in enumerate(nums):
            complement=target-num
            if complement not in numdict:
                numdict[num]=i
            else:
                return [numdict[complement],i]

