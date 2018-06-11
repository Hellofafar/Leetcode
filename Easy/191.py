# ------------------------------
# 191. Number of 1 Bits
# 
# Description:
# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
# Example 1:
# Input: 11
# Output: 3
# Explanation: Integer 11 has binary representation 00000000000000000000000000001011 
# 
# Example 2:
# Input: 128
# Output: 1
# Explanation: Integer 128 has binary representation 00000000000000000000000010000000
# 
# Version: 1.0
# 06/10/18 by Jianfa
# ------------------------------

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return list(bin(n)[2:]).count('1')

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 