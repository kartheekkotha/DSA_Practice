# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, 
# due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
# You are given an integer array nums representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the form of an array.

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length = len(nums)
        isThere = [False for _ in range(length)]
        output = []
        for i in nums:
            if(isThere[i-1] == True):
                output.append(i)
            isThere[i-1] = True
        for i in range(0 , length):
            if isThere[i] == False:
                output.append(i+1)
                return output
        return output