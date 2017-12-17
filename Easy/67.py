# ------------------------------
# 67. Add Binary
# 
# Description:
# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".
# 
# Version: 1.0
# 12/17/17 by Jianfa
# ------------------------------

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b
        
        if not b:
            return a
        
        int_a = int(a, 2)
        int_b = int(b, 2)
        s = int_a + int_b
        bin_s = bin(s)[2:]
        return bin_s

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Usage of int(str, 2) and bin()