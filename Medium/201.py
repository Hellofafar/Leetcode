# ------------------------------
# 201. Bitwise AND of Numbers Range
# 
# Description:
# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
# Example 1:
# Input: [5,7]
# Output: 4
# 
# Example 2:
# Input: [0,1]
# Output: 0
# 
# Version: 1.0
# 08/27/18 by Jianfa
# ------------------------------

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0:
            return 0
        
        moveFactor = 1
        while m != n:
            m >>= 1
            n >>= 1
            moveFactor <<= 1
        
        return m * moveFactor

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# From solution: https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/56729/Bit-operation-solution(JAVA)
# Key point: when m != n, There is at least an odd number and an even number, so the last bit position result is 0.