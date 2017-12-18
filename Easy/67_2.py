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
        
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1') + '0'
        
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1], b[0:-1]) + '0'
        
        else:
            return self.addBinary(a[0:-1], b[0:-1]) + '1'

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Recursion solution.
# Every time get result of last character of two strings. When 1 + 1 need to add a carry.