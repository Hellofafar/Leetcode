# ------------------------------
# 476. Number Complement
# 
# Description:
# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
# Note:
# The given integer is guaranteed to fit within the range of a 32-bit signed integer.
# You could assume no leading zero bit in the integer’s binary representation.
# Example 1:
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
# 
# Example 2:
# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
# 
# Version: 1.0
# 07/09/18 by Jianfa
# ------------------------------

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        for i in range(32):
            if num < 2 ** i:
                return 2 ** i - 1 - num

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Actually I solved it as a math problem. Just apply a simple rule that:
# if x is the first power of 2 that greater than num, then return x - 1 - num