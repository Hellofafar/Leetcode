# ------------------------------
# 441. Arranging Coins
# 
# Description:
# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
# Given n, find the total number of full staircase rows that can be formed.
# n is a non-negative integer and fits within the range of a 32-bit signed integer.
# 
# Example 1:
# n = 5
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
# Because the 3rd row is incomplete, we return 2.
# 
# Example 2:
# n = 8
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤

# Because the 4th row is incomplete, we return 3.
# Version: 1.0
# 07/05/18 by Jianfa
# ------------------------------

import math

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        
        maxnum = int(math.sqrt(2 * n))
        if 2 * n >= (maxnum + 1) * maxnum:
            return maxnum
        
        else:
            return maxnum - 1
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Assume n >= (t+1) * t / 2
# The result is either t or (t - 1)