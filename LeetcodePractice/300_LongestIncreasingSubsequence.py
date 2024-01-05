# Given an integer array nums, return the length of the longest strictly increasing 
# subsequence
# .

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        val = [0 for x in range(length)]
        for i in range(1, length):
            for j in range(0 , i):
                if(nums[i] > nums[j] and val[i]<=val[j]):
                    val[i] = val[j] +1
        return max(val)+1
            