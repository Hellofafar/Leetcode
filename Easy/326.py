# ------------------------------
# 326. Power of Three
# 
# Description:
# Given an integer, write a function to determine if it is a power of three.
# Example 1:
# Input: 27
# Output: true
# 
# Example 2:
# Input: 0
# Output: false
# 
# Example 3:
# Input: 9
# Output: true
# 
# Example 4:
# Input: 45
# Output: false
# 
# Follow up:
# Could you do it without using any loop / recursion?
# 
# Version: 1.0
# 06/24/18 by Jianfa
# ------------------------------

import math
import sys

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        
        while n > 1:
            if n % 3 == 0:
                n = n / 3
            
            else:
                return False
        
        return True

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# One of the solution provided is mathamatic solution.
# log3(n) = log(n) / log(3), so if log(n) / log(3) is an integer, then n is power of 3.
# But I cannot use python to achieve because double divided by double may have precision error.