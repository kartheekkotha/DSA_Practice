# You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

# The 2D array should contain only the elements of the array nums.
# Each row in the 2D array contains distinct integers.
# The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them.

# Note that the 2D array can have a different number of elements on each row.


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        finalList = []
        tempList = []
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=0
                tempList.append(i)
        finalList.append(tempList)
        isEmpty = False
        while(not isEmpty):
            tempList = []
            isEmpty = True
            for i in dic:
                if dic[i] > 0:
                    isEmpty = False
                    tempList.append(i)
                    dic[i]-=1
            if(not isEmpty):
                finalList.append(tempList)
        return finalList