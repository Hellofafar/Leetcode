# ------------------------------
# 389. Find the Difference
# 
# Description:
# Given two strings s and t which consist of only lowercase letters.
# String t is generated by random shuffling string s and then add one more letter at a random position.
# Find the letter that was added in t.
# Example:
# Input:
# s = "abcd"
# t = "abcde"
# Output:
# e
# 
# Explanation:
# 'e' is the letter that was added.
# 
# Version: 1.0
# 06/27/18 by Jianfa
# ------------------------------

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = 0
        for i in s:
            res ^= ord(i)
            
        for j in t:
            res ^= ord(j)

        return chr(res)

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Bit manipulation solution