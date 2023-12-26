'''
You have n dice, and each die has k faces numbered from 1 to k.
Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7. 
Example 1:
Input: n = 1, k = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces.
There is only one way to get a sum of 3.
Example 2:
Input: n = 2, k = 6, target = 7
Output: 6
Explanation: You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
'''

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = [[0]*(target+1) for _ in range(n+1)]
        dp[0][0] = 1  # base case

        for i in range(1, n+1):
            for j in range(1, target+1):
                for f in range(1, min(j, k)+1):  # face of the die
                    dp[i][j] = (dp[i][j] + dp[i-1][j-f]) % MOD

        return dp[n][target]

# We look at the previous dice sum and add all the faces available 
