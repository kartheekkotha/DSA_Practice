# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

# Return the minimum number of operations needed to make s alternating.

class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        one_odd = 0
        one_even = 0
        length = len(s)
        for i in range(0, length):
            if(i%2==0 and s[i] == "1"):
                one_even+=1
            if(i%2!=0 and s[i] == "1"):
                one_odd+=1
        if(length%2==0):
            zero_even = length//2 - one_even
        else:
            zero_even = length//2 - one_even+ 1
        zero_odd = length//2 - one_odd 
        return min((one_odd + zero_even),(one_even + zero_odd))

        