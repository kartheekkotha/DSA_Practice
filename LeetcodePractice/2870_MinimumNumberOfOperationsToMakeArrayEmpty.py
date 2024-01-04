# You are given a 0-indexed array nums consisting of positive integers.

# There are two types of operations that you can apply on the array any number of times:

# Choose two elements with equal values and delete them from the array.
# Choose three elements with equal values and delete them from the array.
# Return the minimum number of operations required to make the array empty, or -1 if it is not possible.

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        count = 0
        for i in dic:
            val = dic[i]
            if(val==1):
                return -1
            if(val %3 == 0):
                count+= val//3
            else:
                count+= val//3 +1
        return count