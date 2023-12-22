# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        zCount = 0
        oCount = 0
        for i in s:
            if i == "0":
                zCount+=1
            else:
                oCount+=1
        leftZ = 0
        rightO = oCount
        if s[0] == "0":
            maxCount = oCount+1
        else:
            maxCount = oCount-1
        count = maxCount
        for i in range(1,len(s)-1):
            if s[i] == "0":
                count+=1
            else:
                count -= 1
            if count > maxCount:
                maxCount = count
        return maxCount