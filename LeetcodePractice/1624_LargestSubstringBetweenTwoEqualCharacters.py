# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

# A substring is a contiguous sequence of characters within a string.


class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        maxCount = -1
        for i in range(0,length):
            count = 0
            for j in range(i+1,length):
                if(s[i]== s[j]):
                    if(maxCount < count):
                        maxCount = count
                count+=1
        return maxCount