# ------------------------------
# 474. Ones and Zeroes
# 
# Description:
# In the computer world, use restricted resource you have to generate maximum benefit 
# is what we always want to pursue.
# 
# For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, 
# there is an array with strings consisting of only 0s and 1s.
# 
# Now your task is to find the maximum number of strings that you can form with given m 
# 0s and n 1s. Each 0 and 1 can be used at most once.
# 
# Note:
# The given numbers of 0s and 1s will both not exceed 100
# The size of given string array won't exceed 600.
# 
# Example 1:
# Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
# Output: 4
# Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, 
# which are “10,”0001”,”1”,”0”
# 
# Example 2:
# Input: Array = {"10", "0", "1"}, m = 1, n = 1
# Output: 2
# Explanation: You could form "10", but then you'd have nothing left. Better form "0" 
# and "1".
# 
# Version: 1.0
# 10/21/19 by Jianfa
# ------------------------------

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            numZeroes = 0
            numOnes = 0
            for c in s:
                if c == "0":
                    numZeroes += 1
                else:
                    numOnes += 1
            
            for i in range(m, numZeroes - 1, -1):
                for j in range(n, numOnes - 1, -1):
                    memo[i][j] = max(memo[i][j], memo[i-numZeroes][j-numOnes] + 1)
        
        return memo[m][n]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Dynamic programming solution from https://leetcode.com/problems/ones-and-zeroes/discuss/95814/c%2B%2B-DP-solution-with-comments
# 