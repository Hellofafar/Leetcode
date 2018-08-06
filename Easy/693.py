# ------------------------------
# 693. Binary Number with Alternating Bits
# 
# Description:
# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
# Example 1:
# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101
# 
# Example 2:
# Input: 7
# Output: False
# Explanation:
# The binary representation of 7 is: 111.
# 
# Version: 1.0
# 08/05/18 by Jianfa
# ------------------------------

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n, rest = divmod(n, 2)
        while n:
            if rest == n % 2:
                return False
            n, rest = divmod(n, 2)
        
        return True
        

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# A mathematical solution.