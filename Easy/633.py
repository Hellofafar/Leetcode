# ------------------------------
# 633. Sum of Square Numbers
# 
# Description:
# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.
# Example 1:
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# 
# Example 2:
# Input: 3
# Output: False
# 
# Version: 1.0
# 07/28/18 by Jianfa
# ------------------------------

import math

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        temp = int(math.sqrt(c))
        for a in range(temp + 1): # Take care of the range here
            b = math.sqrt(c - a*a)
            if b == int(b):
                return True
            
        return False
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Use sqrt function. Check whether c - a^2 is a square number.