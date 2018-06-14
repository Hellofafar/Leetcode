# ------------------------------
# 231. Power of Two
# 
# Description:
# Given an integer, write a function to determine if it is a power of two.
# Example 1:
# Input: 1
# Output: true 
# Explanation: 20 = 1
# 
# Example 2:
# Input: 16
# Output: true
# Explanation: 24 = 16
# 
# Example 3:
# Input: 218
# Output: false
# 
# Version: 1.0
# 06/13/18 by Jianfa
# ------------------------------

import math

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if n <= 0:
        #     return False
        
        # if n == 1:
        #     return True
        
        # if n % 2 != 0:
        #     return False
        
        # while n > 2:
        #     if n % 2 != 0:
        #         return False
            
        #     temp = math.sqrt(n)
        #     if int(temp) != temp:
        #         n /= 2
                
        #     else:
        #         n = temp
        
        # return True

        if n <= 0:
            return False
        
        binary = bin(n)[2:]
        if list(binary).count('1') == 1:
            return True
        
        else:
            return False

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Take care of some boundary condition, e.g. n <= 0.
# A very smart solution is using bit manipulation: convert n to binary number.