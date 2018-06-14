# ------------------------------
# 172. Factorial Trailing Zeroes
# 
# Description:
# Given an integer n, return the number of trailing zeroes in n!.
# Example 1:
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# 
# Example 2:
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# 
# Note: Your solution should be in logarithmic time complexity.
# 
# Version: 1.0
# 06/09/18 by Jianfa
# ------------------------------

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        power = 1
        trailing = 0
        while n >= pow(5, power):
            trailing += n / pow(5, power)
            power += 1
            
        return trailing

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# The trailing number is actually the maximum power of factor 5 that can divide the n!