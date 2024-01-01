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
    

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_index = {}
        ans = -1
        
        for i in range(len(s)):
            if s[i] in first_index:
                ans = max(ans, i - first_index[s[i]] - 1)
            else:
                first_index[s[i]] = i

        return ans