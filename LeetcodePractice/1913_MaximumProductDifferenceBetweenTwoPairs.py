'''
The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference
'''



class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = nums[:4]
        arr.sort()
        One_One = arr[0]
        One_Two = arr[1]
        Two_One = arr[2]
        Two_Two = arr[3]
        
        for i in range(4,len(nums)):
            if nums[i] >= Two_Two:
                if(One_One > Two_One):
                    One_Two = One_One
                    One_One = Two_One
                elif(One_Two > Two_One and One_One < Two_One):
                    One_Two = Two_One
                Two_One = Two_Two
                Two_Two = nums[i]

            elif nums[i] >= Two_One and nums[i] <Two_Two:
                if(One_One > Two_One):
                    One_Two = One_One
                    One_One = Two_One
                elif(One_Two > Two_One and One_One < Two_One):
                    One_Two = Two_One
                Two_One = nums[i]
            elif nums[i] <= One_One:
                One_Two = One_One
                One_One = nums[i]
            elif nums[i] <= One_Two and nums[i] > One_One:
                One_Two = nums[i]
        
        print(One_One , One_Two , Two_One , Two_Two)
        val = (Two_One * Two_Two) - (One_One * One_Two)
        return val