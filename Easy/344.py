# ------------------------------
# Reverse String
# 
# Description:
# Write a function that takes a string as input and returns the string reversed.
# Example:
# Given s = "hello", return "olleh".
# 
# Version: 1.0
# 06/24/18 by Jianfa
# ------------------------------

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 