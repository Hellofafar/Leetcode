# ------------------------------
# 168. Excel Sheet Column Title
# 
# Description:
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
# For example:
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
#     ...
# Example 1:
# Input: 1
# Output: "A"
# 
# Example 2:
# Input: 28
# Output: "AB"
# 
# Example 3:
# Input: 701
# Output: "ZY"
# 
# Version: 1.0
# 06/09/18 by Jianfa
# ------------------------------

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = ''
        while n > 26:
            rest = n % 26
            if rest == 0:
                string = 'Z' + string
                n = n / 26 - 1
            else:
                string = chr(rest + 64) + string
                n = n / 26
        
        string = chr(n + 64) + string
        
        return string
            

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# An important point is this is not 26 number system since there is no 0.
# 26 is Z, but not 10.
# 52 is ZZ but not 100.