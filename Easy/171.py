# ------------------------------
# 171. Excel Sheet Column Number
# 
# Description:
# Given a column title as appear in an Excel sheet, return its corresponding column number.
# For example:
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...
# Example 1:
# Input: "A"
# Output: 1
# 
# Example 2:
# Input: "AB"
# Output: 28
# 
# Example 3:
# Input: "ZY"
# Output: 701
# 
# Version: 1.0
# 06/09/18 by Jianfa
# ------------------------------

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            res += (ord(s[i]) - 64) * pow(26, len(s) - i - 1)
        
        return res

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# 